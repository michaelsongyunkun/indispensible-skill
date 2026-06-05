# COR SeniorFriend Compare Page Design Notes

Source inspected: `https://corseniorfriend.com/compare` on May 30, 2026.

## Observed Screens

- Selection desktop: centered 1000px tool surface on warm background; sticky nav; search; selected pills; two filter rows; dense two-column school card grid; sticky bottom action bar.
- Selection mobile: large logo/header, hamburger, centered title, large search input, large pill filters, single-column cards, persistent bottom action.
- Report desktop: 1400px max layout, sticky 280px preference sidebar, score cards, large comparison table, testimonial accordion, mentor recruitment links, feedback prompt, founder note form, trust footer.

Bundled visual references:

- `assets/selection-desktop.png`
- `assets/report-desktop.png`
- `assets/selection-mobile.png`
- `assets/capisa-signin-desktop.png`
- `assets/capisa-signin-mobile.png`

## Visual Tokens

| Role | Value |
| --- | --- |
| Page background | `#FFFDF7` |
| Alternate band | `#FAF8F2` |
| Cards/panels | `#FFFFFF` |
| Main text | `#1A1A2E` |
| Body muted | `#6B6B7B` |
| Faint text | `#9CA3AF` |
| Dividers | `#EEEEEE`, `#E5E5E5` |
| Blue | `#4A8FE7` |
| Blue soft | `#EEF4FD` |
| Blue text | `#3570B8` |
| Orange | `#F5A623` |
| Orange soft | `#FFF3E0` |
| Orange deep/shadow | `#D4900A` |
| Green | `#5BAD6F` |
| Green soft | `#EDF7F0` |
| Green text | `#3D8B52` |
| Footer | near `#141426` |

## Typography

- CSS imports `DM Sans`, `Plus Jakarta Sans`, and `Noto Sans SC`; base stack uses `DM Sans`, `Noto Sans SC`, `PingFang SC`, sans-serif.
- The interface relies on strong weights rather than large desktop type: 900 for titles, 700 for names/actions, 600 for filters/metadata.
- Desktop H1 observed at 26px/900; report title at 22px/900; score numbers at 32px/900.
- Mobile title is much larger and centered, with generous vertical rhythm.

## Layout Measurements

- Selection wrapper: max width 1000px, `padding-left/right: 24px`, top padding 80px mobile-ish and 128px desktop.
- Report wrapper: max width 1400px, same side padding.
- Report sidebar: 280px wide, sticky top 80px, max height `calc(100vh - 6rem)`.
- Card grid: `grid-cols-1 sm:grid-cols-2`, 12px gap.
- School cards: 20px padding, 16px radius, 2px border.
- Search input: 14px vertical padding, 48px left padding, 14px radius, 2px border.
- Filter pills: 8px by 18px, full radius, 2px border.
- Sticky bottom bar: white, top border, 16px by 24px padding.

## Interaction Patterns

- Card hover: translate up by 2px, add soft shadow.
- Primary CTA: orange with dark orange bottom shadow; active press removes shadow and translates down.
- Selection card active state switches to blue-soft background and 2.5px blue border.
- Inputs shift border and faint ring on focus.
- Mobile bottom CTA remains persistent; disabled state is gray with gray shadow.

## Component Inventory

- Compact nav with logo, links, "tools" dropdown, login/register, language chip.
- Search bar with icon and clear button.
- Selected-item removable chips.
- Category and ranking filter pills with separate active colors.
- School cards with Chinese title, italic English subtitle, icon metadata, active check circle.
- Preference factor cards with icon, range slider, dot importance scale, active left border.
- Score cards with best-match badge, large number, progress bar.
- Comparison table with sticky first column, section separators, alternating rows, mini bars.
- Testimonial accordion panel with blue selected border.
- Mentor cards with avatar circle, rating, orange chat CTA and blue outlined video CTA.
- Founder/wechat capture card.
- Verification strip and dark footer.

## Design Translation Heuristics

- Use this style when users need to compare many options quickly and feel confident about a choice.
- Preserve the "worksheet" feeling: most surfaces should be useful controls, tables, or data cards.
- Use color as state and category, not decoration.
- Keep copy short near controls; longer founder/trust copy belongs low on the page.

# Capisa Student Home / Sign-In Design Notes

Source inspected: `https://app.capisa.top/student-home` on May 30, 2026. The route redirects unauthenticated visitors to `/signin`; the visible page is the student sign-in shell. The frontend bundle also exposes student dashboard/profile component classes and labels, so dashboard notes below are derived from static bundle evidence rather than an authenticated screenshot.

## Observed Screens

- Desktop sign-in: very light gray page, two-column layout, centered Capisa logo above a white login card on the left, large royal-blue brand panel on the right, embedded dashboard-preview screenshot/card.
- Mobile sign-in: form-only experience, large vertical whitespace, logo centered above a single white rounded card; the blue preview panel is removed.
- Bundle-confirmed dashboard modules: `Student Profile Analysis`, `Academic Profile`, `Student Capabilities Radar`, `Profile Analysis`, `Strongest Aspects`, `Areas for Improvement`, `Development Recommendations`, `No Profile Data`, and `Start Questionnaire`.

## Capisa Visual Tokens

| Role | Value |
| --- | --- |
| Page background | `#F9FAFB` |
| Card background | `#FFFFFF` |
| Primary text | `#111827` |
| Secondary text | `#374151` / `#4B5563` |
| Muted text | `#6B7280` / `#9CA3AF` |
| Border | `#E5E7EB` |
| Input border | `#D1D5DB` |
| Primary blue | `#2563EB` |
| Primary hover | `#1D4ED8` |
| Info panel | `#EFF6FF` with `#BFDBFE` border |
| White overlay on blue panel | `rgba(255,255,255,0.05)` |

## Sign-In Layout Measurements

- Desktop form card: max width around 672px, padding 32px, `border: 2px solid #E5E7EB`, 24px radius.
- Form inputs: 50px height desktop, 12px padding, 8px radius, 1px gray border.
- Primary login button: 48px height desktop, full width, 8px radius.
- Right blue panel: tall rounded rectangle, about half the viewport width, 24px corner radius, centered headline and preview card.
- Mobile card: nearly full width with 32px page gutters, 24px radius, larger visual whitespace above the logo.

## Capisa Dashboard Components

- Shell style: neutral gray background, Inter typography, Tailwind utility feel, white `rounded-2xl shadow-xl` cards.
- Profile dashboard cards use `p-6` or `p-8`, `rounded-2xl`, and dense section headers with icons.
- Analysis tiles use pastel panels:
  - Blue for GPA/profile overview and development recommendations.
  - Green for standardized tests and strongest aspects.
  - Purple for AP/IB and competitive advantages.
  - Orange for extracurricular activities.
  - Yellow/amber for competitions, awards, and improvement areas.
  - Pink for hobbies and interests.
- AI report sections combine a title row, italic helper text, a pale blue overview callout, stat tiles, radar/chart card, and stacked colored analysis notes.
- Empty-state card: white `rounded-2xl shadow-xl`, centered icon, 20px title, muted explanatory paragraph, blue CTA.
- Edit controls: small icon-only buttons in section headers using muted gray, turning blue on hover.

## Capisa Translation Heuristics

- Use Capisa style when the product is closer to SaaS dashboard, AI analysis report, profile management, or login/onboarding.
- Use COR style when the product is closer to public-facing comparison, selection, mentor marketplace, or trust-led admissions utility.
- Do not mix both palettes on the same surface without a clear hierarchy. A page can use Capisa app shell plus COR-like comparison widgets, but the primary background and CTA style should come from one system.
