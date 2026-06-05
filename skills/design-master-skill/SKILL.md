---
name: design-master-skill
description: "Use when designing, rebuilding, or restyling education/admissions product pages, school-selection tools, student dashboards, AI counseling portals, mentor marketplace flows, login/onboarding screens, or data-heavy comparison dashboards in the distilled visual languages of COR SeniorFriend and Capisa: warm decision-tool surfaces, compact utility cards, blue/orange/green state systems, Inter/Sans dashboard typography, rounded white panels, sticky actions, comparison tables, profile analysis cards, and pragmatic trust-building sections."
---

# Design Master Skill

## Purpose

Use this skill to recreate website design languages distilled from education/admissions products, currently COR SeniorFriend `https://corseniorfriend.com/compare` and Capisa `https://app.capisa.top/student-home`. It is best for serious but friendly product surfaces where students compare schools, manage admissions profiles, review AI analysis, or move through counseling workflows.

For fuller token inventories and page anatomy, read `references/design-notes.md`. Visual references are bundled in `assets/selection-desktop.png`, `assets/report-desktop.png`, `assets/selection-mobile.png`, `assets/capisa-signin-desktop.png`, and `assets/capisa-signin-mobile.png`.

## Design DNA

- Make the product feel like a calm decision tool, not a marketing landing page.
- Use a warm paper background with white work surfaces: page `#FFFDF7`, alternate band `#FAF8F2`, cards `#FFFFFF`, dividers `#EEEEEE`.
- Keep the palette functional: blue for navigation/selection, orange for primary action and rank filters, green for verification/winners, dark navy for headings.
- Prefer compact density over decorative spaciousness. The original page fits search, filters, selected schools, and many school cards into a utilitarian workspace.
- Use rounded UI, but keep it disciplined: 12px inputs/buttons, 14px action buttons, 16px cards/panels, 999px pills.
- Interaction should feel tactile: primary orange buttons use a small darker base shadow and move down on active press.
- For Capisa-like AI admissions dashboards, shift from warm paper to clean SaaS neutrals: `#F9FAFB` page, white rounded panels, royal blue primary actions, and pastel analysis modules.

## Page Structure

For a selection/comparison flow, use this sequence:

1. Sticky/header nav with compact logo, nav links, tool dropdown, auth actions, language chip.
2. Centered page title and subtitle.
3. Selected-item pill row or empty italic state.
4. Search input with icon, 2px border, 14px radius.
5. Two rows of pill filters: category filters in blue, rank/range filters in orange.
6. Dense item grid: one column on mobile, two columns from small tablet upward.
7. Sticky bottom action bar showing selected count and a primary action button.
8. Results view with back link, report title, optional mobile preference accordion, desktop left preference sidebar, score cards, comparison table, testimonials/mentor sections, feedback capture, trust footer.

## Core Tokens

Use these values unless the local codebase has established equivalents:

```css
:root {
  --cor-bg: #FFFDF7;
  --cor-band: #FAF8F2;
  --cor-card: #FFFFFF;
  --cor-ink: #1A1A2E;
  --cor-muted: #6B6B7B;
  --cor-faint: #9CA3AF;
  --cor-line: #EEEEEE;
  --cor-blue: #4A8FE7;
  --cor-blue-soft: #EEF4FD;
  --cor-blue-text: #3570B8;
  --cor-orange: #F5A623;
  --cor-orange-soft: #FFF3E0;
  --cor-orange-deep: #D4900A;
  --cor-green: #5BAD6F;
  --cor-green-soft: #EDF7F0;
  --cor-green-text: #3D8B52;
  --cor-footer: #141426;
}
```

Capisa-style tokens for AI counseling dashboards and login/onboarding:

```css
:root {
  --capisa-bg: #F9FAFB;
  --capisa-card: #FFFFFF;
  --capisa-ink: #111827;
  --capisa-muted: #4B5563;
  --capisa-faint: #9CA3AF;
  --capisa-line: #E5E7EB;
  --capisa-input-line: #D1D5DB;
  --capisa-blue: #2563EB;
  --capisa-blue-hover: #1D4ED8;
  --capisa-blue-soft: #EFF6FF;
  --capisa-blue-line: #BFDBFE;
  --capisa-green-soft: #F0FDF4;
  --capisa-purple-soft: #FAF5FF;
  --capisa-orange-soft: #FFF7ED;
  --capisa-yellow-soft: #FEFCE8;
  --capisa-pink-soft: #FDF2F8;
}
```

Typography:

- Font stack: `DM Sans`, `Noto Sans SC`, `PingFang SC`, sans-serif.
- Capisa stack: `Inter`, `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `Roboto`, sans-serif.
- Mobile page title can be large and bold; desktop tool titles stay compact.
- Typical sizes: title 22-26px desktop, 42-48px mobile hero-like tool title, body 13-15px, metadata 11-12px, table text 13px.
- Use weights 900 for page titles/logo emphasis, 700 for item names and key labels, 500-600 for filters and metadata.

## Components

Search input:

- White background, `2px solid #eee`, 14px radius, 14px text.
- Left search icon in muted gray; focus border blue or orange with a faint tinted ring.
- Placeholder should be concrete and task-specific.

Filter pills:

