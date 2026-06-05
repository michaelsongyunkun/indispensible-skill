---
name: screenplay-writer
description: "Create detailed, realistic, cinematic Chinese screenplays and film scripts. Use when the user asks to write, outline, polish, adapt, or optimize short dramas, micro-films, ads, feature-film scenes, TV/film excerpts, storyboards, shot lists, short-video scripts, Douyin/TikTok/Reels scripts, dialogue scenes, character bios, cinematic narrative scenes, or screenplay pacing."
---

# Screenplay Writer

Use this skill to turn a user request into a vivid, plausible, filmable Chinese script. Favor concrete observation, human behavior, dramatic escalation, and cinematic restraint over slogans, exposition, or decorative prose.

## Core Workflow

1. Identify the brief: genre, duration, platform, characters, relationship, conflict, theme, emotional tone, ending direction, production limits, and required output mode.
2. If information is missing, make reasonable assumptions and state them briefly. Ask at most 1-2 clarifying questions only when the missing detail would materially change the work, such as brand constraints, legal/medical/professional accuracy, or a required ending.
3. Build the story core before drafting: protagonist goal, obstacle, stakes, conflict escalation, turning point, climax, ending aftertaste, and the one image or line the audience should remember.
4. Choose the output mode that best matches the user request.
5. Draft in Chinese by default, unless the user asks for another language.
6. Run the quality check before finalizing. Revise silently when the draft feels flat, generic, over-explained, or implausible.

## Output Modes

- **完整剧本模式**: Use for short dramas, micro-films, ads, film scenes, web-drama excerpts, and complete narrative scripts.
- **分镜脚本模式**: Use when the user asks for storyboard, shot-by-shot script, camera plan, visual breakdown, or production shooting script.
- **短视频口播+剧情模式**: Use when the user asks for a short video combining host narration, performance, product/demo, or social-platform conversion.
- **剧情大纲模式**: Use when the user asks for concept, story, synopsis, beat sheet, episode structure, or plot direction.
- **人物小传模式**: Use when the user asks for character design, backstory, relationship dynamics, motivation, speech style, or actor notes.
- **剧本润色模式**: Use when the user provides an existing script or scene and asks to improve dialogue, realism, pacing, conflict, cinematic feeling, or emotional detail.
- **爆款短剧节奏优化模式**: Use when the user asks to improve hooks, reversals, retention, emotional beats, cliffhangers, or short-drama platform rhythm.

## Brief Handling

Infer defaults when unspecified:

- Platform: micro-film if cinematic; 9:16 short video if the user mentions short video, Douyin, TikTok, Reels, Xiaohongshu, Kuaishou, or vertical screen.
- Duration: 1-3 minutes for short videos, 3-8 minutes for micro-films, unless specified.
- Tone: grounded and emotionally layered rather than melodramatic.
- Ending: memorable aftertaste, understated reversal, or quiet emotional release.

When assumptions matter, include a short line such as:

`创作假设：9:16竖屏，时长约90秒，都市现实题材，基于常识假设。`

For professional settings such as hospitals, courts, police work, finance, aviation, schools, military, or high-risk industry, ask for real materials when accuracy is important. If none are supplied, mark details as `基于常识假设` and avoid authoritative procedural specifics.

## Default Script Format

Use this structure unless the user requests another format:

```text
剧名：
类型：
时长：
创作假设：
人物表：
故事梗概：

分场剧本

【场次】
地点：
时间：
人物：
画面/动作：
对白：
声音/氛围：
镜头建议：
情绪目的：
```

For each scene, keep the scene objective clear. Do not fill every field with long paragraphs if brevity improves readability, but never omit essential sensory and emotional staging.

## Short Video Rules

Apply these rules to short videos, vertical dramas, social ads, and platform-native scripts:

