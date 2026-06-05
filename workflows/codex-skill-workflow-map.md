---
title: Codex Skill 与工作流地图
created: 2026-06-05
updated: 2026-06-05
tags:
  - codex
  - skills
  - workflow
  - obsidian
---

# Codex Skill 与工作流地图

这页是 Michael Song 的 Codex 工作能力索引：记录常用 skill、来源标注、合并关系、以及日常高频工作流。

仓库收录规则：

- `skills/`：自己开发/本地定制的 active canonical skills。
- `downloaded-skills/`：下载/本地安装且经常使用的 helper skills。
- 插件/系统内置 skill 不收录；旧版本 skill 不收录。

## 来源标注规则

| 标注 | 含义 | 判断依据 |
|---|---|---|
| 自己开发/本地定制 | 为你的项目、审美、写作、知识库或重复工作专门创建、强化或合并过的 skill。 | 描述里出现 Michael Song、你的具体项目，或本轮/此前明确基于你的工作流创建。 |
| 下载/本地安装 | 安装在本地 skill 目录里的通用能力，能直接用，但暂时没有明确证据说明是你自己开发。 | 位于 `~/.codex/skills` 或 `~/.agents/skills`，描述偏通用。 |
| 插件/系统内置 | Codex 系统、官方插件或第三方插件缓存提供的 skill。 | 位于 `.system` 或 `.codex/plugins/cache/...`，例如 Browser、GitHub、Vercel、Figma、Documents。 |
| 已合并但不收录 | 旧 skill、重复副本或已被合并进 canonical skill 的版本。 | 不放入本仓库；只保留 canonical skill。 |

> 注：这里的“自己开发”按当前电脑证据做保守标注，不等于法律意义的作者归属。通用 skill 如果你确认也是自己写的，可以把来源改成“自己开发/本地定制”。

## 高频核心 Skill

| Skill | 来源 | 主要用途 | 现在的 canonical 用法 |
|---|---|---|---|
| `mvp-product-shipping-loop` | 自己开发/本地定制 | 把产品想法、vibe-coding prompt、本地 app/MVP 请求变成可运行实现，并完成测试、浏览器验收、交付说明。 | 替代 `prompt-to-mvp-builder` 的执行部分；从 prompt 提取 MVP 要求也在这里做。 |
| `us-college-application-consultant` | 自己开发/本地定制 | 美本申请顾问产品：规划 Agent、知识库/RAG、报告导出、后台埋点、权限、Excel 下载。 | 替代 `us-college-planning-agent` 和 `us-college-analytics-dashboard`。 |
| `knowledge-doc-builder` | 自己开发/本地定制 | 知识库、Markdown、Word/docx、CSV/JSON 索引、审计、教育数据、食谱/营养数据。 | 替代 `recipe-nutrition-data-builder`，作为所有知识库/数据文档生产入口。 |
| `ui-ux-pro-max` | 自己开发/本地定制 | UI/UX 设计、重构、审美方向、响应式、可访问性、组件、图表、前端视觉打磨。 | 替代 `frontend-design`，通用 UI 审美入口。 |
| `design-master-skill` | 自己开发/本地定制 | 美本/招生产品专属视觉规则：顾问平台、学生 dashboard、学校选择、家长报告、数据对比页。 | 与 `ui-ux-pro-max` 搭配：通用 UI 用 Pro Max，招生产品审美再加载 design-master。 |
| `product-invent-skill` | 自己开发/本地定制 | 发明、验证、范围定义、计划、设计、构建、测试、部署产品或 MVP。 | 产品从 0 到 1 的上游入口。 |
| `vibe-coding-prompt-generator` | 自己开发/本地定制 | 把粗糙产品想法整理成高质量 Codex-ready prompt。 | 只保留 prompt 生成能力；执行交给 `mvp-product-shipping-loop`。 |
| `local-webapp-run-deploy` | 自己开发/本地定制 | 本地 web app 运行、重启、打包、部署、GitHub 发布、localhost 问题排查。 | MVP 做完后的运行/部署/交付入口。 |
| `ai-entertainment-app-builder` | 自己开发/本地定制 | 偶像匹配、人格测试、塔罗/占卜式体验、quiz、结果卡、轻量分享 app。 | 娱乐/测试类产品专用入口。 |
| `xhs-image-intel` | 自己开发/本地定制 | 小红书/XHS/RedNote 公开或授权内容采集、图片信息抽取、内容情报、CSV/JSON/Excel 数据集。 | 内容研究、招生案例收集、市场笔记整理入口。 |
| `xianxia-longform-writer` | 自己开发/本地定制 | 中文长篇网文/仙侠/修真/《逆命天炉》续写、章节审计、节奏、伏笔、连续性。 | 替代旧 `writer-skill`。 |
| `resume-rewriter` | 自己开发/本地定制 | 简历/CV 改写、JD 匹配、ATS、STAR/XYZ、真实性控制、Word 输出。 | 简历与招聘产品相关任务入口。 |
| `cinematic-video-workflow` | 自己开发/本地定制 | 从想法到剧本、角色几何、场景几何、Vidu 视频生成的短片工作流。 | 视频创作总调度。 |
| `screenplay-writer` | 自己开发/本地定制 | 中文剧本、短剧、广告片、镜头、分场、对白、节奏优化。 | 纯剧本写作入口。 |
| `competitor-analysis` | 下载/本地安装（待确认） | 产品、公司、SaaS、AI 产品、市场定位、定价、差异化分析。 | 产品验证和竞品研究入口。 |
| `define-goal` | 下载/本地安装（待确认） | 把模糊目标变成具体、可衡量的目标和成功标准。 | 大任务开始前用。 |
| `mcp-builder` | 下载/本地安装（待确认） | 构建 MCP server，连接外部 API/服务。 | Agent/工具集成开发入口。 |
| `chatgpt-apps` | 下载/本地安装（待确认） | ChatGPT Apps SDK：MCP server + widget UI + Apps bridge。 | ChatGPT App 项目入口。 |
| `web-crawler` | 下载/本地安装（待确认） | 合规爬虫、结构识别、列表/详情页抽取、CSV/Excel/JSON 导出。 | 网页数据采集入口。 |
| `playwright` / `playwright-interactive` | 下载/本地安装 | 真实浏览器自动化、表单、截图、UI flow debugging。 | 本地网页验收、bug 复现、视觉检查入口。 |
| `pdf` | 下载/本地安装 | PDF 阅读、生成、渲染、布局检查。 | PDF 相关文档入口。 |
| `openai-docs` | 下载/本地安装 / 系统也有 | OpenAI API、Codex、模型、官方文档查证。 | 问 OpenAI 产品和 API 时优先用。 |

