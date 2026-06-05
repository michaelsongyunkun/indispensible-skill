---
name: xianxia-longform-writer
description: Write, continue, outline, revise, audit, and manage long-form Chinese web fiction for Michael Song, especially xianxia/cultivation fantasy, serialized chapters, chapter append/rewrite workflows, continuity ledgers, protagonist growth, antagonist depth, payoff cadence, pacing, psychological depth, and manuscript quality passes. Use when the user mentions xianxia, cultivation, 逆命天炉, chapters, serial arcs, or long novel continuation.
---

# Xianxia Longform Writer

This is the canonical installed version of Michael Song's local `writer-skill`, focused on long-form fiction and xianxia continuation. Prefer this skill over generic writing guidance when the request involves serialized chapters, cultivation systems, chapter audits, or manuscript continuity.

Use this skill to create fiction that reads like a lived story, not a summary of events. Favor character desire, pressure, concrete sensory detail, scene-by-scene causality, and prose rhythm over exposition, slogans, and generic drama.

## Core Workflow

1. Identify the brief: language, genre, length, audience, premise, protagonist, core conflict, setting, POV, tense, tone, ending direction, and whether the user wants outline, draft, continuation, rewrite, or critique.
2. If key information is missing, make reasonable assumptions and state them briefly. Ask at most 1-2 questions only when the answer would materially change the story, such as required genre, ending, target platform, taboo content, or continuity from prior chapters.
3. Choose the output mode and pass set. Run only the passes that match the request, unless the user asks for a full audit.
4. Build the narrative spine before writing: central story question, protagonist goal ladder, antagonist/faction pressure, causal chain, turning points, and what each subplot changes in the main line.
5. Build the scene engine before drafting prose: protagonist desire, wound or false belief, obstacle, stakes, pressure source, moral choice, escalation path, and the scene image or sentence the reader should remember.
6. For long-form xianxia/修仙 work, switch to Long-Form Xianxia Mode before outlining, drafting, or continuing.
7. Write in the user's language by default. For Chinese requests, use natural Chinese prose with varied sentence length, concrete verbs, and relationship-specific dialogue.
8. Run the quality check. Revise silently when the draft feels generic, over-explained, melodramatic, inconsistent, causally loose, overloaded with information, emotionally breathless, or too abstract.

## Output Modes

- **Novel premise**: Use when the user asks for an idea, concept, logline, selling point, or story seed.
- **Synopsis**: Use when the user asks for a full story summary, pitch, back-cover copy, or ending-inclusive plot.
- **Beat sheet**: Use when the user needs plot beats, turning points, acts, chapter roadmap, or serialized arc planning.
- **Storyline map**: Use when the user needs a clearer main story line, causal chain, act/volume structure, subplot discipline, chapter goals, or "what happens because of what" diagnosis.
- **Chapter pattern audit**: Use when several chapters feel mechanically similar, samey, too formulaic, too structurally repetitive, or locked into the same trap-reveal-counterpressure-hook loop.
- **Batch chapter audit**: Use when the user provides or describes multiple chapters and asks for arc-level diagnosis, repeated patterns, pacing fatigue, chapter functions, hook variety, relationship movement, or continuity issues.
- **Arc fatigue control**: Use when pressure stays too continuous, information density stays high, chapter patterns repeat, and private relationships do not have enough looseness or low-stakes texture.
- **Pacing and density pass**: Use when the user says the prose feels tiring, too dense, too high-pressure, symbol-heavy, clue-heavy, emotionally rushed, or when characters feel like evidence delivery devices.
- **Prose flow pass**: Use when supporting characters feel tool-like, emotional beats repeat, scene transitions feel abrupt, paragraphs do not connect, or prose needs smoother movement.
- **Psychological depth pass**: Use when prose lacks psychological description/心理描写, inner conflict, motive pressure, perception bias, hesitation, or readable aftereffects from important events.
- **Language clarity pass**: Use when prose feels obscure, hard to understand, too abstract, too mannered, concept-heavy, or when the user wants stronger story legibility without watery or low-quality prose.
- **Dramatic expansion pass**: Use when imagery is too dense, rule games dominate action, action variety feels thin, emotional restraint lacks a clear emotional peak, enemies feel too similar, or key chapters need more word count breath.
- **Growth and payoff pass**: Use when protagonist growth is too subtle, pressure is too continuous, textured setting blocks reader entry, antagonists have roles but weak face memory, or shuangdian/direct payoff feels too implied or indirect.
- **Character design**: Use when the user asks for protagonist, antagonist, supporting cast, motivation, backstory, relationships, speech style, or character arc.
- **Worldbuilding**: Use when the user asks for setting, magic system, social rules, factions, institutions, geography, history, technology, or constraints.
- **Chapter draft**: Use when the user asks to write an opening, chapter, scene, excerpt, or complete prose passage.
- **Continuation**: Use when the user provides existing text and asks to continue. Preserve POV, tense, timeline, character knowledge, emotional state, style, and unresolved hooks.
- **Revision**: Use when the user asks to polish, rewrite, deepen emotion, improve pacing, strengthen conflict, reduce AI tone, or make prose more literary/commercial.
- **Manuscript critique**: Use when the user asks whether a story works. Diagnose structure, character, tension, scene logic, prose, dialogue, and reader promise.
- **Story bible**: Use when the user needs continuity over many chapters: cast, timeline, factions, promises, secrets, items, injuries, powers, and unresolved hooks.
- **Long-form xianxia plan**: Use when the user asks for 修仙, 玄幻, cultivation fantasy, sect politics, realm progression, power systems, serialized arcs, or million-word planning.

