# Google Docs Formatting

## Standing Rule
**Always format headings when pushing content to Google Docs.** Never leave a doc as unformatted plain text. This is mandatory, not optional. {{YOUR_NAME}} has flagged this multiple times.

## Preferred Method: Import with Correct Heading Levels

Don't manually compute indices in existing docs. Tables create unpredictable index overhead and position estimates break. Instead:

1. **Prepare markdown with target heading levels.** In the local `.md` file, headings use `##` for H1, `###` for H2, `####` for H3. For Google Docs import, shift levels so the import produces the right styles:
   - `##` in local → `#` in import file (imports as H1)
   - `###` in local → `##` in import file (imports as H2)
   - `####` in local → `###` in import file (imports as H3)
   - Title line stays as `#` (imports as H1, change to Title after)
2. **Import using `import_to_google_doc`** with `source_format: md`. This preserves tables, bold, links, and lists automatically.
3. **Apply Title style** to the first paragraph only (index 1 to end of title text). This is the one operation that requires a known index, and index 1 is always safe.
4. **Copy into existing doc** if the URL must stay the same: select-all in imported doc, copy, select-all in old doc, paste. Heading styles carry over via copy-paste.

## Heading Hierarchy (PRDs)

Use Google Docs **named paragraph styles** (Title, Heading 1, Heading 2, Heading 3). Not manual font sizes.

| Style | Use for | Example |
|-------|---------|---------|
| Title | Doc title (one per doc) | "{{PRODUCT}} Ramps: Additional Assets & Ramps" |
| Heading 1 | Top-level sections | Background, Goal, User Stories, Resources, Stakeholders, Revenue Model, Open Questions |
| Heading 2 | Subsections / phases | Phase 1, Phase 2, Phase 3 |
| Heading 3 | Nested subsections | User Stories (under a phase), Design Considerations, Technical Considerations, Operational Considerations |
| Bold normal text | Table labels, metadata | "Measure of Success" (above a table), "Status: In Review" |

## Table Formatting
- Header row cells: **bold** normal text (not heading-styled)
- All header cells must be bold consistently. Don't leave some bolded and some not.

## Naming Conventions
- Use "Considerations" not "Suggestions" or "Cases" for subsection labels (Design Considerations, Technical Considerations, Operational Considerations).

## Common Pitfalls
- **Don't compute indices manually for existing docs with tables.** Table structure adds unpredictable overhead to character indices. Import fresh instead.
- Google Docs API indices are 1-based (index 1 = first character)
- `update_paragraph_style` applies to the ENTIRE paragraph overlapping the given range. If your range spans two paragraphs, both get styled.
- `get_doc_as_markdown` uses `#` for H1, `##` for H2, etc. It does NOT distinguish Title from H1 in the output.
- Batch operations have a limit; split into multiple calls if needed (20 ops per call works fine)
