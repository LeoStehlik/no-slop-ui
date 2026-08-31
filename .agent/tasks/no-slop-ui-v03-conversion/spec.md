# Task: no-slop-ui-v03-conversion

## Task Statement

Ship No Slop UI v0.3 as a conversion-focused release. The repository already receives search and ChatGPT traffic, but the public surface needs faster proof, clearer install/adoption paths, practical snippets, and a stronger review artifact so visitors can understand and use the skill quickly.

## Acceptance Criteria

**AC1:** The README has a stronger above-the-fold conversion path.
- Verify: Inspect `README.md` for a concise problem statement, quick-start command block, agent prompt, proof image, and links to the proof/checklist/snippets before long background material.

**AC2:** The repo includes a real before/after proof artifact.
- Verify: `docs/conversion-proof.md` exists and documents the before failure, after pass, checklist verdict, concrete changes, and conversion path; `assets/no-slop-ui-before-after.svg` exists and is referenced by README.

**AC3:** The repo includes copy-paste framework/agent snippets.
- Verify: `docs/agent-snippets.md` includes concise snippets for Codex, Claude Code, OpenClaw, Cursor/custom agents, PR review, and brief clauses.

**AC4:** The review checklist is stronger as a standalone acceptance artifact.
- Verify: `examples/review-checklist.md` covers product fit, layout, components, visual style, motion, copy, and explicit PASS/REVISE/ESCALATE verdicts.

**AC5:** Skill metadata and release surface are prepared for v0.3.0.
- Verify: `SKILL.md` metadata version is `0.3.0`, validation passes, and a GitHub release/tag can be cut from the final commit.

**AC6:** The release has durable proof.
- Verify: `.agent/tasks/no-slop-ui-v03-conversion/` contains spec/evidence/verdict artifacts; repo validation, clean clone validation, GitHub Actions, and release checks are recorded.

## Constraints

- Keep the skill small and framework-agnostic.
- Do not turn the repo into a broad UI framework or component library.
- Preserve the blunt product philosophy: stop generic AI UI sludge with practical rules.
- Keep public artifacts generic and free of private workspace paths or client data.
- Keep development and release work on the approved development host, not the runtime control-plane host.

## Non-Goals

- No native plugin wrapper.
- No npm package or component library.
- No hosted documentation site.
- No fake benchmark claims.
- No external posting or launch promotion in this task.

## Verification Approach

Run the repo validator, inspect local links, run a sensitive-path scan, verify the proof asset exists, do a clean-clone validation after push, confirm GitHub Actions, and inspect release/sync state.