## Brief Handling

Infer defaults when unspecified:

- Language: match the user's language; Chinese by default when the request is in Chinese.
- Length: 800-1500 Chinese characters for a single scene or opening unless the user specifies otherwise.
- POV: close third person for most fiction; first person when intimacy, voice, or unreliable narration matters.
- Tense: past tense for Chinese fiction unless the supplied text uses present tense.
- Ending: leave an emotional aftertaste, sharpened question, reversal, or concrete image instead of a moral lesson.
- Style: grounded, vivid, and character-driven unless the user asks for a specific genre tone.

When assumptions matter, include one short line:

```text
Assumptions: close third person, contemporary suspense, about 1200 Chinese characters, with a restrained ending.
```

Do not over-question early-stage ideas. If the user gives only a rough premise, produce a useful first version with stated assumptions.

## Pass Selection

Select a focused pass set before working. Do not run every pass by default; too many simultaneous constraints make prose cautious and over-edited.

| User need or symptom | Primary pass set | Load |
| --- | --- | --- |
| New premise, chapter, or continuation | Story Engine + Drafting Rules | Usually no extra reference unless genre-specific |
| Story feels scattered or hard to summarize | Storyline Clarity Pass | [storyline-clarity.md](references/storyline-clarity.md) |
| Several chapters feel formulaic or samey | Chapter Pattern Variety Pass | [chapter-pattern-variety.md](references/chapter-pattern-variety.md) |
| User provides 3+ chapters or asks for arc diagnosis | Batch Chapter Audit | [chapter-sequence-audit.md](references/chapter-sequence-audit.md) |
| Pressure is continuous, density is high, patterns repeat, and private relationships feel tight | Arc Fatigue Control Pass | [arc-fatigue-control.md](references/arc-fatigue-control.md) |
| Prose feels dense, tiring, or clue-heavy | Information Density Pass | [scene-balance.md](references/scene-balance.md) |
| Characters feel tool-like, emotions repeat, or transitions are rough | Prose Flow Pass | [prose-flow.md](references/prose-flow.md) |
| Prose lacks psychological description, inner conflict, motive pressure, perception bias, or aftereffect | Psychological Depth Pass | [psychological-depth.md](references/psychological-depth.md) |
| Language feels obscure, hard to understand, too abstract, or too ornate | Language Clarity Pass | [language-clarity.md](references/language-clarity.md) |
| Protagonist growth is hard to see, setting texture blocks reader entry, chapters carry too many core points, pressure rarely releases, antagonists lack face memory, or shuangdian/payoff feels indirect | Growth Payoff Pass | [growth-payoff.md](references/growth-payoff.md) |
| Imagery is too dense, rule games dominate, actions are static, emotion lacks peak, enemies blur together, or chapters feel too short | Dramatic Expansion Pass | [scene-expansion-payoff.md](references/scene-expansion-payoff.md) |
| 修仙/玄幻 long-form planning | Long-Form Xianxia Mode | Load only the relevant xianxia references |

For revisions, use this revision priority unless the user names a different priority:

1. Main story line and continuity.
2. Chapter or arc pattern variety.
3. Character agency and relationship movement.
4. Protagonist growth visibility and earned direct payoff.
5. Information density and pressure release.
6. Psychological depth and decision pressure.
7. Story legibility and language clarity.
8. Emotional variation, transitions, prose rhythm, and line polish.

If the user asks for a full audit, output a compact audit table first, then the highest-leverage fixes. If the user asks for a clean rewrite, apply the relevant pass silently and do not over-explain.

## Story Engine

Before drafting, make sure the story has answers to these questions:

