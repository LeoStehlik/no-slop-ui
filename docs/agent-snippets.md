# Agent Snippets

Copy the smallest snippet that fits your agent surface.

## Codex Repo Instruction

```text
Use no-slop-ui for frontend work. Before editing visible UI, read no-slop-ui/SKILL.md. Build the actual product surface first. Avoid glassmorphism, decorative gradients, nested cards, oversized rounded corners, fake metrics, vague SaaS copy, and transform-heavy hover effects. After editing, check examples/review-checklist.md and report any misses before calling the UI done.
```

## Claude Code Project Instruction

```text
For UI tasks, apply no-slop-ui. Prefer quiet product UI: stable layout, restrained radius, subtle borders, clear hierarchy, direct labels, and real workflow density. Do not ship generic AI dashboard styling. Use no-slop-ui/examples/review-checklist.md as the final acceptance pass.
```

## OpenClaw Skill Usage

```text
/no-slop-ui
Build this visible interface with the repository's existing design system first. Keep the screen practical and scannable. Run the No Slop UI checklist before final response.
```

## Cursor Or Custom Agent Prompt

```text
Read no-slop-ui/SKILL.md, then revise this UI. Remove generic AI styling: decorative gradients, glass panels, huge cards, empty metric grids, eyebrow labels, vague copy, and hover transforms. Keep only the UI structure that helps the user complete the task. Return a checklist verdict using examples/review-checklist.md.
```

## Pull Request Review Prompt

```text
Review this frontend PR with no-slop-ui. Focus on product fit, layout density, component states, visual restraint, responsive text fit, and generic AI visual patterns. List blockers first. Do not request purely subjective polish unless it affects usability or makes the UI look AI-generated.
```

## Tiny Brief Clause

```text
Visual quality gate: no-slop-ui applies. The task is not complete until generated UI passes examples/review-checklist.md or documents a justified exception.
```
