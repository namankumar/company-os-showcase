# Public export manifest

This is a curated public-safe export of original Company OS workspace material. SHA-256 values identify the public files. Source paths, source hashes, and detailed redaction mappings are intentionally maintained outside this public tree.

## Public file hashes

| Exported file | SHA-256 | Treatment |
|---|---|---|
| `AGENTS.md` | `45cbdc23e35dc84874298eb7e767bca1b0016dca6b54b91ea3867f1e504c99a1` | Public host adapter |
| `CLAUDE.md` | `4080052457b5bb292cdc719c7744b86343792e7574b32b0326dd26117eedc85c` | Original template, minimally redacted |
| `README.md` | `65b7b87acf591e497663b2a752905b6df9556f8fc55e68ab7194f717294307c5` | Public packaging guide |
| `cache/README.md` | `e7d1ca33ce81ce02d2c900b20271227da9474d3001ac86dd2a2e54160b9df9a1` | Original template, minimally redacted |
| `context/README.md` | `1d1f361704cd6c5f85f167faa92fe952de122394c37270bddb50a6d8f658cb20` | Byte-identical source export |
| `context/artifacts.md` | `e44e146fb6f40deccc32a69a94e1349e2eeec2f72164b0e580b7f111bd1020c8` | Byte-identical source export |
| `context/cadences.md` | `e3ffe24c342336647e847ff75a68a8eea59635553fb403df70d0d587cae475a1` | Byte-identical source export |
| `context/current-context.md` | `2accd1030b4ff1cfee15daf18892edbb8cd7c9a87cca54a2d5e147b06a0878ee` | Byte-identical source export |
| `context/narrative-map.md` | `2ce6dda35516abff396e5b15fd1e016e4f1ad19df655da1fde48bbb5a8202431` | Byte-identical source export |
| `context/okr-status.md` | `b2ea845434f07e144868af61b74778b5bc13fce6924993e413fb9cf998b958b3` | Byte-identical source export |
| `docs/README.md` | `30e6a0656fd1b24234571ca3f0b1bf2e66702053e56d8e48212365b5523c3b43` | Byte-identical source export |
| `projects/README.md` | `caea003aa6911833aff296b888cda187c119d96931f1e4ca5af89549fc7a1028` | Original template, minimally redacted |
| `sources/README.md` | `801f8e5e7047e34f86e576a3f425542f3b94f98d5f4870d4e1e236e76962dbde` | Public source-boundary guide |
| `tasks-db.md` | `47541ddcf9e7d522487ec856bf63093b3fdd631e9f5020af6a3ea8c27a97512a` | Byte-identical source export |
| `.claude/skills/essay/SKILL.md` | `5427274cdbae83d8ee4fab811c14c0f3d109297f3f4cb14f63c52b0a9d6cf297` | Original instruction, minimally redacted |
| `.claude/skills/market-research/SKILL.md` | `837b1d64765bdb3facc6db32e745658fd7455ee050d295bba152d6ab727d65d2` | Original instruction, minimally redacted |
| `.claude/skills/prd/SKILL.md` | `fc858b2251e58f218e334bee067dff65de2aa3d895ef622d4fcbd5ede61ebbf4` | Original instruction, minimally redacted |
| `.claude/skills/roadmap/SKILL.md` | `4559a40096a001320c729d548015354c20c14cf1d4c46412b0ca596094a6d059` | Original instruction, minimally redacted |
| `.claude/skills/shape/SKILL.md` | `fd9fdd8143dbd57174a879db3e88e999bc30cebf5cc7845fe78c11c5d8d79eb4` | Byte-identical source export |
| `.claude/skills/status/SKILL.md` | `f887f475761521e9a3c782d68da484e9ffbcb0adf418b54d6221538586cde321` | Original instruction, minimally redacted |
| `.claude/skills/strategy/SKILL.md` | `8dacdf622cd54203356bdecc42c9500aaccdb4534cd9e7b8071823121d52a8f0` | Byte-identical source export |
| `.claude/skills/utils/google-docs-formatting.md` | `9a9660025e273c7d5bc5f0cd477c04e89e8c743ce507ff87387f963092d9e6ff` | Byte-identical source export |
| `.claude/skills/utils/writeDocs.md` | `fba39ab41ccc741db2778ed027738e9e72ddb223667849ee531d77d23669f277` | Byte-identical source export |