## 下载/本地安装的辅助 Skill

| Skill | 来源 | 用途 |
|---|---|---|
| `figma-use` | 下载/本地安装 | 调用 Figma 工具前的必需前置 skill。 |
| `figma-generate-design` | 下载/本地安装 | 把页面、代码、描述转成 Figma screen/view。 |
| `figma-create-new-file` | 下载/本地安装 | 创建新的 Figma/FigJam 文件。 |
| `gh-address-comments` | 下载/本地安装 | 处理 GitHub PR review/issue comments。 |
| `gh-fix-ci` | 下载/本地安装 | 调试 GitHub Actions CI 失败。 |
| `yeet` | 下载/本地安装 | 明确要求时：stage、commit、push、开 PR。 |
| `notion-research-documentation` | 下载/本地安装 | 从 Notion 汇总研究、生成文档。 |
| `notion-spec-to-implementation` | 下载/本地安装 | 把 Notion PRD/spec 转成实现计划和任务。 |
| `linear` | 下载/本地安装 | 管理 Linear issues/projects。 |
| `security-best-practices` | 下载/本地安装 | Python/JS/TS/Go 安全最佳实践审查。 |
| `security-threat-model` | 下载/本地安装 | 代码库威胁建模、资产/边界/攻击路径/缓解。 |
| `sentry` | 下载/本地安装 | 查询 Sentry issues/events。 |
| `screenshot` | 下载/本地安装 | OS 层截图。 |
| `speech` | 下载/本地安装 | OpenAI Audio API 文本转语音。 |
| `transcribe` | 下载/本地安装 | 音频/视频转录，可选说话人标注。 |
| `together-video` | 下载/本地安装 | Together AI 文生视频/图生视频。 |
| `vidu-skills` | 下载/本地安装 | Vidu API/CLI：文生图、文生视频、图生视频、TTS、lip-sync、任务查询。 |
| `product-studio-orchestrator` | 下载/本地安装 / 本地 agent skill | 多 agent、并行 agent、产品工作室式协作。 |

## 插件/系统内置 Skill

