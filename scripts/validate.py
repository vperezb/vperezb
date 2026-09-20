#!/usr/bin/env python3
"""Pre-commit validation for vperezb context repo."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTEXT = ROOT / "context"

REQUIRED_CONTEXT = [
    "agent-guidelines.md",
    "roles-targeted.md",
    "limitations.md",
    "cv.md",
    "portfolio.md",
    "skills.json",
    "resume.json",
    "writings.json",
]

JSON_FILES = ["skills.json", "resume.json", "writings.json"]

LINK_SOURCES = ["README.md", "llms.txt"]

CANONICAL_PROJECTS = {
    "faciliteacoches.com",
    "bcnmarket",
    "bonusconsum",
    "google-api-support",
    "libripolis.com",
    "bibliodetect",
    "aws-ip-change-tracker",
    "Tiendeo Mobile App",
    "Facilitea",
}


def error(msg: str) -> None:
    print(f"ERROR: {msg}")


def warn(msg: str) -> None:
    print(f"WARN:  {msg}")


def ok(msg: str) -> None:
    print(f"OK:    {msg}")


def check_required_files() -> bool:
    passed = True
    for name in REQUIRED_CONTEXT:
        path = CONTEXT / name
        if path.is_file():
            ok(f"found context/{name}")
        else:
            error(f"missing context/{name}")
            passed = False
    for name in ["llms.txt", "prompts/job-application-agent.md", "prompts/coding-assistant-agent.md"]:
        path = ROOT / name
        if path.is_file():
            ok(f"found {name}")
        else:
            error(f"missing {name}")
            passed = False
    return passed


def check_json_files() -> bool:
    passed = True
    for name in JSON_FILES:
        path = CONTEXT / name
        try:
            json.loads(path.read_text(encoding="utf-8"))
            ok(f"{name} is valid JSON")
        except json.JSONDecodeError as exc:
            error(f"{name} invalid JSON: {exc}")
            passed = False
    return passed


def check_relative_links() -> bool:
    passed = True
    pattern = re.compile(r"\]\((\.[^)#]+)")
    for source in LINK_SOURCES:
        text = (ROOT / source).read_text(encoding="utf-8")
        for match in pattern.finditer(text):
            target = ROOT / match.group(1)
            if target.is_file():
                ok(f"{source} -> {match.group(1)}")
            else:
                error(f"{source} broken link: {match.group(1)}")
                passed = False
    return passed


def check_llms_full_sync() -> bool:
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "build_llms_full", ROOT / "scripts" / "build-llms-full.py"
    )
    if spec is None or spec.loader is None:
        error("could not load scripts/build-llms-full.py")
        return False
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    build = module.build

    output = ROOT / "llms-full.txt"
    if not output.is_file():
        error("llms-full.txt missing — run: python scripts/build-llms-full.py")
        return False

    current = output.read_text(encoding="utf-8")
    regenerated = build()
    if current == regenerated:
        ok("llms-full.txt is in sync with context/")
        return True

    error("llms-full.txt is stale — run: python scripts/build-llms-full.py")
    return False


def check_resume_privacy() -> bool:
    resume = json.loads((CONTEXT / "resume.json").read_text(encoding="utf-8"))
    basics = resume.get("basics", {})
    passed = True
    for field in ("email", "phone"):
        value = basics.get(field, "")
        if value:
            warn(f"resume.json basics.{field} is set — confirm intentional before publishing")
            passed = False
        else:
            ok(f"resume.json basics.{field} is empty (private)")
    return passed


def check_project_coverage() -> bool:
    """Ensure key projects appear in canonical source files."""
    sources = {
        "portfolio.md": (CONTEXT / "portfolio.md").read_text(encoding="utf-8"),
        "cv.md": (CONTEXT / "cv.md").read_text(encoding="utf-8"),
        "llms.txt": (ROOT / "llms.txt").read_text(encoding="utf-8"),
    }
    passed = True
    for project in sorted(CANONICAL_PROJECTS):
        hits = [name for name, text in sources.items() if project.lower() in text.lower()]
        if hits:
            ok(f"'{project}' referenced in {', '.join(hits)}")
        else:
            warn(f"'{project}' not found in portfolio.md, cv.md, or llms.txt")
            passed = False
    return passed


def main() -> int:
    checks = [
        ("Required files", check_required_files),
        ("JSON validity", check_json_files),
        ("Relative links", check_relative_links),
        ("Resume privacy", check_resume_privacy),
        ("Project coverage", check_project_coverage),
        ("llms-full.txt sync", check_llms_full_sync),
    ]

    print("Validating vperezb context repo\n")
    results = [fn() for _, fn in checks]
    print()
    if all(results):
        print("All checks passed.")
        return 0
    print("Some checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
