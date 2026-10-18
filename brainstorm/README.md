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

### Prerequisites

- Access to [Claude.ai](https://claude.ai) (Pro, Team, or Enterprise)
- Claude must support the Skills system (available via the Skills interface in Claude.ai)

### Setup

1. **Save the skill file**  
   Place `SKILL.md` in your skills directory, e.g.:
   ```
   /mnt/skills/user/brainstorm/SKILL.md
   ```

2. **Register the skill**  
   Add the skill to your skill configuration (e.g. in the system prompt or via the Claude.ai Skills interface):
   ```
   name: brainstorm
   description: Facilitate structured, collaborative brainstorming sessions using proven ideation techniques. Use when the user wants to brainstorm.
   ```

3. **Done** — Claude will automatically detect when to activate the skill.

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

The skill includes 30+ techniques across 6 categories:

**Collaborative:** Yes-And Building, Brainwriting Round Robin, Random Stimulation, Role Playing, Ideation Relay  
**Creative:** What-If Scenarios, Analogical Thinking, Reversal/Inversion, First Principles, SCAMPER, Forced Relationships, Concept Blending  
**Deep Analysis:** Five Whys, Assumption Reversal, Question Storming, Failure Analysis, Constraint Mapping, Morphological Analysis  
**Structured:** Six Thinking Hats, Mind Mapping, Solution Matrix, Decision Tree Mapping, Trait Transfer  
**Playful / Theatrical:** Alien Anthropologist, Future Self Interview, Parallel Universe, Dream Solution, Persona Journey  
**Wild / Edge-Case:** Chaos Engineering, Anti-Solution, Black Swan Events, Zombie Apocalypse  

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

## License & origin

This skill was developed as a standalone `SKILL.md` and is compatible with the Claude Skills system. It can be freely adapted and extended.
