# Stack Recipes

These are starting compositions, not mandatory dependencies. Preserve an established project stack when it already works.

## Astro product site

Use this when the product needs fast static pages, strong SEO and a few interactive areas.

- **Astro** owns routing, page composition and static output.
- **React islands** are reserved for controls that need client state. Do not hydrate headings, cards or copy.
- **Tailwind CSS v4** provides tokens, layout and responsive constraints.
- **Base UI / coss ui** supplies accessible primitives for menus, dialogs, tabs, fields and other behaviour-heavy controls.
- **Inter** carries interface and body copy. **Geist Mono** is useful for code, identifiers and technical values.
- **Lucide** provides restrained, consistent icons. Use icons to aid recognition, never to decorate every heading.

Good fit: documentation products, developer tools, self-hosted software sites and content-led product pages.

## Astro operational dashboard

Use this when the screen is mostly live data and navigation, with little need for a full React application.

- Keep the shell and routes in **Astro**.
- Use plain browser JavaScript for straightforward fetch/render cycles.
- Add a React island only when a component has enough local state or interaction to justify it.
- Keep data formatting, stale-state handling, empty states and error states close to the renderer.
- Draw simple sparklines locally when they communicate real history. Do not add a charting dependency for three lines and an axis-free trend.
- Use the same restrained tokens and type stack as the product site so related surfaces feel like one family without becoming identical.

Good fit: pool dashboards, service status pages, admin consoles and operational readouts.

## Component choice order

1. Reuse the project's existing component system.
2. Use a native HTML element when it already has the right semantics.
3. Use Base UI or coss ui for behaviour-heavy accessible primitives.
4. Use shadcn/ui when starting a React application without an established system.
5. Write a custom component only when the product requirement is genuinely specific.

## Visual composition

- Establish a small token set before composing pages: background, surface, border, text, muted text, accent, success, warning and danger.
- Use one main sans family and at most one mono family.
- Keep radii in the 6–12px range and shadows nearly invisible.
- Let real product screenshots, tables, forms and live data carry the page.
- Build hierarchy with spacing, type weight and borders before adding colour.
- Treat mobile as a layout change, not a desktop page squeezed narrower.

## Acceptance checks

- The page still makes sense with every decorative asset removed.
- Every chart, metric and badge answers a real user question.
- Interactive elements have keyboard, focus and disabled states.
- Real content has been tested for overflow at desktop and mobile widths.
- Static pages ship without unnecessary client JavaScript.
- Screenshots show the real product and have dimensions, useful alt text and appropriate loading priority.
