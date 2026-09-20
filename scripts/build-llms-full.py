#!/usr/bin/env python3
"""Regenerate llms-full.txt from canonical context/ sources."""

from __future__ import annotations

from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTEXT = ROOT / "context"
OUTPUT = ROOT / "llms-full.txt"

SECTIONS: list[tuple[str, Path]] = [
    ("AGENT GUIDELINES & PERSONA", CONTEXT / "agent-guidelines.md"),
    ("TARGET ROLES & CASE-STUDY MAPPING", CONTEXT / "roles-targeted.md"),
    ("DOCUMENTED SKILL BOUNDARIES", CONTEXT / "limitations.md"),
    ("CURRICULUM VITAE", CONTEXT / "cv.md"),
    ("PORTFOLIO & CASE STUDIES", CONTEXT / "portfolio.md"),
    ("SKILLS & COMPETENCY MATRIX", CONTEXT / "skills.json"),
    ("JSON RESUME", CONTEXT / "resume.json"),
    ("TECHNICAL WRITING INDEX", CONTEXT / "writings.json"),
]


def build() -> str:
    parts: list[str] = [
        "# COMPLETE AGENT CONTEXT (vperezb)",
        "",
        "> Auto-generated unified context for LLM prompt injection.",
        f"> Generated: {date.today().isoformat()}",
        "> Source of truth: context/ files. Regenerate with: python scripts/build-llms-full.py",
        "",
    ]

    for index, (title, path) in enumerate(SECTIONS, start=1):
        content = path.read_text(encoding="utf-8").strip()
        parts.extend(
            [
                "=" * 80,
                f"PART {index}: {title}",
                f"Source: {path.relative_to(ROOT).as_posix()}",
                "=" * 80,
                "",
                content,
                "",
            ]
        )

    parts.extend(
        [
            "=" * 80,
            "PART 9: AGENT PROMPT TEMPLATES",
            "Source: prompts/",
            "=" * 80,
            "",
            (ROOT / "prompts" / "job-application-agent.md").read_text(encoding="utf-8").strip(),
            "",
            (ROOT / "prompts" / "coding-assistant-agent.md").read_text(encoding="utf-8").strip(),
            "",
        ]
    )

    return "\n".join(parts)


def main() -> None:
    OUTPUT.write_text(build(), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)} ({OUTPUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
