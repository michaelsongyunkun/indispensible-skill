# JD Tailoring Guide

Use this reference when the user provides a JD, target role, or target company.

## JD Parse

Extract six dimensions before rewriting:

| Dimension | What to extract |
|---|---|
| Core responsibilities | 3-5 things the hire will actually do |
| Hard requirements | degree, years, tools, language, domain, work authorization |
| Preferred skills | plus factors that can differentiate the candidate |
| Implicit expectations | ownership, ambiguity, data fluency, cross-functional work, customer sense |
| ATS keywords | tools, methods, domain nouns, certifications |
| Business context | B2B/B2C, growth/mature stage, product type, team interface |

If the JD is vague, infer cautiously and label the inference.

## Evidence Matrix

Create a matrix before rewriting:

| JD requirement | Resume evidence | Strength | Rewrite action |
|---|---|---|---|
| exact JD phrase | source quote or "no evidence" | met / weak / stretch / missing | keep / strengthen / move up / ask / remove |

Definitions:

- `met`: direct evidence exists.
- `weak`: related evidence exists but lacks scope, result, or tool.
- `stretch`: transferable evidence from another context.
- `missing`: no evidence in the resume.

## Prioritization

The first third of the resume should answer: "why this candidate for this role?"

Order content by:

1. Hard requirement coverage.
2. Strongest role-specific proof.
3. Recency.
4. Brand/company signal.
5. General polish.

Do not bury the best JD-matching evidence under education, generic skills, or unrelated projects.

## Keyword Insertion

Use ATS keywords only when they are supported by evidence. Natural insertion beats density.

Good:

`使用 SQL 拆分转化漏斗，定位新用户激活率下降的主要节点。`

Bad:

`熟悉 SQL、数据分析、用户增长、A/B 测试、生命周期、策略运营。`

If a required keyword is missing but plausible, ask a confirmation question:

`JD 要求 A/B testing。简历没有相关证据；你是否做过实验分组、指标口径或效果复盘？`

## Tailoring Moves

Use these moves in order:

1. Rewrite the summary/intent to match the role honestly.
2. Move the most relevant experience up.
3. Rewrite achievement labels to mirror the role's competency language.
4. Replace generic skills with evidence-backed skills.
5. Compress unrelated content.
6. Add confirmation questions for missing but likely facts.

## Output

For user-facing JD tailoring, include:

```markdown
## JD 匹配结论
| JD 要求 | 现有证据 | 判定 | 修改动作 |

## 改写预览
| 模块 | 原文 | 改写后 | 原因 | 风险 |

## 待确认信息
- [ ] ...
```

When editing a file after approval or when the user explicitly asks for direct edits, preserve a short change log.