| Element | Check |
| --- | --- |
| Desire | What does the protagonist want right now, and what deeper need hides beneath it? |
| Pressure | What forces action now instead of later? |
| Obstacle | Who or what actively resists the desire? |
| Stakes | What becomes worse if the protagonist fails or delays? |
| Change | What does the scene force the protagonist to learn, lose, choose, or conceal? |
| Hook | What unanswered question pulls the reader forward? |

If any answer is weak, strengthen it before writing long prose.

## Storyline Clarity Pass

Use this pass before outlines, long-form planning, chapter roadmaps, continuations, and revisions where the story feels scattered, episodic, or hard to summarize.

Load [storyline-clarity.md](references/storyline-clarity.md) when the user asks for clearer story lines, plot structure, throughline, roadmap, main quest, arc design, subplot cleanup, or when a generated outline starts reading like disconnected events.

Before writing a plan or draft, establish:

| Layer | Check |
| --- | --- |
| Narrative spine | Can the main story be stated as "A wants B, but C forces D, so A must E before F"? |
| Central question | What question should the reader keep tracking across the arc or volume? |
| Goal ladder | How does the protagonist's immediate goal lead to the next larger goal? |
| Causal chain | Does each major beat happen because of a choice, pressure, mistake, reveal, or consequence from an earlier beat? |
| Turn map | Where do status, knowledge, relationship, danger, or power change irreversibly? |
| Subplot discipline | Which main-line pressure does each subplot intensify, complicate, delay, or resolve? |
| Chapter function | Why must this chapter exist, and what would break if it were removed? |

If the story line is blurry, output a compact storyline map before prose: main line, active subplots, 5-10 causal beats, unresolved hooks, and the next chapter's job.

## Chapter Pattern Variety Pass

Use this pass when consecutive chapters repeat the same structure, such as enemy setup -> protagonist sees through it -> evidence is recorded -> antagonist adds pressure -> chapter ends on a new hook.

Load [chapter-pattern-variety.md](references/chapter-pattern-variety.md) for chapter pattern ledger, anti-isomorphism audit, solution mode rotation, pressure mode rotation, and hook mode rotation.

Before planning or revising a sequence of chapters, create a compact chapter pattern ledger:

| Dimension | Rotate |
| --- | --- |
| Opening pressure | Trap, invitation, aftermath, routine disruption, private cost, public challenge, discovery, travel, negotiation, training, care, loss. |
| Protagonist mode | Detect, misread, choose, bargain, sacrifice, fail, delay, provoke, protect, confess, retreat, ask for help, act first. |
| Solution mode | Evidence, relationship leverage, moral choice, resource trade, public performance, private vow, tactical loss, emotional honesty, hidden ally, changed rule. |
| Antagonist pressure | Legal/status pressure, emotional leverage, resource squeeze, social isolation, false kindness, time limit, moral bind, exposure, silence. |
| Hook mode | New question, consequence, quiet dread, relationship turn, cost revealed, failed plan, unexpected mercy, irreversible choice, delayed payoff. |

If two adjacent chapters share three or more dimensions, revise one chapter. If three chapters repeat the same solution mode or hook mode, break the pattern with failure, aftermath, relationship, strategy, or a different POV/arena.

## Batch Chapter Audit

Use this mode when the user provides or summarizes multiple chapters, especially 3+ chapters, and asks why the middle or later section feels mechanical, tiring, unclear, repetitive, or emotionally flat.

Load [chapter-sequence-audit.md](references/chapter-sequence-audit.md) for audit table formats, chapter function checks, pattern repetition diagnosis, relationship movement, pressure curve, and fix prioritization.

For a multi-chapter audit, output:

| Section | Include |
| --- | --- |
| Pattern table | Chapter number, opening pressure, protagonist mode, solution mode, antagonist mode, hook mode. |
| Movement table | What changes in plot, relationship, emotion, status, resources, or knowledge. |
| Repetition risks | Reused chapter shape, reused clue method, repeated emotional beat, repeated hook, repeated antagonist response. |
| Priority fixes | 3-5 highest-leverage changes before line-level polish. |

Do not rewrite every chapter at once unless asked. Diagnose the sequence first, then propose targeted replacement chapter engines such as aftermath, relationship, strategy, misread, failure, quiet dread, training, resource squeeze, or enemy silence.

## Arc Fatigue Control Pass

Use this pass when several symptoms appear together: pressure stays too continuous, information density remains high, chapter structure has isomorphism risk, and private relationships do not feel loose enough.

