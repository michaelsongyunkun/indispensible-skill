---
name: knowledge-doc-builder
description: Use when building, cleaning, verifying, indexing, or exporting structured knowledge-base documents for Michael Song: Markdown, Word docx, CSV, JSON, PDF, education/admissions datasets, university lists, Common App materials, journal catalogs, recipe/food/nutrition catalogs, idol/personality lists, audits, and scripts under knowledge-style folders.
---

# Knowledge Doc Builder

Use this skill for repeatable "raw material -> structured Markdown -> Word/docx + index/audit" work. Prefer preserving source evidence, naming conventions, and reproducible scripts over one-off prose generation.

## Core Workflow

1. Identify the deliverable: Markdown, Word `.docx`, CSV index, JSON audit, PDF, or a bundle.
2. Inventory existing assets before writing. Check for paired `.md`/`.docx`, `build_*.py`, `generate_*.py`, index CSV, and audit JSON files.
3. Define a compact schema before generating content. Include required fields, optional fields, source/evidence field, status, and uncertainty notes.
4. Keep the source of truth explicit. Do not invent schools, requirements, journals, recipes, nutrients, cases, prices, rankings, or eligibility rules without a source or a clear "needs verification" marker.
5. Generate Markdown first when the final output is a Word document. Keep headings, tables, and bullet structures stable so conversion can be repeated.
6. Build or reuse a script when the same operation is likely to recur: large document rendering, index generation, deduplication, audit checks, unit conversion, or docx export.
7. Produce an audit artifact when data quality matters: duplicate count, missing fields, unsupported claims, inconsistent units, stale dates, or source gaps.
8. Verify final files: open or render docx/PDF when tools are available, check file size, inspect the first/last sections, and confirm generated index/audit counts.

## Food And Nutrition Data Mode

Use this subflow for recipes, restaurant menus, ingredients, cooking-coach content, calorie estimates, nutrition tables, and food knowledge bases:

- Define schema first: recipe/menu name, cuisine, servings, ingredients, original units, normalized grams/ml, steps, prep/cook time, tags, allergens, calories, macro estimates, source, and verification status.
- Preserve original units while adding normalized units. Do not overwrite user-facing measurements with calculated grams only.
- Separate recipe generation from nutrition calculation. Keep generated cooking text, ingredient normalization, and calorie/macro estimation as distinct steps or script functions.
- Treat nutrition as an estimate unless backed by a cited database or provided source. Avoid medical, diet-treatment, or disease-specific claims.
- Audit for duplicate recipe names, missing ingredient amounts, impossible calories/macros, broken unit conversions, unsupported allergens, and inconsistent serving counts.
- Export in the format that supports reuse: Markdown/docx for reading, CSV/JSON for indexing, and audit JSON for cleanup.

## Local Asset Clues

Look first in Michael's knowledge/document folders and nearby outputs. Common reusable patterns include:

- `build_*.py` scripts for Word document generation.
- `generate_*.py` scripts for larger data libraries.
- Paired files such as `*_markdown.md` and `*_markdown.docx`.
- Index CSV files and audit JSON files.
- Education/admissions resources: university programs, Common App activity banks, journal catalogs, AP/IB/A-Level requirements, admission cases.
- Food resources: recipe catalogs, ingredient indexes, restaurant/menu libraries, nutrition estimates, calorie calculations, `ai-cooking-coach`, `generate_3000_recipes.py`, and `build_restaurant_500_markdown_docx.py`.

## Document Quality Rules

- Use concise section headings and predictable table columns.
- Separate factual data, interpretation, and recommendations.
- Keep bilingual or Chinese output consistent with the user's requested audience.
- For parent-facing admissions docs, use practical, calm language rather than sales copy.
- For large catalogs, include an index or search-friendly summary table.
- Do not hide uncertainty. Use `unknown`, `needs verification`, or `source missing` instead of filling gaps.

## Script Guidelines

When creating a script:

- Accept input/output paths as parameters instead of hardcoding a single file.
- Print counts and warnings at the end.
- Keep generated files outside the original source path unless the user asks to overwrite.
- Prefer structured parsing libraries for docx, CSV, JSON, Excel, and PDF.
- Add a dry-run or audit mode when the script changes or filters data.

## Verification Checklist

Before final response, report:

- Source files used.
- Output files created or updated.
- Row/item counts.
- Audit warnings and unresolved verification gaps.
- Conversion/render checks performed.
