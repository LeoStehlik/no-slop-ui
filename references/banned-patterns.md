# Banned UI Patterns

Every item below is what AI-generated UI does by default. Recognise it. Avoid it.

## Layout

| Banned | Use instead |
|--------|-------------|
| Floating detached sidebar with rounded outer shell | Fixed sidebar, solid bg, 1px border-right |
| Hero section inside an internal dashboard | Standard page header, h1 + subtitle only |
| Metric-card grid as default dashboard layout | Content-first layout — metrics only where they belong |
| Right-side rail with "Today" schedule | Only if product explicitly requires it |
| Asymmetric creative layout | Predictable grid/flex |
| Dead space to look expensive | Consistent 24–32px padding |
| Mobile: everything stacked into one long scroll | Proper responsive breakpoints |

## Components

| Banned | Use instead |
|--------|-------------|
| Glassmorphism / frosted panels | Solid background, subtle border |
| Floating cards with dramatic shadows | `box-shadow: 0 2px 8px rgba(0,0,0,0.08)` max |
| Pill buttons everywhere | 6–10px border-radius max |
| Gradient button backgrounds | Solid fill or outlined |
| Animated underline inputs / morphing focus | `outline: 2px solid var(--ring)` |
| Fancy floating labels on inputs | Labels above the field, always |
| Dropdown with entrance animation | Simple list, subtle shadow, no animation |
| Modal with slide-in / scale animation | Centered overlay, simple fade |
| Tabs with sliding pill indicator | Underline or border indicator only |
| Zebra stripes on tables (unless data-dense) | Clean rows, subtle hover |
| Status dots via `::before` pseudo-elements | Simple inline badge or icon |

## Typography

| Banned | Use instead |
|--------|-------------|
| Eyebrow label: `<small>TEAM COMMAND</small>` + h2 | Just h1/h2 with proper hierarchy |
| Uppercase + letter-spacing labels everywhere | Reserve for truly categorical labels |
| Gradient text | Solid colour |
| Mixed serif + sans-serif | Single typeface family |
| Decorative copy: "One place to track what matters" | Direct, functional headings only |
| `Segoe UI`, `Trebuchet MS`, `Arial` | System UI or a single clean sans-serif |

## Colour & Visual

| Banned | Use instead |
|--------|-------------|
| Soft corporate gradients as backgrounds | Solid colours from the palette |
| Blue-black gradient "premium dark mode" | True dark: `#0f172a` / `#1e293b` |
| Cyan accents on dark blue | Muted, intentional accent colour |
| Coloured glows on cards or buttons | No glow |
| Conic-gradient donuts as decoration | No decorative gradients |
| Gradient borders | 1px solid subtle border |
| Random colour combinations | Pick from `colour-palettes.md` |

## Motion

| Banned | Use instead |
|--------|-------------|
| `transform: translateX(2px)` on nav hover | Background colour change only |
| Bounce / spring animations | `100–200ms ease` |
| Scale on card hover | Subtle border or shadow change |
| Entrance animations on page load | No animation, or simple opacity fade |

## Specific HTML Patterns — Hard No

```html
<!-- BANNED: Eyebrow + headline combo -->
<div class="headline">
  <small>Team Command</small>
  <h2>One place to track what matters today.</h2>
  <p>The layout stays strict and readable...</p>
</div>

<!-- BANNED: Small label + strong note -->
<div class="team-note">
  <small>Focus</small>
  <strong>Keep updates brief, blockers visible, and next actions easy to spot.</strong>
</div>

<!-- BANNED: Nav badge -->
<span class="nav-badge">Live</span>

<!-- BANNED: Gradient brand block -->
<div style="background: linear-gradient(135deg, #2a2a2a, #171717)">...</div>

<!-- BANNED: KPI grid as dashboard default -->
<div class="kpi-grid">
  <div class="kpi-card">...</div>
  <div class="kpi-card">...</div>
  <div class="kpi-card">...</div>
</div>
```

## The Rule

**If it feels like the AI default — it is. Pick the harder, cleaner option.**

When in doubt: what would Linear do?
