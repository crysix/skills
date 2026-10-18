# 🧠 Brainstorm Skill

A structured, collaborative brainstorming facilitator for Claude — built on proven ideation techniques from creativity research and design thinking.

---

## What does this skill do?

Instead of just dumping a list of ideas, Claude acts as an **active facilitator**: it asks targeted questions, guides you through techniques, builds on your responses, and helps you move from obvious ideas to genuine breakthroughs.

**Core principles:**
- **Quantity** before quality
- **Diverge** before converging — stay in idea-generation mode longer than feels natural
- Claude asks **one question at a time** — no question bombardment
- No evaluation during the ideation phase
- Target: 50–100+ ideas for larger sessions

---

## Installation

### Let Claude install it (easiest)

Give Claude Code the link to this skill and ask it to install it:

**For all projects**
```
Install the skill from https://github.com/crysix/skills/tree/main/brainstorm globally so it is available in every project.
```

**For this project only**
```
Install the skill from https://github.com/crysix/skills/tree/main/brainstorm in this project.
```

Claude downloads the folder and puts it in the right place: `~/.claude/skills/brainstorm/` for all projects, `.claude/skills/brainstorm/` for one project.

### Install manually

```bash
git clone https://github.com/crysix/skills.git ~/skills

# all projects
mkdir -p ~/.claude/skills && cp -r ~/skills/brainstorm ~/.claude/skills/

# this project only (run inside the project)
mkdir -p .claude/skills && cp -r ~/skills/brainstorm .claude/skills/
```

Use `ln -s` instead of `cp -r` to pick up updates with `git pull`.

- **Codex:** copy the folder to `~/.codex/skills/` instead.
- **claude.ai:** zip the `brainstorm` folder and upload it in the Skills settings.

No configuration needed; Claude detects automatically when to use the skill.

---

## Usage

### Trigger phrases

The skill activates when you use phrases like:

```
"Let's brainstorm about ..."
"I need ideas for ..."
"Brainstorming session on ..."
"Help me come up with ideas for ..."
"I want to think creatively about X"
```

### Typical session flow

```
You:    "Let's brainstorm."
Claude: "What are we brainstorming about?"

You:    "New features for my SaaS app"
Claude: "What outcome do you want from this session?"

You:    "A list of concrete feature ideas for the next 3 months"
Claude: "Are there constraints, audiences, or resources I should consider?"

...
```

Questions you have already answered are skipped: if your first message names the topic, Claude goes straight to the next question (see the example opener below).

After the setup phase, Claude summarizes the topic, goal, constraints, and preferred energy style, then asks for confirmation before starting the actual session.

---

## Brainstorming modes

At the start, you and Claude choose one of four modes:

| Mode | Description |
|---|---|
| **User-selected techniques** | You choose from the technique library |
| **Recommended techniques** | Claude picks methods based on your topic and goals |
| **Random technique** | Surprise as a creative catalyst to break patterns |
| **Progressive flow** | Start broad, then gradually narrow toward actionable ideas |

---

## Available techniques (overview)

The skill includes 44 techniques across 7 categories:

**Collaborative:** Yes-And Building, Brainwriting Round Robin, Random Stimulation, Role Playing, Ideation Relay  
**Creative:** What-If Scenarios, Analogical Thinking, Reversal/Inversion, First Principles, Forced Relationships, Time Shifting, Metaphor Mapping, Cross-Pollination, Concept Blending, Reverse Brainstorming  
**Deep Analysis:** Five Whys, Morphological Analysis, Provocation, Assumption Reversal, Question Storming, Constraint Mapping, Failure Analysis, Emergent Thinking  
**Structured:** SCAMPER, Six Thinking Hats, Mind Mapping, Resource Constraints, Decision Tree Mapping, Solution Matrix, Trait Transfer  
**Playful / Theatrical:** Alien Anthropologist, Future Self Interview, Parallel Universe, Emotion Orchestra, Dream Solution, Persona Journey  
**Wild / Edge-Case:** Chaos Engineering, Pirate Mode, Zombie Apocalypse, Anti-Solution, Black Swan Events  
**Nature / Systems:** Nature's Solutions, Ecosystem Thinking, Evolutionary Pressure  

---

## Output format

### During the session (divergence phase)

```markdown
**[Category #1] Idea Name**
_Concept:_ 1–3 sentence description.
_Novelty:_ What makes this different from the obvious answer.
```

### After the session (convergence phase)

```markdown
## Organized Themes

### Theme 1: ...
- Idea
- Idea

## Top Priorities

1. ...
2. ...

## Action Plan

### Idea: ...
- Next step:
- Resources needed:
- Risks / blockers:
- Success metric:
- Timeline:
```

---

## Tips for better sessions

- **Trust the pace** — Claude will guide you through questions before suggesting ideas. That's intentional.
- **Answer openly** — unfinished or wild ideas are very welcome.
- **Say "next"** — to move to another technique, just say "next" or "move on."
- **Say "organize"** — when you're ready to cluster and prioritize ideas.
- **Leverage domain pivots** — every ~10 ideas, Claude deliberately shifts perspective (e.g. from UX → business model → technical feasibility) to break thinking routines.

---

## Example session opener

```
You:    "I want to brainstorm: new monetization ideas for a SaaS product."

Claude: "What outcome do you want from this session?"

You:    "Concrete revenue ideas I can test within 1–2 months."

Claude: "Are there any constraints — budget, team size, technical limits?"

You:    "Solo project, no budget, Laravel/Vue stack."

Claude: "And what energy should the session have — practical and actionable,
         or wild and unconstrained first?"
```

---

## Author

Christian Hinz ([@crysix](https://github.com/crysix))

---

## License

MIT, see [LICENSE](../LICENSE). Feel free to adapt and extend it.