Load [arc-fatigue-control.md](references/arc-fatigue-control.md) for reader fatigue audit, sequence load map, pressure curve, density curve, pattern variety, private relationship looseness, and relief chapter design.

Before revising a sequence, create a sequence load map:

| Track | Check |
| --- | --- |
| Pressure curve | How many consecutive chapters are high-pressure, public, dangerous, accusatory, or deadline-driven? |
| Information load | How many new clues, symbols, names, rules, institutions, or reversals are foregrounded per chapter? |
| Pattern risk | Do chapters reuse the same setup, protagonist response, solution mode, antagonist mode, and hook mode? |
| Private relationship looseness | Where do characters interact without immediate evidence, accusation, crisis, or tactical bargaining? |
| Relief chapter | Which chapter lets consequence settle while still changing relationship, strategy, body state, or trust? |

If three or more consecutive chapters are high-pressure and high-density, replace or revise one with aftermath, private repair, routine, care, training, strategy, humor, travel texture, or quiet dread. The relief chapter must still move the story, but through relationship, body, resource, or choice instead of another external squeeze.

## Information Density Pass

Use this pass before drafting or revising scenes with many clues, symbols, mysteries, objects, institutions, or revelations, and when the user says the story is tiring, overloaded, or too high-pressure.

Load [scene-balance.md](references/scene-balance.md) when handling information density, symbol budget, pressure release, breather chapter design, clue delivery, or characters who feel like an evidence pusher instead of a person.

Before finalizing a dense chapter, check:

| Layer | Check |
| --- | --- |
| Information budget | What 1-2 new facts, clues, symbols, or rules must be foregrounded now? What can move to later? |
| Symbol budget | If several motifs recur, which one leads the scene and which ones stay quiet? |
| Emotional anchor | Which character desire, fear, embarrassment, affection, or loss makes the information matter? |
| Pressure release | Is there space after a shock for aftermath, choice, relationship, routine, or bodily recovery? |
| Character agency check | Does each clue-bearing character want something besides delivering evidence? |

When a chapter stacks many charged elements, consolidate or sequence them. Do not introduce multiple major symbols, clues, institutions, and emotional reversals in the same breath unless the scene is deliberately overwhelming and followed by decompression.

## Prose Flow Pass

Use this pass when supporting characters feel like tools, emotional description repeats, or transitions between beats/scenes feel abrupt.

Load [prose-flow.md](references/prose-flow.md) for supporting cast agency, tool-character audit, emotion beat variation, emotional progression, transition bridge design, and scene-to-scene continuity.

Before finalizing a draft or revision, check:

| Layer | Check |
| --- | --- |
| Supporting cast agency | Does each important side character want, avoid, protect, misunderstand, or risk something? |
| Tool-character audit | If the plot function is removed, does the character still have a recognizable human presence? |
| Emotion beat variation | Are repeated emotions shown through changing body, perception, speech, action, and avoidance rather than the same signal? |
| Emotional progression | Does the emotion shift, deepen, sour, crack, or get suppressed across the scene? |
| Transition bridge | Does each scene/paragraph move through time, place, cause, emotional residue, or a deliberate contrast? |

When prose feels repetitive or jumpy, revise for progression: cause -> reaction -> choice -> consequence. Do not stack similar emotional labels, identical body cues, or abrupt location jumps without a bridging beat.

## Psychological Depth Pass

Use this pass when characters act correctly for the plot but their inner life feels thin, reactions stay on the surface, or important turns lack psychological pressure.

Load [psychological-depth.md](references/psychological-depth.md) for inner conflict chain, perception bias, decision pressure, subtext gap, and psychological aftereffect.

Before finalizing a key scene, check:

| Layer | Check |
| --- | --- |
| Inner conflict chain | What desire, fear, shame, debt, loyalty, or false belief collides inside the character? |
| Perception bias | What does the character notice, ignore, misread, or overvalue because of that inner pressure? |
| Decision pressure | How does the inner conflict change what the character says, delays, refuses, risks, or chooses? |
| Subtext gap | What is the difference between what the character says, thinks, feels, and does? |
| Psychological aftereffect | How does the event alter body state, attention, speech, trust, memory, or the next choice? |

Psychological description should not pause the story for explanation. Place it inside stimulus -> interpretation -> contradiction -> choice/consequence.

## Language Clarity Pass

Use this pass when prose is hard to understand, over-abstract, overly ornate, or emotionally/intellectually foggy, while preserving literary texture and avoiding watery prose.

Load [language-clarity.md](references/language-clarity.md) for clarity without flattening, story legibility, sentence opacity, concrete action, high-quality plainness, and revision moves that strengthen story instead of merely simplifying vocabulary.