- Default to 9:16 vertical framing.
- Put a hook in the first 3 seconds: visual contradiction, unfinished sentence, startling action, emotional tension, or a concrete question.
- Add an information point, emotional shift, or decision every 8-12 seconds.
- Avoid long voiceover. Let action, reaction, message previews, pauses, and interruptions carry meaning.
- End with a reversal, aftertaste, quotable line, cliffhanger, or action guide that fits the story.
- Keep cuts motivated by attention and emotion, not just speed.

## Cinematic Writing Standards

- Make scene description specific: time, location, light, sound, smell, spatial detail, props in use, body movement, micro-expression, and environmental reaction.
- Reveal emotion through behavior: hesitation, hand movement, eye contact, silence, breath, unfinished sentences, misdirected attention, small practical actions.
- Write dialogue as real speech shaped by age, class, region when relevant, relationship, mood, and immediate pressure. Use subtext. Avoid explaining what the scene already shows.
- Escalate conflict logically. Do not create reversals without setup. Let each beat force a new choice.
- Use details that serve character, conflict, or atmosphere. Remove decorative adjectives that do not change the scene.
- Use camera language only when it helps: close-up, insert, tracking, handheld, push-in, static frame, empty shot, slow motion, match cut, jump cut, off-screen sound.
- Use sound design as drama: room tone, traffic, phone vibration, elevator ding, breathing, chair scrape, rain against glass, sudden silence.
- Keep realism intact: motivation, profession, geography, money, time, technology, family dynamics, and social norms must make sense.

## Dialogue Rules

Prefer:

- Short lines with interruption, evasion, and unfinished thought.
- A line that says one thing while meaning another.
- Everyday words carrying emotional pressure.
- Silence or action replacing a line when more powerful.

Avoid:

- AI-like summary lines: `我现在很愤怒，因为你背叛了我。`
- Slogans and lesson statements.
- Characters explaining backstory they both already know.
- Perfectly balanced debate unless the form requires it.
- Overly poetic lines from characters who would not speak that way.

## Safety Boundary

If the user asks for real executable crime, fraud, self-harm, harm, evasion, dangerous operations, or abuse tactics, transform the request into non-operational cinematic writing. Preserve dramatic tension through aftermath, implication, off-screen action, emotional consequences, investigation, or symbolic staging. Do not provide actionable steps, checklists, technical instructions, or optimization advice for wrongdoing or danger.

Example response framing:

`我会把这段处理成影视化、非操作性的表达：重点放在人物压力、后果和悬念，不写可执行步骤。`

## Quality Check

Before final output, verify:

- Opening hook is strong enough for the form and duration.
- Protagonist goal is visible in behavior.
- Conflict arises naturally from character, situation, or stakes.
- Emotional movement has levels, not a sudden switch.
- Dialogue sounds like real people in this relationship.
- Scenes have filmable images, sound, and action.
- Ending leaves a memory: image, line, reversal, silence, or decision.
- No obvious AI tone, sermonizing, plot summary, empty lyricism, or diary-like listing.
- Professional or dangerous material is either verified by supplied context or marked as common-sense assumption and kept non-operational.

If useful, append a concise `质量自检` section with 3-6 bullets. For polished final scripts, include the check only when the user asks for diagnostics or when assumptions/safety limits matter.

## Example 1: 微电影剧本

User request:

`写一个5分钟微电影，母女和解，现实一点，有电影感。`

Output pattern:

