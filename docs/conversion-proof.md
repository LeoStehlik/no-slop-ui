# No Slop UI v0.3 Conversion Proof

This artifact exists so a stranger arriving from GitHub, Google, or ChatGPT can see the rule set working in under a minute.

## Scenario

An AI coding agent is asked to build a review queue for an internal operations tool. The user needs to scan items, see status, and run a check.

The common generated result looks flashy but weak: glass panel, decorative gradient, vague command-center copy, oversized radius, fake metric boxes, and no real workflow density.

The no-slop-ui result is plainer: fixed navigation, direct page title, ordinary action button, table rows, subtle borders, and no decorative filler.

Open the browser demo: [`../examples/before-after.html`](../examples/before-after.html)

## Before Verdict

| Checklist Area | Verdict | Evidence |
| --- | --- | --- |
| Product fit | FAIL | The generated screen invents metric cards instead of supporting review work. |
| Layout | FAIL | The UI centers one oversized floating panel instead of a real work surface. |
| Components | FAIL | Cards and metric boxes are decorative; no table, filters, or task structure. |
| Visual style | FAIL | Gradient background, frosted panel, large radius, glow/shadow, purple-blue AI palette. |
| Copy | FAIL | "Operational clarity" and "Command centre" describe a mood, not a task. |
| Motion | PASS | The compact demo does not include motion. |

Overall: **REVISE**

## After Verdict

| Checklist Area | Verdict | Evidence |
| --- | --- | --- |
| Product fit | PASS | The screen now centers the review queue task. |
| Layout | PASS | Fixed sidebar, stable content area, table-first workflow. |
| Components | PASS | Ordinary nav, toolbar, button, and table. |
| Visual style | PASS | Solid surfaces, subtle borders, restrained radius, no glow or decorative gradient. |
| Copy | PASS | Labels name the user's task directly. |
| Motion | PASS | No decorative movement required. |

Overall: **PASS**

## What Changed

- Removed decorative gradient and glass panel.
- Replaced fake metric cards with a real table.
- Replaced vague copy with task labels.
- Reduced radius and shadow strength.
- Added stable sidebar and toolbar dimensions.
- Kept the example small enough to inspect quickly.

## Why This Converts Better

People arriving from search or ChatGPT need immediate proof. A rule list is useful, but a before/after artifact shows the taste boundary faster: the repo is not selling a style, it is preventing a predictable agent failure.

The conversion path is now:

1. Land on README.
2. See the proof image.
3. Open the live HTML example.
4. Copy an agent snippet.
5. Use the checklist before accepting generated UI.
