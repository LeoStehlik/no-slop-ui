# ClawHub review — 2026-11-07

Reviewed the published scanner findings against the repository. The skill’s normal behaviour is specified in Markdown; a bundled repository validator is maintainer tooling, not a replacement implementation. File validation is local, explicit and does not transmit content. The skill now makes that distinction explicit where applicable.

Scanner claims that rewriting prose, using example locale strings, or following an explicit design/documentation request are autonomous destructive operations do not match the source. Those findings were not “fixed” by disabling the product or adding generic approval prompts. Source content is data; external publication still follows the user’s task.