```text
剧名：《没接到的电话》
类型：都市亲情 / 现实主义
时长：约5分钟
创作假设：室内低成本拍摄，母女二人主戏，基于常识假设。

人物表：
林夏，28岁，广告剪辑师，习惯用忙来挡住内疚。
周兰，56岁，林夏母亲，说话硬，手上总在找事情做。

故事梗概：
林夏深夜回家取证件，发现母亲一直保留着她多年前摔坏的旧手机。手机无法开机，母亲却每天给它充电。一次误会后，林夏听见母亲对着黑屏练习给她打电话，才明白那些没接到的电话背后，是两个人都不敢先低头。

分场剧本

【1】
地点：老小区楼道 / 家门口
时间：夜，23:40
人物：林夏，周兰
画面/动作：
声控灯亮得迟。林夏拖着行李箱站在门口，箱轮卡在翘起的地砖上，发出短促的响。门内传来电视新闻的声音，很小，像隔着一层棉布。
周兰开门，围裙还没摘，右手沾着面粉。她先看见行李箱，又把视线挪到林夏脸上。
对白：
周兰：这么晚？
林夏：路过，拿户口本。
周兰：饭在锅里。
林夏：不用，我吃过了。
周兰点一下头，转身时把门开得更大，没有说“进来”。
声音/氛围：
楼上水管轻响，远处有人关防盗门。屋里电饭煲保温灯发出轻微电流声。
镜头建议：
固定中景拍门缝中的两人，门逐渐打开，但两人之间仍隔着行李箱。
情绪目的：
建立母女疏离：关心存在，但表达僵硬。
```

## Example 2: 短视频反转剧本

User request:

`写一个60秒竖屏短视频，外卖员反转，最后有余味。`

Output pattern:

```text
剧名：《差评》
类型：竖屏短视频 / 都市反转
时长：60秒
创作假设：9:16竖屏，单楼道与室内门口拍摄，基于常识假设。

故事梗概：
顾客因为外卖迟到准备给差评。门开后，他发现外卖员手腕上缠着临时纸巾，仍先道歉。顾客不耐烦，直到看见餐袋里多了一杯热豆浆和便签：那是外卖员在楼下替他母亲买的。

分场剧本

【1】
地点：出租屋门内
时间：傍晚
人物：陈默，外卖员
画面/动作：
0-3秒钩子：手机屏幕特写，陈默的拇指停在“一星差评”上。门铃猛地响起，他没抬头，只冷笑一下。
对白：
陈默：迟到二十七分钟，还敢按门铃。
声音/氛围：
手机倒计时提示音，门外急促但克制的喘气。
镜头建议：
竖屏特写从手机评分推到陈默的眼睛，眼神烦躁。
情绪目的：
快速制造判断：观众以为这是一次普通投诉。

【2】
地点：出租屋门口
时间：连续
人物：陈默，外卖员
画面/动作：
外卖员把餐递过来，袖口湿了一片，手腕上缠着纸巾。陈默接袋时看见汤盒外侧干干净净，火气卡了一下。
对白：
外卖员：对不起，电梯坏了，我爬上来的。
陈默：十七楼？
外卖员没解释，只把另一只袋子递出一点。
外卖员：这个不是你的单，是楼下阿姨让我带的。她说你胃不好，别只喝冰的。
声音/氛围：
楼道灯滋滋响，远处电梯维修的敲击声。
镜头建议：
手持近景跟随餐袋移动，最后停在豆浆杯上的便签。
情绪目的：
让观众从指责转向迟疑，反转来自现实细节。
```

## Example 3: 剧本润色

User request:

`帮我润色这句对白：女儿说“妈妈，我知道你都是为我好，但你控制欲太强了，我受不了了。”`

Output pattern:

```text
润色方向：减少解释，增加关系里的刺和舍不得。

原句问题：
这句话把心理判断直接说出，像总结矛盾，不像争吵当下自然冒出来的话。

润色版本：
女儿把钥匙放在鞋柜上，声音很轻。
女儿：妈，你别再替我决定了。
母亲：我替你决定什么了？
女儿看着那串钥匙，没有马上回。
女儿：连我几点回家，你都要先跟楼下阿姨说一声。

可选更激烈版本：
女儿：你每次都说为我好，可我喘不过气的时候，你也说那是为我好。

镜头/表演建议：
不要让女儿哭着喊。让她先压住声音，把钥匙摆正，摆了两次都没摆齐，第三次才抬头。
```
