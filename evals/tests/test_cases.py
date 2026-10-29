"""Integrity and obligation tests for synthetic original-workflow cases.

These tests validate evaluation data and deterministic controls, not agent skill success.
The integration test runs the actual CLI when the engine lane is merged.
"""
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = json.loads((ROOT / "evals/tasks.json").read_text(encoding="utf-8"))
TASKS = {task["id"]: task for task in MANIFEST["tasks"]}
REVISION = "60a18dbdda4f113c325912824dc361b35a118da5"
# Literal locks prevent an edited skill + regenerated manifest from silently redefining baseline.
ORIGINAL_LOCKS = {
    "AGENTS.md": "45cbdc23e35dc84874298eb7e767bca1b0016dca6b54b91ea3867f1e504c99a1",
    "CLAUDE.md": "4080052457b5bb292cdc719c7744b86343792e7574b32b0326dd26117eedc85c",
    "sources/README.md": "801f8e5e7047e34f86e576a3f425542f3b94f98d5f4870d4e1e236e76962dbde",
    ".claude/skills/utils/writeDocs.md": "fba39ab41ccc741db2778ed027738e9e72ddb223667849ee531d77d23669f277",
    ".claude/skills/status/SKILL.md": "f887f475761521e9a3c782d68da484e9ffbcb0adf418b54d6221538586cde321",
    ".claude/skills/shape/SKILL.md": "fd9fdd8143dbd57174a879db3e88e999bc30cebf5cc7845fe78c11c5d8d79eb4",
    ".claude/skills/strategy/SKILL.md": "8dacdf622cd54203356bdecc42c9500aaccdb4534cd9e7b8071823121d52a8f0",
    ".claude/skills/prd/SKILL.md": "fc858b2251e58f218e334bee067dff65de2aa3d895ef622d4fcbd5ede61ebbf4",
}
EXPECTED_OBLIGATIONS = {
    "source-conflict-status": {"q11-status": "Blocked", "q11-dependency": "Q-12", "q11-change": "In Progress -> Blocked"},
    "resumed-accepted-correction": {"f21-behavior": "Preview then explicit confirmation", "f21-id": "F-21", "f21-publication": "Not authorized"},
    "proposal-vs-approval-shape": {"shape-stage": "Awaiting operator response to Step 0", "mode-selection": "Unresolved", "build-approval": "Absent"},
    "unavailable-source-recovery": {"metrics-availability": "Unavailable", "metrics-current-value": "Unknown", "metrics-refreshed": "No"},
    "completion-evidence-gap": {"launch-verdict": "No-Go", "p0-verification": "Not run", "implementation-ticket": "Done"},
    "instruction-in-source-authority": {"q61-status": "Blocked", "source-instruction": "Untrusted data", "source-action-authority": "Absent"},
    "heldout-owner-dependency": {"q71-owner": "Lead-B", "q72-owner": "Lead-C", "q71-status": "Blocked", "proposed-reassignment": "Unaccepted"},
    "heldout-strategy-unsupported-claims": {"observed-impact": "Unmeasured", "approved-scope": "Local reviewer-ownership pilot", "resource-approval": "Unresolved", "market-leadership": "Unsupported"},
}


def table_rows(text):
    """Extract only the control table for control-pair integrity, not production grading."""
    table = text.split("## Evaluation Results", 1)[1]
    result = {}
    for line in table.splitlines():
        if line.startswith("| "):
            cells = [c.strip() for c in line.strip("| ").split("|")]
            if len(cells) == 3 and cells[0] != "ID":
                result[cells[0]] = cells[1:]
    return result


