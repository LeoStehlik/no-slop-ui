#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["README.md", "SKILL.md", "LICENSE"]
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def iter_markdown_files() -> list[Path]:
    paths = [ROOT / "README.md", ROOT / "SKILL.md"]
    for dirname in ("references", "examples", "docs"):
        folder = ROOT / dirname
        if folder.exists():
            paths.extend(sorted(folder.rglob("*.md")))
    return [path for path in paths if path.exists()]


def check_required_files() -> None:
    for rel in REQUIRED:
        path = ROOT / rel
        if not path.exists():
            fail(f"missing required file: {rel}")
        if path.stat().st_size == 0:
            fail(f"required file is empty: {rel}")


def check_local_links() -> None:
    for path in iter_markdown_files():
        text = path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(1).strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"link escapes repo in {path.relative_to(ROOT)}: {match.group(1)}")
            if not resolved.exists():
                fail(f"broken local link in {path.relative_to(ROOT)}: {match.group(1)}")


def check_skill_metadata() -> None:
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if skill.startswith("---") and skill.count("---") >= 2:
        metadata = skill.split("---", 2)[1]
    else:
        metadata = skill
    if "description:" not in metadata:
        fail("SKILL.md must include a description")


def main() -> int:
    check_required_files()
    check_local_links()
    check_skill_metadata()
    print("skill repo validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
