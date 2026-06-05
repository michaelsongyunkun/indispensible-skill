---
name: competitor-analysis
description: Use when comparing products, companies, apps, SaaS tools, marketplaces, AI products, or business ideas against competitors; when the user asks for competitor research, market landscape mapping, positioning, differentiation, pricing comparison, product strategy, or an objective product evaluation with alternatives.
---

# Competitor Analysis

## Overview

Produce decision-grade competitive intelligence, not a generic list of similar companies. The output should help the user decide where to position, what to build, what to avoid, and which threats to monitor.

Default to the user's language. Use current public sources when the market, pricing, product features, funding, traffic, reviews, or leadership may have changed. If the user provides internal notes, customer feedback, pricing sheets, screenshots, or exports, treat those as primary context and clearly separate them from public research.

## When to Use

Use for:

- Competitor research, competitive landscape, market map, battlecard, SWOT, product comparison, pricing comparison, GTM analysis, differentiation strategy, product positioning.
- Evaluating a startup idea, AI product idea, SaaS product, app, education product, marketplace, content product, or local service against alternatives.
- Finding direct competitors, adjacent competitors, substitutes, emerging entrants, incumbents, and underserved niches.
- Objective product evaluation where the answer depends on what alternatives already do.

Do not use for:

- Pure user research with no competitor question.
- A single-company profile unless the user asks how that company compares to others.
- Market sizing only; include competitor analysis only if positioning or alternatives matter.

## Intake

Before researching, infer or ask for missing details only when they materially change the competitive set:

- Target: product, business, feature, idea, or company to analyze.
- Market boundary: category, geography, customer segment, price band, platform, language, B2B/B2C, regulated constraints.
- Decision: launch, pivot, pricing, roadmap, positioning, investment, acquisition, sales battlecard, content strategy.
- Depth: quick scan, strategic brief, or deep diligence.

If details are missing and a reasonable default is safe, state the assumption and proceed.

## Analysis Depth

| Mode | Use When | Competitors | Output |
| --- | --- | ---: | --- |
| Quick scan | User wants a fast answer or early idea check | 3-5 | Landscape, obvious gaps, recommendation |
| Strategic brief | Default mode for product/business decisions | 5-8 | Matrix, profiles, opportunity map, positioning |
| Deep diligence | High-stakes strategy, investment, launch, or pricing work | 8-12 | Segmented landscape, evidence register, risks, watchlist |

## Length and Detail

Respect the user's requested length first. If the user does not specify, use the shortest mode that can support the decision. For Chinese output, think in approximate characters; for English output, think in approximate words.

Default targets:

- Quick scan: 800-1,400 Chinese characters or 500-900 English words.
- Strategic brief: 1,800-3,500 Chinese characters or 1,200-2,200 English words.
- Deep diligence: 4,500-9,000 Chinese characters or 3,000-6,000 English words; offer a staged report if it would exceed the conversation's useful length.

Load `references/detail-controls.md` whenever the user asks for "详细", "精简", "long", "short", "deep", "brief", a word/character count, a report length, or when choosing between quick scan, strategic brief, and deep diligence.

## Optional References

Load only the reference files needed for the task:

- `references/source-quality.md`: Use when public/current claims, citations, reviews, pricing, funding, traction, or high-stakes decisions matter.
- `references/output-variants.md`: Use when the user needs a quick scan, strategic brief, deep diligence memo, pricing teardown, sales battlecard, investor brief, or roadmap input.
- `references/detail-controls.md`: Use when report length, word/character count, table/profile depth, or concise-vs-detailed output matters.
- `references/scoring-rubric.md`: Use when ranking competitors, assigning threat levels, scoring moats, prioritizing opportunities, or comparing products with a matrix.
- `references/research-query-patterns.md`: Use before web research or when the competitive set, pricing, reviews, traction, funding, docs, or customer sentiment must be discovered.
- `references/report-quality-check.md`: Use before final delivery for strategic briefs, deep diligence, pricing teardowns, investor memos, or any high-stakes recommendation.
- `references/ai-product-playbook.md`: Use for AI apps, agents, copilots, model wrappers, automation tools, AI SaaS, or AI features.
- `references/education-product-playbook.md`: Use for education, admissions, tutoring, counseling, student planning, parent-facing, or school-facing products.

## Workflow