| Skill / 插件 | 来源 | 用途 |
|---|---|---|
| `skill-creator` | 系统内置 | 创建、更新、验证 Codex skills。 |
| `skill-installer` | 系统内置 | 安装 Codex skills。 |
| `plugin-creator` | 系统内置 | 创建 Codex plugin。 |
| `imagegen` | 系统内置 | AI 生成/编辑图片。 |
| `browser:control-in-app-browser` | Browser 插件 | 打开、点击、输入、截图、验收 localhost/file 页面。 |
| `documents:documents` | Documents 插件 | Word/docx/Google Docs 风格文档创建、编辑、批注。 |
| `spreadsheets:Spreadsheets` | Spreadsheets 插件 | 表格、Excel、CSV、分析、可视化。 |
| `presentations:Presentations` | Presentations 插件 | PPTX/slide deck 创建、渲染、导出。 |
| `figma:*` | Figma 插件 | Figma 文件、设计系统、Code Connect、图表、Slides/FigJam。 |
| `github:*` | GitHub 插件 | GitHub repo/PR/issue/CI/发布工作流。 |
| `notion:*` | Notion 插件 | Notion 研究、文档、会议、知识沉淀、spec 到实现。 |
| `hyperframes:*` | HyperFrames 插件 | HTML 动画、视频合成、GSAP、字幕、voiceover、website-to-video。 |
| `vercel:*` | Vercel 插件 | Next.js、部署、验证、AI SDK、shadcn、env、存储、认证、observability、workflow。 |
| `superpowers:*` | Superpowers 插件 | TDD、系统调试、写计划、验证完成、subagent、技能写作、代码审查。 |

## 已合并但不收录的 Skill

| 旧 skill | 状态 | 新入口 |
|---|---|---|
| `prompt-to-mvp-builder` | 已合并，不收录旧版本 | `mvp-product-shipping-loop` |
| `us-college-planning-agent` | 已合并，不收录旧版本 | `us-college-application-consultant` |
| `us-college-analytics-dashboard` | 已合并，不收录旧版本 | `us-college-application-consultant` |
| `recipe-nutrition-data-builder` | 已合并，不收录旧版本 | `knowledge-doc-builder` |
| `frontend-design` | 已合并，不收录旧版本 | `ui-ux-pro-max` |
| `writer-skill` | Desktop 旧副本不收录 | `xianxia-longform-writer` |
| `resume-writer-master` | Desktop 旧副本不收录 | `resume-rewriter` |

## 高频工作流

### 1. 产品想法 -> MVP -> 浏览器验收 -> 交付

推荐顺序：

1. `define-goal`：把模糊想法变成目标、用户、成功标准。
2. `product-invent-skill`：发明/验证产品方向，确定范围。
3. `vibe-coding-prompt-generator`：需要时生成高质量 Codex build prompt。
4. `mvp-product-shipping-loop`：提取 MVP 要求、实现、测试、浏览器验收。
5. `ui-ux-pro-max`：界面、交互、响应式、视觉质感。
6. `local-webapp-run-deploy`：启动、打包、部署、交付 URL。
7. `playwright` 或 Browser 插件：桌面/移动端真实浏览器检查。
8. `yeet` / GitHub / Vercel：明确要求时提交、PR、部署。

常用触发语：

- “用 `mvp-product-shipping-loop` 把这个 prompt 做成能跑的 MVP。”
- “先帮我提取这个产品的 MVP contract，再实现并浏览器验收。”
- “这个 localhost 打不开/重启后跑不起来，用 `local-webapp-run-deploy` 查一下。”

### 2. 美本申请顾问产品迭代

推荐顺序：

1. `us-college-application-consultant`：判断属于规划 Agent、RAG、导出、后台、埋点还是权限。
2. `design-master-skill`：招生/教育产品专属审美、布局、家长端可信表达。
3. `knowledge-doc-builder`：整理大学、专业、活动、案例、课程、要求等知识库。
4. `documents:documents` / `spreadsheets:Spreadsheets`：Word 报告、Excel/CSV 数据。
5. `ui-ux-pro-max`：复杂 dashboard、表格、报告页、移动端体验。
6. `playwright` 或 Browser 插件：完整流程验收。
7. GitHub/Vercel skills：CI、部署、线上检查。

常用触发语：

- “用 `us-college-application-consultant` 改这个美本顾问产品。”
- “这个页面是招生产品，用 `design-master-skill` 的审美规则重做。”
- “把这些学校/案例整理成可导出的知识库，用 `knowledge-doc-builder`。”

### 3. 知识库/文档/数据集生产

推荐顺序：

1. `knowledge-doc-builder`：确定 schema、来源、索引、审计、输出格式。
2. `documents:documents`：需要 Word/docx 时使用。
3. `spreadsheets:Spreadsheets`：需要 Excel/CSV 表格、统计、清洗时使用。
4. `pdf`：涉及 PDF 提取、渲染、版式检查时使用。
5. `web-crawler`：从公开网页合规采集数据。
6. `xhs-image-intel`：从小红书图片/笔记抽取信息。

常用触发语：