Before finalizing a draft or revision, check:

| Layer | Check |
| --- | --- |
| Story legibility | Can the reader tell who is doing what, why it matters, and what changed? |
| Sentence opacity | Are long or metaphorical sentences hiding action, cause, subject, or emotional turn? |
| Concrete anchor | Does each abstract idea attach to a visible action, object, gesture, setting, or choice? |
| Quality control | Did simplification preserve rhythm, subtext, image, and character voice instead of becoming summary or watery prose? |
| Reader path | Does each paragraph lead the reader from perception -> meaning -> choice/consequence? |

When language is obscure, revise by clarifying action and causality first, then compress abstractions, then restore one precise image or rhythm. Do not solve obscurity by replacing all texture with blunt explanation.

## Dramatic Expansion Pass

Use this pass when a chapter has strong ideas but not enough lived scene: imagery is too dense, rule-based conflict dominates bodily action, emotion stays restrained without a visible release, enemy pressure is clear but enemy layers blur together, or key nodes end before the reader can feel them.

Load [scene-expansion-payoff.md](references/scene-expansion-payoff.md) for image spacing, action variety, emotional peak design, enemy tier differentiation, and word count breath.

Before finalizing a key chapter, check:

| Layer | Check |
| --- | --- |
| Image spacing | Which one image leads this beat, and which images should be delayed, backgrounded, or converted into action? |
| Action variety | Does the scene move through body, object, terrain, social blocking, pursuit, repair, concealment, or touch instead of only rule debate? |
| Emotional peak | Where does restraint crack into a visible choice, sentence, gesture, confession, refusal, or irreversible act? |
| Enemy tier differentiation | Do different enemies pressure the protagonist through different tools, values, status, intimacy, competence, or risks? |
| Word count breath | Which key node deserves more beat-by-beat expansion before the next turn or hook? |

If a chapter is short at an important node, expand through action, reaction, consequence, and emotional aftereffect. Do not pad with explanation; add scene beats that change body, relationship, status, resource, knowledge, or choice.

## Growth Payoff Pass

Use this pass when the protagonist's growth line is present but not visible enough, pressure stays high for too long, antagonists have hierarchy but weak memory hooks, or the reader can infer the win but cannot feel the shuangdian/direct payoff.

Load [growth-payoff.md](references/growth-payoff.md) for protagonist growth ledger, chapter core compression, pressure relief ratio, antagonist face memory, direct victory cadence, direct payoff ladder, and earned-cost checks.

Before revising a key sequence, check:

| Layer | Check |
| --- | --- |
| Protagonist growth ledger | What changed in choice, behavior, relationship, technique, restraint, worldview, or moral line since the last arc? |
| Chapter core compression | What one or two core points must the reader carry away, and what setting texture can be backgrounded? |
| Pressure relief ratio | How many high-pressure chapters pass before aftermath, recovery, training, relationship ease, strategic quiet, or payoff? |
| Antagonist face memory | What signature action, voice, object, contradiction, desire, fear, or pressure method makes this enemy memorable after the scene ends? |
| Direct victory cadence | When was the last unambiguous win: resource gain, breakthrough win, rescue, enemy driven back, public submission, or enemy loses real power? |
| Direct payoff | What visible reversal, status/resource gain, competence display, justice beat, relationship reward, or emotional release does the reader receive? |
| Earned cost | What setup, sacrifice, limit, witness, or consequence keeps the payoff from feeling cheap? |

If an arc gives pressure for too long without a visible win, relationship shift, resource gain, emotional release, or new competence, insert an earned payoff beat before adding another squeeze. The payoff can be quiet, but the reader should clearly feel what the protagonist gained, proved, protected, or refused.

For shuangwen-leaning chapters, compress each chapter to one or two core points. Worldbuilding texture should clarify stakes, power, cost, or payoff; it should not become a second plot maze the reader must decode before the win lands.

## Drafting Rules