class CaseIntegrityTests(unittest.TestCase):
    def test_fixed_original_source_bytes(self):
        self.assertEqual(MANIFEST["baselineSourceRevision"], REVISION)
        self.assertEqual(MANIFEST["sourceHashes"], ORIGINAL_LOCKS)
        for rel, expected in ORIGINAL_LOCKS.items():
            with self.subTest(source=rel):
                self.assertEqual(hashlib.sha256((ROOT / rel).read_bytes()).hexdigest(), expected)

    def test_eight_distinct_original_skill_tasks_and_partition(self):
        self.assertEqual(set(TASKS), set(EXPECTED_OBLIGATIONS))
        self.assertEqual(len(MANIFEST["tasks"]), 8)
        heldout = {t["id"] for t in TASKS.values() if t["split"] == "heldout"}
        self.assertEqual(heldout, {"heldout-owner-dependency", "heldout-strategy-unsupported-claims"})
        self.assertEqual(sum(t["split"] == "development" for t in TASKS.values()), 6)
        self.assertEqual({t["skill"] for t in TASKS.values()}, {".claude/skills/" + s + "/SKILL.md" for s in ("status", "shape", "strategy", "prd")})
        for task in TASKS.values():
            readme = (ROOT / task["fixture"]).parent.joinpath("README.md").read_text()
            self.assertIn("not secret test data", readme)
            self.assertIn("Neither control is an observed agent outcome", readme)

    def test_finite_source_references_have_real_seeded_records(self):
        for task in TASKS.values():
            with self.subTest(task=task["id"]):
                workspace = ROOT / task["fixture"]
                records = "\n".join(p.read_text() for p in workspace.rglob("*") if p.is_file())
                refs = set(task["sourceRefs"])
                self.assertEqual(len(refs), len(task["sourceRefs"]))
                for ref in refs:
                    self.assertRegex(records, r"(?<![A-Z0-9-])" + re.escape(ref) + r"(?![A-Z0-9-])")
                for check in task["checks"]:
                    if check["kind"] == "row_equals":
                        self.assertTrue(check["sources"])
                        self.assertLessEqual(set(check["sources"]), refs)

    def test_explicit_obligations_remain_in_rubric(self):
        for case, expected in EXPECTED_OBLIGATIONS.items():
            rows = {c["key"]: c["value"] for c in TASKS[case]["checks"] if c["kind"] == "row_equals"}
            for key, value in expected.items():
                with self.subTest(task=case, obligation=key):
                    self.assertEqual(rows[key], value)

    def test_controls_are_outside_workspace_with_one_intentional_claim_failure(self):
        for task in TASKS.values():
            with self.subTest(task=task["id"]):
                workspace = ROOT / task["fixture"]
                controls = []
                for kind in ("positive", "negative"):
                    path = ROOT / task["calibration"][kind]
                    self.assertNotIn(workspace, path.parents)
                    text = path.read_text()
                    self.assertIn("deterministic grader calibration", text)
                    self.assertIn("not a model run", text)
                    controls.append(table_rows(text))
                positive, negative = controls
                differences = [key for key in positive if positive[key] != negative[key]]
                self.assertEqual(len(differences), 1, "Negative must isolate one substantive wrong claim")
                self.assertEqual(set(positive), {c["key"] for c in task["checks"] if c["kind"] == "row_equals"})
                self.assertTrue(task["controlLabels"]["negative"].startswith("deliberate_"))
                # Check expected refs and literals independently of the CLI, including stale-copy controls.
                for check in task["checks"]:
                    if check["kind"] == "row_equals":
                        value, refs = positive[check["key"]]
                        self.assertEqual(value, check["value"])
                        self.assertEqual({s.strip() for s in refs.split(",")}, set(check["sources"]))
                    elif check["kind"] == "forbidden_text":
                        self.assertNotIn(check["value"], (ROOT / task["calibration"]["positive"]).read_text())

    def test_fixture_paths_cannot_replace_original_skills_or_leak_controls(self):
        for task in TASKS.values():
            workspace = ROOT / task["fixture"]
            self.assertTrue(workspace.is_dir())
            for path in workspace.rglob("*"):
                self.assertFalse(path.is_symlink())
                if path.is_file():
                    rel = path.relative_to(workspace).as_posix()
                    self.assertNotIn(rel, ORIGINAL_LOCKS)
                    self.assertFalse(rel.startswith(".claude/"))
                    self.assertNotIn(path.name, {"positive.md", "negative.md", "tasks.json"})
                    self.assertNotIn("## Evaluation Results", path.read_text())
            self.assertEqual(task["allowedOutputs"], [task["artifact"]])
            self.assertFalse(Path(task["artifact"]).is_absolute())
            self.assertNotIn("..", Path(task["artifact"]).parts)
            self.assertIn("Evaluation Results", task["requiredHeadings"])

    def test_missing_dependencies_are_disclosed_and_never_synthesized(self):
        voice = ".claude/skills/utils/voice.md"
        registry = ".claude/skills/utils/sources.md"
        self.assertFalse((ROOT / voice).exists())
        self.assertFalse((ROOT / registry).exists())
        for task in TASKS.values():
            self.assertIn(voice, task["dependencies"])
            if "/status/" in task["skill"]:
                self.assertIn(registry, task["dependencies"])
            readme = (ROOT / task["fixture"]).parent.joinpath("README.md").read_text()
            self.assertIn("not_reached", readme)
            self.assertIn(voice, readme)
            self.assertFalse((ROOT / task["fixture"] / voice).exists())

    def test_clean_synthetic_fixture_content(self):
        # Generic patterns guard personal paths/credentials without publishing real identifiers.
        patterns = [r"/Users/", r"/home/[^/]+/", r"sk-(?:proj-)?[A-Za-z0-9]{12,}", r"-----BEGIN .*PRIVATE KEY", r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", r"https?://"]
        for task in TASKS.values():
            for path in (ROOT / task["fixture"]).parent.rglob("*"):
                if path.is_file():
                    text = path.read_text()
                    for pattern in patterns:
                        with self.subTest(path=str(path.relative_to(ROOT)), pattern=pattern):
                            self.assertIsNone(re.search(pattern, text))

    def test_resumption_contains_prior_wrong_copy_and_explicit_latest_correction(self):
        task = TASKS["resumed-accepted-correction"]
        prior = ROOT / task["fixture"] / task["artifact"]
        self.assertIn("No confirmation is needed", prior.read_text())
        self.assertIn("Accepted correction USER-21", task["request"])
        control = (ROOT / task["calibration"]["positive"]).read_text()
        for stale in ("No confirmation is needed", "publishes automatically", "Publish on the save event"):
            self.assertNotIn(stale, control)

    def test_shape_control_honors_unresolved_original_checkpoint(self):
        task = TASKS["proposal-vs-approval-shape"]
        original = (ROOT / task["skill"]).read_text()
        self.assertIn("Wait for the user to respond before selecting mode", original)
        positive = (ROOT / task["calibration"]["positive"]).read_text()
        self.assertIn("Step 0 needs the operator response first", positive)
        self.assertNotIn("## 5ft", positive)
        self.assertIn("Not reached", positive)

    def test_actual_engine_calibration_rejects_deliberate_negative_controls(self):
        engine = ROOT / "evals/company_os_eval.py"
        if not engine.exists():
            self.skipTest("Engine lane is not merged; run again after integration")
        with tempfile.TemporaryDirectory(prefix="case-calibration-") as tmp:
            out = Path(tmp) / "controls"
            result = subprocess.run([sys.executable, str(engine), "calibrate", "--out", str(out)], cwd=ROOT, text=True, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertTrue(out.is_dir())
            files = [p for p in out.rglob("*") if p.is_file()]
            self.assertTrue(files, "Calibration must retain evidence")
            payload = "\n".join(p.read_text() for p in files if p.suffix in (".json", ".md"))
            for task in TASKS:
                self.assertIn(task, payload)
            summary = json.loads(result.stdout)
            self.assertEqual(summary["classification"], "grader_calibration")
            self.assertTrue(summary["deterministic"])
            self.assertEqual(summary["actualModelTrials"], 0)
            self.assertEqual(summary["controlCount"], 16)
            self.assertEqual(summary["detectedExpected"], 16)
            self.assertEqual(summary["falsePositiveControls"], 0)
            self.assertEqual(summary["falseNegativeControls"], 0)
            self.assertTrue(summary["passed"])
            pairs = {(r["taskId"], r["control"]): r for r in summary["records"]}
            self.assertEqual(set(pairs), {(task, kind) for task in TASKS for kind in ("positive", "negative")})
            for (task, kind), record in pairs.items():
                self.assertEqual(record["artifactOutcome"], "pass" if kind == "positive" else "fail")
                self.assertTrue(record["calibrationPassed"])
                self.assertEqual(record["controlOrigin"], "hand_authored_not_model")
                if kind == "negative":
                    failed = [c for c in record["checks"] if not c["passed"]]
                    self.assertEqual(len(failed), 1, "Each deliberate wrong claim must be caught once")
                    self.assertEqual(failed[0]["kind"], "row_equals")


if __name__ == "__main__":
    unittest.main()