- “把这些资料做成知识库文档，带索引和审计。”
- “把这个数据集清洗成 Markdown + Word + CSV/JSON。”
- “这是食谱/营养数据，用 `knowledge-doc-builder` 的 food/nutrition 子流程。”

### 4. UI/UX 设计与重构

推荐顺序：

1. `ui-ux-pro-max`：通用 UI/UX、视觉方向、交互、响应式、可访问性。
2. `design-master-skill`：招生/教育/顾问产品专属风格。
3. Browser 插件或 `playwright`：截图、交互、移动端检查。
4. Figma skills：需要转成 Figma 设计时使用。

常用触发语：

- “用 `ui-ux-pro-max` 把这个页面做得更专业、更有记忆点。”
- “这个 dashboard 信息太散，按工作型产品重排。”
- “这个是美本产品，结合 `design-master-skill` 和 `ui-ux-pro-max`。”

### 5. 内容、小说、剧本、视频

推荐顺序：

1. `xianxia-longform-writer`：仙侠长篇、章节续写、连续性、节奏、伏笔。
2. `screenplay-writer`：中文剧本、短剧、广告片、镜头、对白。
3. `cinematic-video-workflow`：从想法到剧本/角色/场景/视频生成。
4. `vidu-skills` 或 `together-video`：生成图片/视频。
5. `speech` / `transcribe`：配音、转录、音频辅助。

常用触发语：

- “用 `xianxia-longform-writer` 续写下一章，注意伏笔和连续性。”
- “把这个故事改成短片剧本，再走 `cinematic-video-workflow`。”
- “用 Vidu 生成这个镜头的视频。”

### 6. 小红书/内容情报/市场研究

推荐顺序：

1. `xhs-image-intel`：XHS 笔记、图片、评论、链接、导出结果抽取。
2. `competitor-analysis`：竞品、定位、差异化、价格、市场格局。
3. `web-crawler`：公开网页采集。
4. `knowledge-doc-builder`：整理成结构化报告、CSV/JSON、审计。

常用触发语：

- “用 `xhs-image-intel` 把这些小红书笔记整理成表格。”
- “分析这些竞品的定位、定价、差异化。”
- “把采集结果做成可复用知识库。”

### 7. 简历/申请材料/求职产品

推荐顺序：

1. `resume-rewriter`：简历改写、JD 匹配、ATS、真实性控制。
2. `documents:documents`：Word 简历输出、批注、格式。
3. `knowledge-doc-builder`：招聘/候选人/岗位数据整理。
4. `mvp-product-shipping-loop`：招聘助手、简历 polishing app 的 MVP 实现。

常用触发语：

- “用 `resume-rewriter` 按这个 JD 改我的简历。”
- “输出 Word 版，保留真实性和证据约束。”

### 8. Agent/MCP/ChatGPT Apps/工具集成

推荐顺序：

1. `openai-docs`：OpenAI API、Codex、模型、Apps SDK 官方文档。
2. `mcp-builder`：构建 MCP server。
3. `chatgpt-apps`：ChatGPT Apps SDK 项目。
4. `product-studio-orchestrator`：明确需要多 agent/并行 agent 时使用。
5. `security-best-practices` / `security-threat-model`：涉及权限、密钥、外部服务时做安全检查。

常用触发语：

- “我要做一个 MCP server，先用 `mcp-builder` 设计工具。”
- “这是 ChatGPT App，按 `chatgpt-apps` 和官方 docs 做。”
- “这个集成涉及密钥/权限，做一次 threat model。”

### 9. GitHub、CI、部署、线上排查

推荐顺序：

1. `gh-fix-ci`：GitHub Actions 失败。
2. `gh-address-comments`：PR review comments。
3. `yeet`：明确要 stage/commit/push/PR 一条龙时。
4. Vercel skills：Next.js、部署、日志、env、storage、AI SDK、verification。
5. `sentry`：线上错误事件。
6. `security-best-practices`：发布前安全检查。

常用触发语：

- “用 `gh-fix-ci` 看这个 PR 的 CI 为什么挂了。”
- “处理这个 PR 的 review comments。”
- “帮我 yeet：提交、push、开 PR。”

## 下一步维护规则

- 新建 skill 后，把它加到本页“高频核心 Skill”或“辅助 Skill”。
- 合并 skill 后，把旧 skill 移到“已合并或归档”。
- 每月检查一次 `~\.codex\skills`，删除或归档重复触发的旧版本。
- 能合并但不降能力的优先合并；领域专属审美/项目规则不要轻易合并掉。
- 每个 canonical skill 都应该有：
  - `SKILL.md`
  - `agents/openai.yaml`
  - 清晰的 description 触发词
  - 明确的工作流和验收标准
