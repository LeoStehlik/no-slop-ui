# No Slop UI Review Checklist

Use this as a quick proof pass after an agent generates or edits UI.

## Layout

- [ ] The first screen is the actual product experience, not a marketing hero unless the task explicitly asked for a landing page.
- [ ] Dashboards use dense, scannable structure instead of oversized decorative cards.
- [ ] Sidebars and toolbars have stable dimensions and do not float inside decorative shells.
- [ ] Mobile and desktop views have clear responsive constraints; text does not overlap or resize layout awkwardly.

## Components

- [ ] Buttons use familiar icons where appropriate and avoid pill styling by default.
- [ ] Cards have a practical reason to exist: repeated items, modals, or framed tools.
- [ ] No card is nested inside another card.
- [ ] Tables, forms, filters, tabs, and menus use normal product patterns rather than novelty styling.

## Visual Style

- [ ] No glassmorphism, decorative gradients, gradient text, glow, or floating background blobs.
- [ ] Border radius stays restrained: usually 6-10px for controls and 8px or less for cards unless the existing design system says otherwise.
- [ ] Typography uses clear hierarchy without hero-scale type inside compact UI surfaces.
- [ ] The palette does not collapse into one hue family or generic dark-blue/purple AI styling.

## Motion

- [ ] Hover states are subtle: color, border, or shadow changes only.
- [ ] No transform, bounce, spring, scale, or slide effects unless the product domain truly needs them.
- [ ] Loading states preserve layout dimensions.

## Copy

- [ ] Headings and labels are functional, not decorative.
- [ ] No eyebrow-label plus headline pattern.
- [ ] No vague SaaS filler such as clarity, command center, or unlock productivity unless it is real product language.

## Verdict

If two or more checks fail, revise the UI before calling the task done.