1. Scope the market.
   Define the job-to-be-done, customer segment, geography, price band, and buying trigger. Avoid starting from brand names alone.

2. Build the competitive set.
   Classify competitors as:
   - Direct: same customer, same job, same buying moment.
   - Adjacent: overlaps on customer or job but not both.
   - Substitute: different product category but solves the same underlying job.
   - Incumbent: legacy/default behavior the user must displace.
   - Emerging: new entrant, open-source project, fast-growing community, or AI-native alternative.

3. Gather evidence.
   Prefer official sites, pricing pages, docs, changelogs, customer reviews, app store listings, case studies, job posts, funding/news, social proof, traffic/ranking sources, and user-provided materials. Cite sources when browsing or when precise claims matter.

4. Normalize the comparison.
   Compare competitors on the same dimensions. Use "unknown" instead of guessing when data is unavailable.

5. Score only where useful.
   Use 1-5 scores for relative comparison, not false precision. Explain what each score means. Load `references/scoring-rubric.md` for ranking, threat scoring, moat scoring, or opportunity prioritization.

6. Find strategic gaps.
   Identify underserved segments, weak workflows, pricing pain, integration gaps, trust gaps, poor UX, slow onboarding, weak localization, or distribution channels competitors ignore.

7. Recommend a wedge.
   End with a clear positioning recommendation, target segment, claims to emphasize, features to build, features to avoid, and threats to monitor.

## Evidence Labels

Use these labels for non-obvious claims:

| Label | Meaning |
| --- | --- |
| Confirmed | Directly supported by official/product/pricing/docs source |
| Observed | Visible in product UI, public demos, app pages, reviews, or screenshots |
| Reported | Claimed by third-party sources, customers, media, or analysts |
| Inferred | Reasoned from available signals; explain the inference |
| Unknown | Data not available or not verified |

Never invent funding, market share, revenue, user count, pricing, or traction. If a source is stale, say so with the date.

## Comparison Dimensions

Choose dimensions that fit the market. Common dimensions:

- ICP overlap: same buyer, user, budget owner, and urgency.
- Job-to-be-done coverage: how completely the product solves the target workflow.
- Product quality: usability, depth, reliability, speed, mobile/desktop experience.
- AI/data advantage: proprietary data, model quality, workflow automation, personalization, evaluation loop.
- Pricing pressure: price level, packaging clarity, free tier, switching cost, hidden costs.
- Distribution: SEO, community, partnerships, sales motion, marketplace, app store, integrations.
- Trust and compliance: brand, security, privacy, credentials, testimonials, outcomes.
- Momentum: launches, hiring, funding, reviews, community growth, content cadence.
- Moat: data, network effects, workflow lock-in, integrations, brand, regulatory advantage.

## Output Template

Use this default structure unless the user asks for a variant:

1. Executive take: market definition, strongest threat, best opportunity, recommended wedge, confidence level.
2. Landscape matrix: competitor, type, customer, core job, positioning, pricing, strength, weakness, threat level, evidence.
3. Competitor profiles: positioning, product, business model, strengths, weaknesses, threat to the user's target, evidence confidence.
4. Opportunity map: gap, why it exists, target segment, suggested move, risk.
5. Positioning recommendation: segment to prioritize, segment to avoid, differentiating claim, product wedge, GTM/pricing wedge, proof needed, 90-day moves, 12-18 month watchlist.

For quick scans, deep diligence, sales battlecards, pricing teardowns, roadmap input, or founder/investor memos, load `references/output-variants.md`.

## Common Mistakes

- Listing famous companies instead of true substitutes for the user's customer and job.
- Mixing direct, adjacent, and substitute competitors without labeling them.
- Treating feature checklists as strategy.
- Overstating "AI advantage" without data, workflow, or distribution proof.
- Inventing market share or customer counts.
- Ignoring pricing/package friction.
- Forgetting the incumbent behavior: spreadsheets, agencies, manual work, consultants, friends, forums, or doing nothing.
- Ending with observations but no recommended wedge.

## Final Self-Check

Before answering, verify:

- The competitive set matches the scoped customer and job-to-be-done.
- The output length matches the requested or inferred detail mode.
- Important claims have evidence labels or citations.
- Unknowns are explicit.
- Differentiation opportunities are specific enough to act on.
- The recommendation names what to build, what to avoid, and what to monitor.
- For strategic or high-stakes outputs, `references/report-quality-check.md` has been applied.