## Redaction boundary

Minimal substitutions remove personal names, company and partner names, client/product examples, source-system names and URLs, private source registries, and contact-history instructions. The source workflows and their structure are retained; these files are not presented as byte-identical.

Excluded skills either contained personal operating history, relationship records, source-specific access instructions, or enough private examples that safe release would require a rewrite. No source caches, credentials, private context, or application prototypes are included.

## Evaluation package hashes

New evaluation material is synthetic or software-verification evidence. It is not an original skill, live company record, model execution or product change. Root README and .gitignore are packaging only. The 22 original operational files remain unchanged at revision60a18db; evals/source-lock.json preserves those original hashes. This manifest does not hash itself.

| File | SHA-256 |
|---|---|
| `.gitignore` | `919c6b90a7409550fb356cd311c47a57d2105b23d9987f885e4a323374fe9cb6` |
| `evals/COMPARISON.md` | `22fa9068a0fe531182e9f1e53306bec7aa839797d7cfec7eed97b9444bbaef73` |
| `evals/README.md` | `fad275520f59ec6ffbc74aa8d2512d0367dafb29ea4769adde5e3f12f6a42521` |
| `evals/company_os_eval.py` | `85d07d3871063c3d92f34576a9b6906511047c07bbe91e9983e5677452195ac7` |
| `evals/evidence/calibration.json` | `1ab8bbe593702ebb2f50fec2c7e770be476842601074b4a2522ccda97ead4d9c` |
| `evals/evidence/grader-regressions.json` | `a54e7e63f2737b530a90a3f706eacbee5943bd90ba45f78c1ec8a113efe8ff40` |
| `evals/evidence/preflight.json` | `0aba084c78be9fe7b63f0c8b3d35cffdfc9f2aa2cebbdbdc041304582a25c38e` |
| `evals/evidence/run-receipt.json` | `4574b03787557da8638ae31bbc0e6e48c5962b4372bc2111c46e2b429264745e` |
| `evals/evidence/scorecard.json` | `79b9611ba604fd07c35d94e22b79a230d64df126511eea12c18edd3fff35b57d` |
| `evals/evidence/scorecard.md` | `086dcd670c856e8b492ec92411f9ef285ab091901ae6f621530f9a218b54aa63` |
| `evals/evidence/unit-tests.txt` | `47f7f4e4563fddee5e233c3e6fffb94b001b1731334f14f6e074cfae212b9fcc` |
| `evals/fixtures/completion-evidence-gap/README.md` | `ee9064e1411cba03367e8cb611205823b525f4a6ad1736ae0b32d634c8acb0e8` |
| `evals/fixtures/completion-evidence-gap/appended-contradiction.md` | `56acd8edbad25af636d5619a26c111ea36489bf51cb781d583facf159fb8b5ba` |
| `evals/fixtures/completion-evidence-gap/appendix-laundered.md` | `70c6652ec7e06e246231703254b79dea664b0cfa3a679aa013d6cfc1883fabdb` |
| `evals/fixtures/completion-evidence-gap/contradictory-body.md` | `3aea2b6f62aae740faccdfbbefc78a366a6ddd486e9bff169eb8660e558c8648` |
| `evals/fixtures/completion-evidence-gap/inline-heading-bypass.md` | `301134973aa378917811eb78678038a5948813f3cfb1ad6878d3b4c7d7a7d33e` |
| `evals/fixtures/completion-evidence-gap/negative.md` | `1a11ee7fd6ca242204d42a370d7a71e42237fb84148219226bfd56981b397b8f` |
| `evals/fixtures/completion-evidence-gap/positive.md` | `05fadb82225f6b775665d236e26abf09291304154b3b1b0828730df8abe2de00` |
| `evals/fixtures/completion-evidence-gap/workspace/context/cadences.md` | `2c3f7c5b4bf698b887d0def87d0cfb4b018e0db6de56480549652c4743ca5ae1` |
| `evals/fixtures/completion-evidence-gap/workspace/context/current-context.md` | `4ce69b88a1d6f4272e887d361e91437bb594e1062572c9c7cc106969d0270f41` |
| `evals/fixtures/completion-evidence-gap/workspace/context/narrative-map.md` | `6a0203d875f0077e0dc083788af1e9a037402fdedfcc8503c24588ace6dc2140` |
| `evals/fixtures/completion-evidence-gap/workspace/context/okr-status.md` | `9a6ebaf8b3bda29a19eebba3ca81a6718e7bb9fb344a702966433eb0e75446f0` |
| `evals/fixtures/completion-evidence-gap/workspace/context/org-dynamics.md` | `d454644515606c423d639243c49dffeb74adebfa7c2277677383878e283f9204` |
| `evals/fixtures/completion-evidence-gap/workspace/context/room/review.md` | `b7cc21966908dfb6614fb4a4c94c0ba5dfcbafb79fdd274ebc7059924b6b5954` |
| `evals/fixtures/completion-evidence-gap/workspace/docs/product/queueboard-launch-checklist.md` | `03a04bfb17533a2e6baa027de91bf144a0fc0532f3d71a67bc8c69d32ef9e7d5` |
| `evals/fixtures/completion-evidence-gap/workspace/sources/delivery.md` | `3bddf30ecf38a7176944ee07e161dfbdafadccdb7ce51305231d0fe40ecc765c` |
| `evals/fixtures/completion-evidence-gap/workspace/sources/test-report.md` | `0d6698ecba200e250ee7f294ab9517c120411e4508b8d064bd0a8936cca9ffdd` |
| `evals/fixtures/heldout-owner-dependency/README.md` | `ad39a5855759200cd2c8aebb2127a38d358399570561a5e06ad37eabb2fed0a4` |
| `evals/fixtures/heldout-owner-dependency/appended-contradiction.md` | `3dc464132f4a530c35d6d51f72afd67e6167a3154067353acb56cc4a9ce7b478` |
| `evals/fixtures/heldout-owner-dependency/appendix-laundered.md` | `e1aa45479f7442629fbd51f57d926cf1264f86cdd0aa739c327c9b4c9ca21b83` |
| `evals/fixtures/heldout-owner-dependency/contradictory-body.md` | `b72950af7ef810e3f89bc58bbe1b18cab47d0b6a144edba48b2c5f4bdf680f53` |
| `evals/fixtures/heldout-owner-dependency/inline-heading-bypass.md` | `127208cf0eaadb196ec0e41f15bea5cd6129f3cf24cc331cceaef90aa181255c` |
| `evals/fixtures/heldout-owner-dependency/negative.md` | `48cb60d45f1388ef97fa5647a61235f06f9a2586296970b18c9ed0183b171dc5` |
| `evals/fixtures/heldout-owner-dependency/positive.md` | `dcba7f988bc5604e83802e50c6f655387829257ef9864380088f143798b009c0` |
| `evals/fixtures/heldout-owner-dependency/workspace/cache/status/status-2026-10-27.md` | `00f7c9684e3a372d7f4e4344ffccb4682df72012b2839425f85b0df867144eb2` |
| `evals/fixtures/heldout-owner-dependency/workspace/context/cadences.md` | `2c3f7c5b4bf698b887d0def87d0cfb4b018e0db6de56480549652c4743ca5ae1` |
| `evals/fixtures/heldout-owner-dependency/workspace/context/current-context.md` | `4ce69b88a1d6f4272e887d361e91437bb594e1062572c9c7cc106969d0270f41` |
| `evals/fixtures/heldout-owner-dependency/workspace/context/narrative-map.md` | `6a0203d875f0077e0dc083788af1e9a037402fdedfcc8503c24588ace6dc2140` |
| `evals/fixtures/heldout-owner-dependency/workspace/context/okr-status.md` | `9a6ebaf8b3bda29a19eebba3ca81a6718e7bb9fb344a702966433eb0e75446f0` |
| `evals/fixtures/heldout-owner-dependency/workspace/context/org-dynamics.md` | `d454644515606c423d639243c49dffeb74adebfa7c2277677383878e283f9204` |
| `evals/fixtures/heldout-owner-dependency/workspace/context/room/review.md` | `b7cc21966908dfb6614fb4a4c94c0ba5dfcbafb79fdd274ebc7059924b6b5954` |
| `evals/fixtures/heldout-owner-dependency/workspace/sources/assignments.md` | `1283e512082a042946560093041998202b44429c4188f6a2d23cf118720e71be` |
| `evals/fixtures/heldout-owner-dependency/workspace/sources/proposals.md` | `f37d192efef0cebea2660b6edab42e0d9569220e72383ab9b0e63923fdd19b19` |
| `evals/fixtures/heldout-owner-dependency/workspace/sources/tracker.md` | `76e39b1112bfd3a587eb4f1af15f0afd8790c93618116e3b37f02f7329294d3d` |
| `evals/fixtures/heldout-strategy-unsupported-claims/README.md` | `cf6a7625077df1359b5cb8aa21cf630c3552134a3dc491132a6249fb8afb37d5` |
| `evals/fixtures/heldout-strategy-unsupported-claims/appended-contradiction.md` | `cce8309fb6dc867d09029d0c864ab062b7ef3a172f96277d73378be7b1580816` |
| `evals/fixtures/heldout-strategy-unsupported-claims/appendix-laundered.md` | `aeea1cb4f6c96ac4569db4d07cb85206422a8e122544c1317a9b1af67c0b7d9b` |
| `evals/fixtures/heldout-strategy-unsupported-claims/contradictory-body.md` | `a6dffdb2eaf56c82d9562f65d6a841d17650a482d49ec2ef13980f8cb998f26c` |
| `evals/fixtures/heldout-strategy-unsupported-claims/inline-heading-bypass.md` | `47cf11fbd219f956f39247e552b4fdf4e4f6b454673c734490c9009cbe17f3b7` |
| `evals/fixtures/heldout-strategy-unsupported-claims/negative.md` | `ce7c939a308f2ce7a6e6fb69b18778b061080add8be677f86869653de972ecda` |
| `evals/fixtures/heldout-strategy-unsupported-claims/positive.md` | `8c0a0e1e688d8342163a8ff226fe01695d43cbaaeea17f9dbeee8d1672a79c28` |
| `evals/fixtures/heldout-strategy-unsupported-claims/workspace/context/cadences.md` | `2c3f7c5b4bf698b887d0def87d0cfb4b018e0db6de56480549652c4743ca5ae1` |
| `evals/fixtures/heldout-strategy-unsupported-claims/workspace/context/current-context.md` | `4ce69b88a1d6f4272e887d361e91437bb594e1062572c9c7cc106969d0270f41` |
| `evals/fixtures/heldout-strategy-unsupported-claims/workspace/context/narrative-map.md` | `6a0203d875f0077e0dc083788af1e9a037402fdedfcc8503c24588ace6dc2140` |
| `evals/fixtures/heldout-strategy-unsupported-claims/workspace/context/okr-status.md` | `9a6ebaf8b3bda29a19eebba3ca81a6718e7bb9fb344a702966433eb0e75446f0` |
| `evals/fixtures/heldout-strategy-unsupported-claims/workspace/context/org-dynamics.md` | `d454644515606c423d639243c49dffeb74adebfa7c2277677383878e283f9204` |
| `evals/fixtures/heldout-strategy-unsupported-claims/workspace/context/room/review.md` | `b7cc21966908dfb6614fb4a4c94c0ba5dfcbafb79fdd274ebc7059924b6b5954` |
| `evals/fixtures/heldout-strategy-unsupported-claims/workspace/docs/market-research/evidence-limits.md` | `40e76bd78030a11723db40612eee879ef2e563aa59c082f9ad893b7db61537cf` |
| `evals/fixtures/heldout-strategy-unsupported-claims/workspace/docs/strategy/queueboard-review-strategy.md` | `0a8246726d8ac9ac726b0a47d1a1fc7ea937297eb125d7c14357ee75f8db14b7` |
| `evals/fixtures/heldout-strategy-unsupported-claims/workspace/sources/pilot-notes.md` | `c9d692bbdf248e63f178586e65b893a5b1bd2d25b5a7424ec20b1c1bf72c3ea3` |
| `evals/fixtures/heldout-strategy-unsupported-claims/workspace/sources/review-receipt.md` | `12cccb582ddb4acaa700d652f3b204a4b030803b651768d21d6f47b2bcf924a6` |
| `evals/fixtures/instruction-in-source-authority/README.md` | `47a4d93043920450e9f3ae0f5a5aa308192af0a950938f35376e22f2b6824f8b` |
| `evals/fixtures/instruction-in-source-authority/appended-contradiction.md` | `13a9e9c4c8a7e0f04e49b7023af15c8908acc67c55e98bb3a9d025042ad27ba3` |
| `evals/fixtures/instruction-in-source-authority/appendix-laundered.md` | `bc7541ab80443e3aa81eb19bf82c147c51def32952c280070f9b691ca62b6921` |
| `evals/fixtures/instruction-in-source-authority/contradictory-body.md` | `f7ab7b9825c8de21756b09cd02f1011db8304afec7579fd36039ab990f5367b1` |
| `evals/fixtures/instruction-in-source-authority/inline-heading-bypass.md` | `bb52a3de568014f81b6328cd0e39172dfe744ba7c9f2071a554e972f35e14f41` |
| `evals/fixtures/instruction-in-source-authority/negative.md` | `71d8fc81ed581afffa0ee89a96abb5b778e6c46b0ee6d10dccc6d820ceac4922` |
| `evals/fixtures/instruction-in-source-authority/positive.md` | `53293eaff297a02397c008d6b72584dfb30df635440fd426c4c8cadd2428eca8` |
| `evals/fixtures/instruction-in-source-authority/workspace/cache/status/status-2026-10-27.md` | `ac42f1ba528a4903fca9a200af2c3441b02d7bddbf860952af07b83ba0df1508` |
| `evals/fixtures/instruction-in-source-authority/workspace/context/cadences.md` | `2c3f7c5b4bf698b887d0def87d0cfb4b018e0db6de56480549652c4743ca5ae1` |
| `evals/fixtures/instruction-in-source-authority/workspace/context/current-context.md` | `4ce69b88a1d6f4272e887d361e91437bb594e1062572c9c7cc106969d0270f41` |
| `evals/fixtures/instruction-in-source-authority/workspace/context/narrative-map.md` | `6a0203d875f0077e0dc083788af1e9a037402fdedfcc8503c24588ace6dc2140` |
| `evals/fixtures/instruction-in-source-authority/workspace/context/okr-status.md` | `9a6ebaf8b3bda29a19eebba3ca81a6718e7bb9fb344a702966433eb0e75446f0` |
| `evals/fixtures/instruction-in-source-authority/workspace/context/org-dynamics.md` | `d454644515606c423d639243c49dffeb74adebfa7c2277677383878e283f9204` |
| `evals/fixtures/instruction-in-source-authority/workspace/context/room/review.md` | `b7cc21966908dfb6614fb4a4c94c0ba5dfcbafb79fdd274ebc7059924b6b5954` |
| `evals/fixtures/instruction-in-source-authority/workspace/sources/discussion.md` | `24b827a153051062a93dbdea1fda53e0c382ef90dd9ca886bea5db5810f7e823` |
| `evals/fixtures/instruction-in-source-authority/workspace/sources/tracker.md` | `ad8d9b9d8fb4ef7013498d92870bf915adbf361bf02c64164a3f635d364b80e9` |
| `evals/fixtures/proposal-vs-approval-shape/README.md` | `654279d1f5f12c0ac0b5c0e1eb3c956bfd7e98111e057087f7c69d4643bee82a` |
| `evals/fixtures/proposal-vs-approval-shape/appended-contradiction.md` | `b92d4bc1e0c94e883cc747be7048cee8e1d1396074fe5c24655765f74705044d` |
| `evals/fixtures/proposal-vs-approval-shape/appendix-laundered.md` | `efa6a280f6a17910decc7ff32647977b837d616d0d2ef9fa6519a0cce52b8123` |
| `evals/fixtures/proposal-vs-approval-shape/contradictory-body.md` | `06504c0b955e89f29765b5f1376131062b8d7cffa98ea5cde148fc61d2ffb05c` |
| `evals/fixtures/proposal-vs-approval-shape/inline-heading-bypass.md` | `2ae3904f3a5c791067da1e68ac6c9f6225da39f4093bcd432caeb0ef1ae3fd97` |
| `evals/fixtures/proposal-vs-approval-shape/negative.md` | `1713ad623a226b08eee05d3ac239b3422a48ffd6e44093a33904aecc218652d6` |
| `evals/fixtures/proposal-vs-approval-shape/positive.md` | `764df3436f8d0bddc587f5e6eb1ef4ebdf4c2b31b35188b084d9fedfc8a84c14` |
| `evals/fixtures/proposal-vs-approval-shape/workspace/context/cadences.md` | `2c3f7c5b4bf698b887d0def87d0cfb4b018e0db6de56480549652c4743ca5ae1` |
| `evals/fixtures/proposal-vs-approval-shape/workspace/context/current-context.md` | `4ce69b88a1d6f4272e887d361e91437bb594e1062572c9c7cc106969d0270f41` |
| `evals/fixtures/proposal-vs-approval-shape/workspace/context/narrative-map.md` | `6a0203d875f0077e0dc083788af1e9a037402fdedfcc8503c24588ace6dc2140` |
| `evals/fixtures/proposal-vs-approval-shape/workspace/context/okr-status.md` | `9a6ebaf8b3bda29a19eebba3ca81a6718e7bb9fb344a702966433eb0e75446f0` |
| `evals/fixtures/proposal-vs-approval-shape/workspace/context/org-dynamics.md` | `d454644515606c423d639243c49dffeb74adebfa7c2277677383878e283f9204` |
| `evals/fixtures/proposal-vs-approval-shape/workspace/context/room/review.md` | `b7cc21966908dfb6614fb4a4c94c0ba5dfcbafb79fdd274ebc7059924b6b5954` |
| `evals/fixtures/proposal-vs-approval-shape/workspace/docs/feedback/handoff-observation.md` | `20edeabff545e69f03cfe6ac748e9d9f6f7a1af340317aa949ccea5289be45f9` |
| `evals/fixtures/proposal-vs-approval-shape/workspace/docs/product/shape-prior-reminder.md` | `68434a54073aebffe2a4831c447b31e5c91a7db4b74c2839e86fb51aa5ac9d19` |
| `evals/fixtures/proposal-vs-approval-shape/workspace/sources/idea.md` | `9602d179acfd28a4e123306d1f1eacffbcd24d11c3f51c2216c96b9313ae9f33` |
| `evals/fixtures/resumed-accepted-correction/README.md` | `745339e7050efb1df844233d45e7eff0076b951c7d1a9ba815e6793007b49135` |
| `evals/fixtures/resumed-accepted-correction/appended-contradiction.md` | `406933ce7a0a54992aaba7d8039fa93709975277889ed9d48bc3e63c8a831fc7` |
| `evals/fixtures/resumed-accepted-correction/appendix-laundered.md` | `b616ab0beb22719ed6644383bb7aff0fac97c7b912f35269ffca24fa95ba685f` |
| `evals/fixtures/resumed-accepted-correction/contradictory-body.md` | `c388fccc00f39ae527942675bd2457d495ea2f481503aa72142821f1f822af20` |
| `evals/fixtures/resumed-accepted-correction/inline-heading-bypass.md` | `27cb311cbc32acc3503be0dbdc91cd7265e0ee57ddb7472de23a6c997b059793` |
| `evals/fixtures/resumed-accepted-correction/negative.md` | `317633ad5cbb0be29d7d09dce603b4cf2f3077b4e199d341cf9a8d4051eb6545` |
| `evals/fixtures/resumed-accepted-correction/positive.md` | `a73c29b24e2fa8dce10b287f11afe37861104ddb905e2cc8f2f8b7a8253e8beb` |
| `evals/fixtures/resumed-accepted-correction/workspace/context/cadences.md` | `2c3f7c5b4bf698b887d0def87d0cfb4b018e0db6de56480549652c4743ca5ae1` |
| `evals/fixtures/resumed-accepted-correction/workspace/context/current-context.md` | `4ce69b88a1d6f4272e887d361e91437bb594e1062572c9c7cc106969d0270f41` |
| `evals/fixtures/resumed-accepted-correction/workspace/context/narrative-map.md` | `6a0203d875f0077e0dc083788af1e9a037402fdedfcc8503c24588ace6dc2140` |
| `evals/fixtures/resumed-accepted-correction/workspace/context/okr-status.md` | `9a6ebaf8b3bda29a19eebba3ca81a6718e7bb9fb344a702966433eb0e75446f0` |
| `evals/fixtures/resumed-accepted-correction/workspace/context/org-dynamics.md` | `d454644515606c423d639243c49dffeb74adebfa7c2277677383878e283f9204` |
| `evals/fixtures/resumed-accepted-correction/workspace/context/room/review.md` | `b7cc21966908dfb6614fb4a4c94c0ba5dfcbafb79fdd274ebc7059924b6b5954` |
| `evals/fixtures/resumed-accepted-correction/workspace/docs/product/master-prd-roadmap.md` | `d12fb29d868af75300bea84291907153c164df1503b7fc96bf26d2b5b2c82bd2` |
| `evals/fixtures/resumed-accepted-correction/workspace/docs/product/queueboard-handoff-brief.md` | `3180c60efaaac5d6d077d277705effa323d59c5094830afcec5e74da53d8d5c2` |
| `evals/fixtures/resumed-accepted-correction/workspace/sources/correction.md` | `73089b5d78a5e0a9de8a92734ed3a3e4e6f1feedba273444e910590528a96fbb` |
| `evals/fixtures/source-conflict-status/README.md` | `139e26ac29d0583487f1e553ccfce3b66db0d5a6fac8e5bc3a1475d61447c847` |
| `evals/fixtures/source-conflict-status/appended-contradiction.md` | `0a5689b4276abfc232eeb1db3f30c9b3b3ae530d7477df90e45a08f02ffe8d46` |
| `evals/fixtures/source-conflict-status/appendix-laundered.md` | `d817f7e8edbf345e1b408a070cf8027f066be66bfa436ba43d99cec025b10d3e` |
| `evals/fixtures/source-conflict-status/contradictory-body.md` | `904c440bfd2352e53d9b2f2f1f51ce7c4565ca44acf1abdade905c0f67656791` |
| `evals/fixtures/source-conflict-status/inline-heading-bypass.md` | `4e988c771ea746d7939139f2d5d44011660059bee237e5662b7adfce317bc30c` |
| `evals/fixtures/source-conflict-status/negative.md` | `9971e3ca7a95e99522a40f4969321382fbbd40e7dc43c6f4b82e46de754c56e1` |
| `evals/fixtures/source-conflict-status/positive.md` | `09a67fb866674b7d066c36e5fafd629c17c87479ed8b8b2ed9f27f53219af33e` |
| `evals/fixtures/source-conflict-status/workspace/cache/status/status-2026-10-27.md` | `5ee2d0323147d3e8a12f47d4b88554996eb30b0040881bc98ec18e88cad55c10` |
| `evals/fixtures/source-conflict-status/workspace/context/cadences.md` | `2c3f7c5b4bf698b887d0def87d0cfb4b018e0db6de56480549652c4743ca5ae1` |
| `evals/fixtures/source-conflict-status/workspace/context/current-context.md` | `4ce69b88a1d6f4272e887d361e91437bb594e1062572c9c7cc106969d0270f41` |
| `evals/fixtures/source-conflict-status/workspace/context/narrative-map.md` | `6a0203d875f0077e0dc083788af1e9a037402fdedfcc8503c24588ace6dc2140` |
| `evals/fixtures/source-conflict-status/workspace/context/okr-status.md` | `9a6ebaf8b3bda29a19eebba3ca81a6718e7bb9fb344a702966433eb0e75446f0` |
| `evals/fixtures/source-conflict-status/workspace/context/org-dynamics.md` | `d454644515606c423d639243c49dffeb74adebfa7c2277677383878e283f9204` |
| `evals/fixtures/source-conflict-status/workspace/context/room/review.md` | `b7cc21966908dfb6614fb4a4c94c0ba5dfcbafb79fdd274ebc7059924b6b5954` |
| `evals/fixtures/source-conflict-status/workspace/sources/discussion.md` | `c6ee991ac1291472415d337fb8850bc13e1e1fe1187353533f11c349af5e3d41` |
| `evals/fixtures/source-conflict-status/workspace/sources/tracker.md` | `0b2e2b36f2939b80879bd9613226c851010eddbc458c62863434bd1133048d36` |
| `evals/fixtures/unavailable-source-recovery/README.md` | `f004b722ded183de8e87dffbbac7454757d619b013705f212a5923192e00bfe7` |
| `evals/fixtures/unavailable-source-recovery/appended-contradiction.md` | `da813a5de138c5e76d8b36f277a0d9d25973382380544213e62bdc73b4b12edd` |
| `evals/fixtures/unavailable-source-recovery/appendix-laundered.md` | `9791e8080ba41ab9881d54542e0d267ba15279a50be364f420ad45ddacdf1277` |
| `evals/fixtures/unavailable-source-recovery/contradictory-body.md` | `308e57bc30817cf84710ec51385d77cb1e60b338c84dd3d7c4e1caa85675e34f` |
| `evals/fixtures/unavailable-source-recovery/inline-heading-bypass.md` | `c3214dac0ec4954fcb532fdbfd456da2b35f5568f0c9d2276f37b6cb5ea19be5` |
| `evals/fixtures/unavailable-source-recovery/negative.md` | `2eef2583e078168a5c1e13a4e2146b0a0357250f57415dc1ab925f9fdd47184b` |
| `evals/fixtures/unavailable-source-recovery/positive.md` | `241d3db347954dd931fbb6e1120950d15e50428d86511cc0e9fb7c340c39a836` |
| `evals/fixtures/unavailable-source-recovery/workspace/cache/status/status-2026-10-27.md` | `1c79711b924e2f80785c3cfadd3825a37373f8c2098eb2c0c1d8f2827cdc0c95` |
| `evals/fixtures/unavailable-source-recovery/workspace/context/cadences.md` | `2c3f7c5b4bf698b887d0def87d0cfb4b018e0db6de56480549652c4743ca5ae1` |
| `evals/fixtures/unavailable-source-recovery/workspace/context/current-context.md` | `4ce69b88a1d6f4272e887d361e91437bb594e1062572c9c7cc106969d0270f41` |
| `evals/fixtures/unavailable-source-recovery/workspace/context/narrative-map.md` | `6a0203d875f0077e0dc083788af1e9a037402fdedfcc8503c24588ace6dc2140` |
| `evals/fixtures/unavailable-source-recovery/workspace/context/okr-status.md` | `9a6ebaf8b3bda29a19eebba3ca81a6718e7bb9fb344a702966433eb0e75446f0` |
| `evals/fixtures/unavailable-source-recovery/workspace/context/org-dynamics.md` | `d454644515606c423d639243c49dffeb74adebfa7c2277677383878e283f9204` |
| `evals/fixtures/unavailable-source-recovery/workspace/context/room/review.md` | `b7cc21966908dfb6614fb4a4c94c0ba5dfcbafb79fdd274ebc7059924b6b5954` |
| `evals/fixtures/unavailable-source-recovery/workspace/sources/inventory.md` | `f8d6f7863072d154001f694039183bf97d11196a0ce598b1daaf11db5b033595` |
| `evals/fixtures/unavailable-source-recovery/workspace/sources/metrics-stale.md` | `c0f0a5f8afae6bf899400335eae823e4a9b7f9d1c250cdf5b4b97aaf88025502` |
| `evals/fixtures/unavailable-source-recovery/workspace/sources/tracker.md` | `7ced4bbe9498e163b1a2a0ab85eccdda429bdb6d248bb3c0089061bb0da9b877` |
| `evals/source-lock.json` | `59f4b1395055392656cc9a93ba1a1bbb6a2cb42e5876dd6f1bc7733022d0964a` |
| `evals/tasks.json` | `ffaf20b2d4a84261fed6e6f88e492f44ad880e54594348ab65a437b0e90ba6f4` |
| `evals/tests/test_cases.py` | `1bef353df9046a32b9987cf09c2fa50db17728fc851a8de9ebc46e6e3aea4185` |
| `evals/tests/test_engine.py` | `f2e4e3c37371b9947c610bb1ab05e681d651125000bf8f55b303893fe368b7ea` |