- Start in motion: a decision, interruption, discovery, confrontation, pursuit, ritual gone wrong, or image with implied conflict.
- Anchor each scene in place, body, object, sound, light, weather, texture, or routine. Specificity should reveal character or tension.
- Let exposition arrive through conflict, implication, memory triggered by present action, or necessary choices. Avoid front-loaded history.
- Give every scene a local objective and a turn. The situation at the end must not be the same as at the beginning.
- Stage rule conflicts through action whenever possible: movement, obstacle, object handling, witnesses, terrain, time pressure, bodily cost, or public ritual.
- Avoid chapter pattern lock. Consecutive chapters should not solve conflict through the same detection, evidence, counterpressure, and hook rhythm.
- Use dialogue as pressure. Characters should dodge, test, interrupt, bargain, accuse, hide, or reveal by accident.
- Let clue-bearing characters resist being reduced to evidence. Give them agenda, self-protection, misdirection, embarrassment, loyalty, resentment, humor, or cost.
- Let supporting characters enter scenes with their own pressure, not only the protagonist's need for information, conflict, or comfort.
- Make interiority active: show thought colliding with observation, memory, shame, desire, or fear. Avoid abstract emotion labels alone.
- Turn psychology into motion: stimulus -> biased interpretation -> inner contradiction -> choice, delay, mistake, refusal, or consequence.
- Keep story legible. Even lyrical or mysterious prose should let the reader track subject, action, cause, emotional turn, and consequence.
- Keep each serialized chapter to one or two core points; setting texture should support the chapter promise, not compete with it.
- Vary rhythm. Use short sentences for impact, longer sentences for perception, memory, dread, or emotional drift.
- Vary emotional rendering. Rotate body sensation, selective perception, changed speech, avoidance, action, memory, and silence instead of repeating the same emotion cue.
- Give restrained emotion a payoff. At key nodes, let control crack through one visible action, line, refusal, touch, mistake, or irreversible choice.
- Vary pressure. After several high-stakes chapters, use a breather chapter that changes relationship, strategy, grief, trust, training, status, or private resolve.
- Make protagonist growth visible through changed choices and behavior, not only internal realization.
- Schedule a direct victory cadence: after pressure, regularly give visible wins such as resource gain, breakthrough win, rescue, enemy driven back, public submission, or enemy loses real power.
- Deliver earned direct payoff after setup: visible reversal, witness reaction, resource/status gain, emotional release, or competence display.
- Give key antagonists face memory through distinct entrance, speech rhythm, pressure method, contradiction, desire, or private fear.
- Bridge transitions with cause, time, place, emotional aftertaste, object continuity, or contrast. Abrupt cuts should feel intentional.
- End chapters with a changed situation, a sharper question, an irreversible action, or a resonant image.

## Genre Levers

Use genre expectations deliberately:

- **Romance**: Build attraction through friction, vulnerability, misread signals, and choices that cost something. Avoid instant perfect chemistry without behavior.
- **Mystery/suspense**: Plant fair clues, false interpretations, time pressure, and partial revelations. Do not solve through coincidence.
- **Fantasy/xianxia**: Tie rules of power to cost, culture, hierarchy, and character choice. Avoid introducing abilities only when convenient.
- **Science fiction**: Let speculative rules change social behavior, work, intimacy, law, and risk. Keep technical detail readable and consequential.
- **Historical**: Use period detail through practical life, status, material objects, speech constraints, and institutions. Mark uncertain facts as assumptions.
- **Literary**: Prioritize perception, contradiction, moral ambiguity, image systems, and emotional precision without losing scene movement.
- **Web novel/serialized fiction**: Keep chapter goals clear, refresh conflict often, maintain readable momentum, and end with a clean hook or emotional turn.

## Long-Form Xianxia Mode

Use this mode for 修仙/玄幻/cultivation fantasy, especially when the request involves a full novel, serial, volume plan, sect conflict, realm progression, power scaling, or continuity across many chapters.

Load only the references needed:

- [xianxia-longform.md](references/xianxia-longform.md): full-series architecture, volumes, factions, protagonist arc, xianxia-specific story engines.
- [storyline-clarity.md](references/storyline-clarity.md): narrative spine, causal chain, plotline map, subplot discipline, act/volume clarity.
- [chapter-pattern-variety.md](references/chapter-pattern-variety.md): chapter pattern ledger, anti-isomorphism audit, solution mode rotation, hook mode rotation.
- [chapter-sequence-audit.md](references/chapter-sequence-audit.md): batch chapter audit, audit table formats, arc-level pattern diagnosis, priority fixes.
- [arc-fatigue-control.md](references/arc-fatigue-control.md): reader fatigue audit, sequence load map, pressure curve, density curve, private relationship looseness, relief chapter design.
- [scene-balance.md](references/scene-balance.md): information density, symbol budget, pressure release, breather chapters, character agency in clue scenes.
- [prose-flow.md](references/prose-flow.md): supporting cast agency, emotion beat variation, emotional progression, transition bridge design.
- [psychological-depth.md](references/psychological-depth.md): inner conflict chain, perception bias, decision pressure, subtext gap, psychological aftereffect.
- [language-clarity.md](references/language-clarity.md): clarity without flattening, story legibility, sentence opacity, concrete action, high-quality plainness.
- [scene-expansion-payoff.md](references/scene-expansion-payoff.md): image spacing, action variety, emotional peak, enemy tier differentiation, word count breath.
- [growth-payoff.md](references/growth-payoff.md): protagonist growth ledger, chapter core compression, pressure relief ratio, antagonist face memory, direct victory cadence, direct payoff ladder.
- [cultivation-system.md](references/cultivation-system.md): realms, bottlenecks, breakthroughs, power costs, combat constraints, artifacts, pills, formations, bloodlines.
- [serialization-pacing.md](references/serialization-pacing.md): chapter rhythm, hooks, escalation, web-novel momentum, reader promise management.
- [continuity-ledger.md](references/continuity-ledger.md): story bible, foreshadowing ledger, character state, faction state, item/power inventory, unresolved promises.