- Rounded full pills with `padding: 8px 18px`, `2px` border.
- Unselected: white, gray border, muted text.
- Selected category: blue border, `#EEF4FD`, blue text.
- Selected rank/action filter: orange border, `#FFF3E0`, deep orange text.

Selection cards:

- White card, 16px radius, `2px solid #eee`, 20px padding.
- Selected state: blue soft background and `2.5px solid #4A8FE7`.
- Hover: translate up 2px and subtle shadow `0 6px 16px rgba(0,0,0,0.06)`.
- Content hierarchy: bold Chinese name, italic English name, then icon metadata row with city, type, and ranking separated by thin text pipes.

Primary action:

- Orange fill, white text, 14px radius, 700 weight.
- Use `box-shadow: 0 4px 0 #D4900A` for large CTAs and `0 3px 0 #D4900A` for smaller embedded actions.
- Add active press behavior: translate down and remove shadow.
- Disabled action uses gray fill/text and gray base shadow.

Results table:

- Wrap table in a white 16px panel with `2px solid #eee`.
- Use horizontal scroll on narrow screens; keep the first column sticky.
- Header and section rows use the warm background.
- Alternate data rows white and `#FAFAF8`.
- Metric cells combine a numeric value, a slim 4px progress bar, and color-coded dimension accent.
- Highlight best values in green; low/neutral values stay muted or use the dimension color.

Preference sidebar:

- Desktop: 280px sticky left panel with white background, 16px radius, `2px solid #eee`, max height `calc(100vh - 6rem)`.
- Mobile/tablet: collapse the same controls into a rounded accordion above results.
- Each factor card is white, 12px radius, `1px solid #E5E5E5`, 16px padding; active factors get a blue left border.
- Use small dot importance controls and colored range tracks. Unset dimensions must not affect scores.

Trust/footer:

- Add a slim verification band above the footer using `#FAF8F2`, green shield/check icon, 12px muted text, and blue link.
- Footer is dark navy, compact, with muted white text and small columns.

## Capisa AI Dashboard Pattern

Use this pattern for AI admissions portals, profile dashboards, and login/onboarding screens.

Login page:

- Desktop is a two-panel composition: left side contains a centered logo above a max-width form card; right side is a large royal-blue brand panel with a white headline, short value copy, and a dashboard preview image/card.
- On mobile, hide the blue brand panel and stack a logo above a single form card with generous top whitespace.
- Login card: white, `2px solid #E5E7EB`, 24px radius, subtle `0 1px 2px rgba(0,0,0,0.05)` shadow, 24-32px padding.
- Inputs: 8px radius, `1px solid #D1D5DB`, 12px padding, 16px text, blue focus ring.
- Alert/help banner: `#EFF6FF` background, `#BFDBFE` border, 8px radius, blue text.
- Primary button: full-width `#2563EB`, white text, 8px radius, 12px vertical padding; hover to darker blue without tactile bottom shadow.

Student dashboard and AI analysis cards:

- Use a light gray app background with white `rounded-2xl shadow-xl` cards and 24-32px padding.
- Use section cards for profile areas: Basic Information, Academic Background, Test Scores, Extracurricular Activities, Professional Goals, Student Profile Analysis.
- Inside large cards, use pastel sub-panels: blue for academic/profile overview, green for strongest aspects, amber/yellow for improvement areas, purple for AP/IB or competitive advantages, orange for activities, pink for hobbies.
- Use grid layouts aggressively: `grid-cols-1 md:grid-cols-2` for form/profile fields, `md:grid-cols-4` for academic stat tiles, and `gap-4`/`gap-6`.
- Important numbers use 24px bold colored text inside small centered tiles.
- AI analysis modules should feel report-like: title row with an icon, italic explanatory line, radar/chart panel on gray-50, then stacked analysis blocks with colored headings.
- Empty states are centered white cards with a muted icon, short explanation, and a blue CTA such as `Start Questionnaire`.
- Edit actions are small icon buttons in the top-right of section headers; keep them visually quiet until hover.

## Responsive Rules

- Mobile first: one-column cards, large touch targets, visible hamburger, sticky bottom action bar.
- For Capisa-style auth pages, mobile should collapse to the form-only experience; remove decorative preview panels and maintain readable 16px inputs.
- Desktop: constrain selection pages to about 1000px and results pages to about 1400px.
- Use `padding-left/right: 24px` desktop, larger visual breathing room on mobile cards without making the layout sparse.
- Keep text from overflowing buttons and cards; allow metadata rows to wrap.
- Tables may scroll horizontally; do not squeeze columns until they become unreadable.

## Content Tone

- Chinese-first interface, with English school/program names as secondary metadata.
- Explain the user's decision context briefly; avoid long instruction blocks.
- Use pragmatic trust copy: verified identities, real student experience, refund/attendance assurances, and lightweight founder notes.
- Keep CTAs direct: "开始对比", "重新选校", "看看类似学校的学长", "留下微信", "登录", "注册", "Start Questionnaire".

## Avoid

- Do not turn this into a glossy landing page with oversized hero cards, decorative gradients, or stock imagery.
- Do not use purple-heavy gradients, beige-only palettes, floating nested cards, or ornamental blobs.
- Do not make every section a card. Reserve cards for selectable items, panels, tables, accordions, and forms.
- Do not over-enlarge desktop typography; the original design is a focused tool surface.
- Do not hide the main task behind explanatory copy.

