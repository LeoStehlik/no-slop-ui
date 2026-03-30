---
name: no-slop-ui
description: Prevents generic AI UI slop when building any frontend. Use whenever generating or reviewing HTML, CSS, React, Next.js, Vue, Svelte, plain HTML dashboards, admin panels, or landing pages. Stops floating glass cards, gradient abuse, oversized rounded corners, eyebrow labels, hero sections inside dashboards, and every other "AI-generated UI" tell. Enforces clean, honest, human-designed aesthetics inspired by Linear, Raycast, Stripe, and GitHub. Stack-agnostic.
---

# No Slop UI

You are building UI for a human audience. The goal is functional, honest, clean. Not impressive. Not dramatic. **Normal.**

If a design decision feels like the easy AI default — it probably is. Pick the harder, cleaner option.

Read `references/banned-patterns.md` for the full banned list before writing any UI code.
Read `references/colour-palettes.md` when you need to pick colours.

## The Standard

Think **Linear. Raycast. Stripe. GitHub.** They don't try to grab attention. They just work.

**What normal looks like:**
- Sidebar: 240–260px fixed, solid background, 1px border-right. No floating shells, no rounded outer corners.
- Cards: 8–12px radius max, subtle 1px border, shadow max `0 2px 8px rgba(0,0,0,0.08)`. No glow, no float.
- Buttons: solid fill or simple border, 6–10px radius max. No pills, no gradients.
- Typography: clear hierarchy, 14–16px body, system font or single sans-serif. No mixed serif/sans.
- Spacing: 4/8/12/16/24/32px scale. Consistent. No random gaps.
- Borders: 1px solid, subtle colour. No thick decorative borders, no gradient borders.
- Transitions: 100–200ms ease. Opacity or colour only. No bouncy, no transforms.
- Inputs: solid border, simple focus ring. Labels above fields.
- Icons: 16–20px, monochrome or subtle colour, no decorative backgrounds.

## Colour Priority

1. **Use existing project colours first** — read the Tailwind config or CSS variables.
2. If no palette exists — pick from `references/colour-palettes.md`.
3. Never invent random colour combinations.

## Stack-Specific Notes

**shadcn/ui + Tailwind:**
- Use shadcn components as-is — don't re-invent what's already there
- Respect the existing CSS variable system (`--background`, `--foreground`, `--primary` etc.)
- Don't override component defaults unless there's a clear product reason

**Plain HTML dashboards:**
- Single-file is fine — keep it self-contained
- Use CSS custom properties for theming
- No external CDN dependencies unless absolutely necessary

## Hard Rules

- No floating glassmorphism panels
- No gradient backgrounds as decoration
- No oversized rounded corners (20px+ everywhere)
- No eyebrow labels (`<small>SECTION LABEL</small>` above headings)
- No hero sections inside internal dashboards
- No decorative copy ("Operational clarity without the clutter")
- No metric-card grid as the default dashboard layout
- No fake charts that exist to fill space
- No transform animations on hover
- No `Segoe UI`, `Trebuchet MS`, `Arial` font stacks
- No status dots via `::before` pseudo-elements
- No nav badges unless they carry real data
- No pill buttons everywhere
- No dramatic box shadows (24px+ blur)
- No mixed alignment (some left-aligned, some floating center)

Full banned list with examples: `references/banned-patterns.md`