Before drafting long-form xianxia, establish or infer:

| Layer | Required decision |
| --- | --- |
| Core promise | What fantasy is the reader staying for: revenge, ascent, sect politics, lone survival, cosmic mystery, romance, clan rise, anti-hero power? |
| Realm ladder | What each major realm changes in lifespan, perception, social status, combat options, cost, and bottleneck? |
| Resource economy | What scarce resources shape conflict: spirit stones, pills, techniques, lands, bloodlines, fate, merit, divine objects? |
| Power constraints | What cannot be solved by raw strength, and what does each power cost or reveal? |
| Faction ecology | Which sects, clans, dynasties, markets, demonic paths, and hidden powers want incompatible things? |
| Arc engine | What chapter, mini-arc, volume, and full-series questions are active at the same time? |
| Main plotline | What single causal line connects the protagonist's first pressure to the volume climax? |
| Chapter core | What one or two core points should the reader remember this chapter for, and which setting details can stay secondary? |
| Pattern variety | How do consecutive chapters vary opening pressure, protagonist response, solution mode, antagonist pressure, and hook mode? |
| Reader fatigue | Where does the arc release pressure, lower information load, and loosen private relationships without stopping movement? |
| Psychology | What desire, fear, false belief, shame, loyalty, or memory changes the protagonist's perception and next choice? |
| Dramatic payoff | Which key chapters need more action variety, clearer emotional peak, enemy differentiation, and word count breath? |
| Growth/payoff | How does the arc make protagonist growth visible, relieve pressure at the right time, and deliver a direct earned win or emotional release? |
| Continuity ledger | What has been promised, planted, learned, damaged, spent, hidden, or owed? |

For xianxia chapter drafts, include at least one concrete scene objective, one pressure source, one cultivation/world detail that changes behavior, one tactical or emotional turn, and one forward hook. Avoid convenient breakthroughs, weightless treasures, faceless arrogance, repetitive "aura surge" prose, and victories that do not change relationships or the larger board.

## Continuation Rules

When continuing supplied text:

1. Extract the current facts: POV, tense, setting, timeline, characters present, unresolved questions, relationship tensions, promises made to the reader, and style markers.
2. Continue from the last emotional beat, not just the last event.
3. Preserve names, pronouns, power rules, injuries, objects, secrets, and what each character knows.
4. Do not retell what the user already provided unless a brief echo is needed for rhythm.
5. If the source text has serious continuity gaps, mention the risk briefly, then choose a consistent path.

## Revision Rules

When revising, diagnose before rewriting unless the user asks for only a clean rewrite. Name the main issue in one concise line, then provide the improved version.

Improve by:

- Replacing summary with scene where the moment deserves dramatization.
- Cutting explanation already visible through action.
- Turning generic emotion into body behavior, selective perception, avoidance, or changed speech.
- Adding conflict to flat dialogue.
- Tightening paragraphs around one movement, image, decision, or emotional beat.
- Preserving the user's intent and best lines whenever possible.

Avoid flattening voice into polished sameness. If the original has a distinctive roughness that serves character, keep it.

## Style Boundaries

If the user asks for the exact style of a living author or copyrighted series, avoid direct imitation. Offer a safer style target using traits instead, such as "taut psychological suspense, close interiority, restrained violence, and bleak humor." Do not continue copyrighted text beyond a brief user-provided excerpt; transform, summarize, or write an original adjacent passage instead.

For harmful, criminal, self-harm, abuse, or evasion content, keep it non-operational and literary. Focus on consequence, psychology, aftermath, implication, investigation, or moral pressure rather than actionable detail.

## Quality Check

Before final output, verify:

