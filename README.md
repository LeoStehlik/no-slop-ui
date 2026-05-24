# no-slop-ui

![Validate](https://github.com/LeoStehlik/no-slop-ui/actions/workflows/validate.yml/badge.svg)

**Stop AI UI slop. Build interfaces that look human-designed.**

AI coding agents default to the same tired patterns: floating glass cards, gradient abuse, oversized rounded corners, eyebrow labels, hero sections inside dashboards. After a while you can spot "AI UI" from a mile away.

This skill exists to stop that.

`no-slop-ui` is a frontend design rule set for AI coding agents. It blocks the default AI aesthetic and pushes toward clean, functional, honest interfaces - the kind built by teams like Linear, Raycast, Stripe, and GitHub.

**Status:** usable OpenClaw/Codex skill. It is intentionally small: install it, let it trigger on frontend work, and use the checklist in `examples/review-checklist.md` before accepting generated UI.


## Activation Boundary

Use `no-slop-ui` for explicit UI design, frontend implementation, visual polish, or design review tasks. It should not trigger on backend-only work, infrastructure tasks, copywriting, diagrams, or unrelated code review.

The rules are advisory visual constraints. They do not override accessibility, security, localization, product requirements, or an existing project design system.

## Use Cases

- stop AI agents from producing generic glassy dashboard UI
- review frontend work before accepting generated code
- give coding agents concrete design rules instead of taste adjectives
- keep app screens quiet, usable, and domain-appropriate

---

## Credibility Artifact

See [`examples/README.md`](examples/README.md) for the example index, or open [`examples/before-after.html`](examples/before-after.html) to compare generic AI dashboard habits with a plain usable work surface.

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

OpenClaw will auto-discover the skill. Use it when the task is explicitly about frontend UI work.

### Codex / Claude Code / other agents

Include the contents of `SKILL.md` in your system prompt or agent instructions when asking for UI generation.

Or reference the file directly in your prompt:

```
Read no-slop-ui/SKILL.md before building any UI.
```

---

## Usage

Invoke it explicitly for UI work:

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
└── examples/
    └── review-checklist.md         Fast acceptance checklist for generated UI
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

Before accepting generated UI, run the short proof checklist in [`examples/review-checklist.md`](examples/review-checklist.md).

---


## When To Use Which Repo

Use this repo when an AI agent is building frontend UI and you want to block the usual generic output: glass panels, decorative gradients, oversized rounded corners, empty hero copy, and dashboard sludge.

Use the neighbouring tools at different points in the workflow:

| Need | Use |
| --- | --- |
| Turn a fuzzy request into an executable agent brief | [Brief Master](https://github.com/LeoStehlik/brief-master) |
| Prove one coding task is actually done | [Proof Loop](https://github.com/LeoStehlik/proof-loop) |
| Improve repeated agent behaviour with evals | [Loopsmith](https://github.com/LeoStehlik/loopsmith) |
| Keep source-backed memory for long-running agents | [Sovereign Brain](https://github.com/LeoStehlik/decoupled-agent-memory) |
| Stop frontend agents producing generic UI sludge | [no-slop-ui](https://github.com/LeoStehlik/no-slop-ui) |

A practical chain looks like this: messy request -> Brief Master brief -> Proof Loop task -> Loopsmith eval if the same failure keeps recurring -> Sovereign Brain records the durable decision.

## Related Tools

- [Brief Master](https://github.com/LeoStehlik/brief-master) - write frontend briefs that include clear audience, constraints, and success criteria before UI generation starts.
- [Proof Loop](https://github.com/LeoStehlik/proof-loop) - use when a UI change needs explicit acceptance criteria, screenshots, browser checks, or fresh verification before it is called done.
- [Loopsmith](https://github.com/LeoStehlik/loopsmith) - use when the same UI-quality failure keeps recurring and should become an eval case rather than another one-off review.

## Inspiration

Inspired by [Uncodixfy](https://github.com/cyxzdev/Uncodixfy) by cyxzdev. Built as our own take - adapted, extended, and published as an OpenClaw skill.

---

## License

MIT - see [LICENSE](LICENSE)
