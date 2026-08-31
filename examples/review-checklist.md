# No Slop UI Review Checklist

Use this as a quick proof pass after an agent generates or edits UI.

## Product Fit

- [ ] The first screen is the actual product experience, not a marketing hero unless the task explicitly asked for a landing page.
- [ ] The layout helps the user's real workflow: scan, compare, edit, decide, or navigate.
- [ ] The UI does not invent decorative metrics, charts, badges, or activity just to fill space.
- [ ] The screen would still make sense with real production data, empty states, and long labels.

## Layout

- [ ] Dashboards use dense, scannable structure instead of oversized decorative cards.
- [ ] Sidebars and toolbars have stable dimensions and do not float inside decorative shells.
- [ ] Cards are used only for repeated items, modals, or genuinely framed tools.
- [ ] No card is nested inside another card.
- [ ] Mobile and desktop views have explicit responsive constraints; text does not overlap or resize the layout awkwardly.

## Components

- [ ] Buttons use familiar icons where appropriate and avoid pill styling by default.
- [ ] Tables, forms, filters, tabs, and menus use normal product patterns rather than novelty styling.
- [ ] Inputs have visible labels, ordinary borders, and predictable focus states.
- [ ] Loading, disabled, active, selected, empty, and error states preserve stable dimensions.

## Visual Style

- [ ] No glassmorphism, decorative gradients, gradient text, glow, or floating background blobs.
- [ ] Border radius stays restrained: usually 6-10px for controls and 8px or less for cards unless the existing design system says otherwise.
- [ ] Typography uses clear hierarchy without hero-scale type inside compact UI surfaces.
- [ ] The palette does not collapse into one hue family or generic dark-blue/purple AI styling.
- [ ] Shadows are subtle; no large blur shadows, coloured glow, or floating-panel drama.

## Motion

- [ ] Hover states are subtle: color, border, or shadow changes only.
- [ ] No transform, bounce, spring, scale, slide, or parallax effects unless the product domain truly needs them.
- [ ] Loading states preserve layout dimensions.

## Copy

- [ ] Headings and labels are functional, not decorative.
- [ ] No eyebrow-label plus headline pattern.
- [ ] No vague SaaS filler such as clarity, command center, unlock productivity, seamless, or supercharge unless it is real product language.
- [ ] Button text names the action and still fits at mobile widths.

## Verdict

- **PASS:** No checklist section has more than one miss, and no hard visual ban is present.
- **REVISE:** Two or more checks fail, or any hard-ban visual pattern appears.
- **ESCALATE:** A no-slop rule conflicts with accessibility, product requirements, localization, security, or the existing design system. Preserve the higher-priority requirement and document the tradeoff.