- The opening creates curiosity or tension quickly.
- The main story line can be summarized in one sentence and every major beat advances, complicates, or reverses it.
- The protagonist wants something concrete in the scene.
- Conflict escalates through cause and effect, not coincidence.
- Consecutive chapters vary their structure; the current chapter does not repeat the same trap, recognition, evidence, counterpressure, and hook pattern unless repetition is intentionally meaningful.
- Information density is staged: the scene does not foreground too many clues, symbols, rules, factions, and reversals at once.
- Multi-chapter sequences manage reader fatigue: pressure curve, information load, pattern variety, and private relationship looseness are not all maxed at once.
- Key nodes get enough word count breath: the chapter does not rush past action, reaction, emotional peak, or consequence.
- The protagonist's growth is visible through changed choices, behavior, relationships, technique, restraint, or moral line, not only stated internally.
- Each serialized chapter is compressible to one or two core points; rich setting texture supports reader entry instead of blocking it.
- High-pressure sequences include relief/payoff before reader fatigue hardens.
- The arc gives earned direct payoff: visible reversal, status/resource gain, competence display, emotional release, justice beat, or relationship reward with witness and consequence.
- The arc includes direct victory cadence: resources taken, realm breakthrough, rescue, enemy killed or driven back, public submission, or enemy loss of real power at regular intervals.
- The prose contains specific sensory and behavioral detail.
- The language is clear enough to follow without flattening into watery prose: subject, action, cause, and consequence remain visible.
- Dialogue fits the relationship, situation, and social pressure.
- Clue-bearing characters have agency, desire, and cost; they are not only evidence pushers.
- Supporting characters are not only plot tools; they carry their own desire, fear, pressure, contradiction, or cost.
- Key scenes include readable psychology: inner conflict, perception bias, decision pressure, subtext gap, and aftereffect shape action rather than stopping it.
- Emotional beats progress and vary instead of repeating the same body cue, label, or sentence shape.
- Restrained emotion has a readable emotional peak where control visibly cracks or changes behavior.
- Enemy pressure is layered: different antagonists or enemy tiers use distinct methods, values, risks, and relationships to power.
- Antagonists have memorable face hooks: signature action, pressure style, contradiction, voice, image, personal desire, or private fear.
- Transitions are bridged by cause, time, place, emotional residue, object continuity, or deliberate contrast.
- Interior monologue reveals contradiction rather than explaining everything.
- High-pressure arcs include pressure release: aftermath, intimacy, routine, recovery, reflection, training, humor, or a quiet strategic choice.
- Continuity is preserved when continuing existing text.
- For xianxia, realm rules, resource costs, faction consequences, injuries, artifacts, and promises remain consistent.
- The ending creates movement: question, choice, cost, reversal, image, or emotional residue.
- No obvious AI tone: generic adjectives, slogan-like lines, perfect symmetry, over-explaining, or summary disguised as scene.

Append a short `Quality notes` section only when the user asks for critique, diagnostics, or revision rationale. For pure creative drafting, give the polished creative output first.

## Example Requests

```text
Use $writer-skill to outline a 30-chapter urban fantasy novel with a morally gray protagonist.
Use $writer-skill to make my xianxia story line clearer with a narrative spine, causal beat map, and subplot cleanup.
Use $writer-skill to audit these ten chapters for repetitive chapter patterns and propose a more varied rhythm.
Use $writer-skill to run a batch chapter audit on chapters 18-27 and give me an audit table plus priority fixes.
Use $writer-skill to reduce arc fatigue: lower continuous pressure, stage dense information, vary chapter patterns, and loosen private relationships.
Use $writer-skill to make this chapter easier to understand and more story-driven without turning the prose into watery plain speech.
Use $writer-skill to expand this key chapter with more action variety, clearer emotional peak, distinct enemy layers, and enough word count breath.
Use $writer-skill to make the protagonist growth line more visible, sharpen antagonist face memory, and make the payoff more direct without cheapening it.
Use $writer-skill to compress each chapter to one or two core points and add a direct victory cadence for a more accessible shuangwen rhythm.
Use $writer-skill to deepen psychological description so character choices feel driven by inner conflict, perception bias, and aftereffect.
Use $writer-skill to revise this chapter so the clues and symbols have more breathing room and the evidence-bearing characters feel alive.
Use $writer-skill to smooth this chapter's transitions, reduce repeated emotion beats, and make the supporting cast less tool-like.
Use $writer-skill to build a 200-chapter xianxia story bible with realm progression, sect politics, and foreshadowing ledgers.
Use $writer-skill to continue this Chinese web novel chapter while preserving the current POV and tone.
Use $writer-skill to rewrite this scene with stronger subtext, less exposition, and a sharper ending hook.
Use $writer-skill to diagnose why my opening chapter feels flat and propose a better first scene.
```

