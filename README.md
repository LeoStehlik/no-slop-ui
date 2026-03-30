# no-slop-ui

**Stop AI UI slop. Build interfaces that look human-designed.**

AI coding agents default to the same tired patterns: floating glass cards, gradient abuse, oversized rounded corners, eyebrow labels, hero sections inside dashboards. After a while you can spot "AI UI" from a mile away.

This skill exists to stop that.

`no-slop-ui` is a rule set for AI coding agents that blocks the default AI aesthetic and pushes toward clean, functional, honest interfaces - the kind built by teams like Linear, Raycast, Stripe, and GitHub.

---

## What It Does

- Blocks the most common AI UI anti-patterns (full list in `references/banned-patterns.md`)
- Enforces consistent spacing, typography, border-radius, and shadow rules
- Provides curated dark and light colour palettes when no project palette exists
- Stack-agnostic: works with React, Next.js, Vue, Svelte, plain HTML, Tailwind, shadcn/ui - anything

---

## Installation

### OpenClaw

Add your workspace skills directory to `openclaw.json`:

```json
{
  "skills": {
    "load": {
      "extraDirs": ["/path/to/your/skills"]
    }
  }
}
```

Clone this repo into that directory:

```bash
git clone https://github.com/LeoStehlik/no-slop-ui.git /path/to/your/skills/no-slop-ui
```

OpenClaw will auto-discover the skill. It triggers automatically whenever you ask for frontend UI work.

### Codex / Claude Code / other agents

Include the contents of `SKILL.md` in your system prompt or agent instructions when asking for UI generation.

Or reference the file directly in your prompt:

```
Read no-slop-ui/SKILL.md before building any UI.
```

---

## Usage

Once installed in OpenClaw, it triggers automatically on any UI task. You can also invoke it explicitly:

```
/no-slop-ui
```

Or reference it in agent briefs:

```
Apply no-slop-ui rules to this component.
```

---

## What's Inside

```
no-slop-ui/
├── SKILL.md                        Core rules and standards
└── references/
    ├── banned-patterns.md          Full banned list with HTML examples
    └── colour-palettes.md          Dark + light palettes to use when no project palette exists
```

---

## The Standard

> Think Linear. Think Raycast. Think Stripe. Think GitHub.  
> They don't try to grab attention. They just work.

**What normal looks like:**
- Sidebar: 240–260px fixed, solid background, 1px border-right
- Cards: 8–12px radius max, subtle 1px border, `box-shadow: 0 2px 8px rgba(0,0,0,0.08)` max
- Buttons: solid fill or outlined, 6–10px radius max - no pills, no gradients
- Typography: 14–16px body, single typeface, clear hierarchy - no mixed serif/sans
- Spacing: 4/8/12/16/24/32px scale - consistent, never random
- Transitions: 100–200ms ease - opacity or colour only, no transform effects

**Hard no:**
- Glassmorphism / frosted panels
- Gradient backgrounds as decoration  
- Eyebrow labels (`<small>SECTION NAME</small>` + heading)
- Hero sections inside internal dashboards
- Decorative copy ("Operational clarity without the clutter")
- Metric-card grid as the default dashboard layout
- Transform animations on hover
- Dramatic box shadows (24px+ blur)

Full list: [`references/banned-patterns.md`](references/banned-patterns.md)

---

## Inspiration

Inspired by [Uncodixfy](https://github.com/cyxzdev/Uncodixfy) by cyxzdev. Built as our own take - adapted, extended, and published as an OpenClaw skill.

---

## License

MIT - see [LICENSE](LICENSE)
