#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from pathlib import Path


REQUIRED_FILES = [
    Path(".noootwo/directions.md"),
    Path(".noootwo/review.md"),
    Path(".noootwo/design-tokens.md"),
]

DEEP_REQUIRED_FILES = [
    Path(".noootwo/style-discovery.md"),
    Path(".noootwo/reference-board.md"),
]

IMPLEMENTATION_REQUIRED_FILES = [
    Path(".noootwo/specs/active-design.md"),
    Path(".noootwo/plans/active-implementation.md"),
]

STATUS_PENDING_RE = re.compile(r"^Status:\s*pending\b", re.IGNORECASE | re.MULTILINE)
TBD_RE = re.compile(r"(?<!`)\bTBD\b(?!`)")
DECISION_RE = re.compile(r"\b(ready|refine|pivot|needs artifact|not ready)\b", re.IGNORECASE)
READY_DECISION_RE = re.compile(
    r"(^|\n)\s*(?:-\s*)?(?:Decision\s*:\s*)?ready\s*(?:$|\n)",
    re.IGNORECASE,
)
FULL_REDESIGN_TRIGGER_RE = re.compile(
    r"full redesign trigger\s*:\s*(?:yes|true|triggered|full redesign)",
    re.IGNORECASE,
)
USER_SELECTED_DIRECTION_RE = re.compile(
    r"^\s*-?\s*user selected direction\s*:\s*(?!\s*(?:not selected yet|not selected|pending|none|no)\s*$).+\S",
    re.IGNORECASE | re.MULTILINE,
)
USER_DECISION_REQUIRED_RE = re.compile(
    r"decision required before implementation\s*:\s*(?:yes|true|required)",
    re.IGNORECASE,
)
USER_SELECTED_OPTION_RE = re.compile(
    r"^\s*-?\s*user selected option\s*:\s*(?!\s*(?:TBD|not selected yet|not selected|pending|none|no|n/a|na)\s*$).+\S",
    re.IGNORECASE | re.MULTILINE,
)
USER_DELEGATED_CHOICE_RE = re.compile(
    r"^\s*-?\s*user delegated choice to agent\s*:\s*(?:yes|true|delegated)\s*$",
    re.IGNORECASE | re.MULTILINE,
)
APPROVED_BY_USER_RE = re.compile(
    r"approved by user\s*:\s*(?:yes|true|approved)",
    re.IGNORECASE,
)
PLAN_APPROVED_RE = re.compile(
    r"user approved or delegated implementation plan\s*:\s*(?:yes|true|approved|delegated)",
    re.IGNORECASE,
)

REQUIRED_REVIEW_SECTIONS = [
    "artifact evidence",
    "typography craft",
    "responsive visual gate",
    "decision",
    "return action",
]

DEEP_REVIEW_SECTIONS = [
    "spike comparison",
]

DEEP_STYLE_SECTIONS = [
    "source accessibility",
    "source evidence",
    "evidence levels",
    "rejected surfaces",
    "fit scores",
]

DEEP_DIRECTIONS_SECTIONS = [
    "full redesign checkpoint",
    "user decision gate",
    "user selected direction",
    "design-spec delta",
]


def validate_file(target_root: Path, relative_path: Path) -> list[str]:
    path = target_root / relative_path
    errors: list[str] = []

    if not path.exists():
        return [f"{relative_path} is missing"]

    content = path.read_text(encoding="utf-8")
    if STATUS_PENDING_RE.search(content):
        errors.append(f"{relative_path} is still Status: pending")
    if TBD_RE.search(content):
        errors.append(f"{relative_path} contains unresolved TBD placeholders")
    if not content.strip():
        errors.append(f"{relative_path} is empty")

    return errors


def missing_sections(content: str, sections: list[str], path_label: str) -> list[str]:
    lower_content = content.lower()
    return [
        f"{path_label} is missing {section}"
        for section in sections
        if section not in lower_content
    ]


def validate_review(target_root: Path, allow_non_ready: bool, deep_mode: bool) -> list[str]:
    review_path = target_root / ".noootwo/review.md"
    if not review_path.exists():
        return []

    content = review_path.read_text(encoding="utf-8")
    errors: list[str] = []

    errors.extend(
        missing_sections(content, REQUIRED_REVIEW_SECTIONS, ".noootwo/review.md")
    )
    if deep_mode:
        errors.extend(
            missing_sections(content, DEEP_REVIEW_SECTIONS, ".noootwo/review.md")
        )

    if not DECISION_RE.search(content):
        errors.append(".noootwo/review.md does not record a review decision")
    elif not allow_non_ready and not READY_DECISION_RE.search(content):
        errors.append(".noootwo/review.md decision is not ready")

    return errors


def validate_directions(target_root: Path, deep_mode: bool) -> list[str]:
    directions_path = target_root / ".noootwo/directions.md"
    if not directions_path.exists():
        return []

    content = directions_path.read_text(encoding="utf-8")
    errors: list[str] = []

    if deep_mode:
        errors.extend(
            missing_sections(content, DEEP_DIRECTIONS_SECTIONS, ".noootwo/directions.md")
        )

    if FULL_REDESIGN_TRIGGER_RE.search(content) and not USER_SELECTED_DIRECTION_RE.search(content):
        errors.append(
            ".noootwo/directions.md marks full redesign but does not record User selected direction"
        )
    if (
        USER_DECISION_REQUIRED_RE.search(content)
        and not USER_SELECTED_OPTION_RE.search(content)
        and not USER_DELEGATED_CHOICE_RE.search(content)
    ):
        errors.append(
            ".noootwo/directions.md requires a user decision but does not record User selected option or delegated choice"
        )

    return errors


def validate_deep_mode(target_root: Path) -> list[str]:
    errors: list[str] = []

    for relative_path in DEEP_REQUIRED_FILES:
        errors.extend(validate_file(target_root, relative_path))

    style_path = target_root / ".noootwo/style-discovery.md"
    if style_path.exists():
        style_content = style_path.read_text(encoding="utf-8")
        errors.extend(
            missing_sections(style_content, DEEP_STYLE_SECTIONS, ".noootwo/style-discovery.md")
        )

    reference_path = target_root / ".noootwo/reference-board.md"
    if reference_path.exists():
        reference_content = reference_path.read_text(encoding="utf-8")
        errors.extend(
            missing_sections(
                reference_content,
                ["source url or artifact", "borrowed mechanism", "selected mechanisms"],
                ".noootwo/reference-board.md",
            )
        )

    return errors


def validate_implementation_gate(target_root: Path) -> list[str]:
    errors: list[str] = []

    for relative_path in IMPLEMENTATION_REQUIRED_FILES:
        errors.extend(validate_file(target_root, relative_path))

    spec_path = target_root / ".noootwo/specs/active-design.md"
    if spec_path.exists():
        spec_content = spec_path.read_text(encoding="utf-8")
        errors.extend(
            missing_sections(
                spec_content,
                [
                    "approval",
                    "design spec snapshot",
                    "implementation contract",
                    "artifact and review contract",
                ],
                ".noootwo/specs/active-design.md",
            )
        )
        if not APPROVED_BY_USER_RE.search(spec_content):
            errors.append(".noootwo/specs/active-design.md is not approved by user")

    plan_path = target_root / ".noootwo/plans/active-implementation.md"
    if plan_path.exists():
        plan_content = plan_path.read_text(encoding="utf-8")
        errors.extend(
            missing_sections(
                plan_content,
                [
                    "implementation steps",
                    "token mapping tasks",
                    "component tasks",
                    "artifact and verification plan",
                    "completion criteria",
                ],
                ".noootwo/plans/active-implementation.md",
            )
        )
        if not PLAN_APPROVED_RE.search(plan_content):
            errors.append(
                ".noootwo/plans/active-implementation.md is not approved or delegated"
            )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate that Noootwo design deliverables are ready for handoff."
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target project directory. Defaults to the current working directory.",
    )
    parser.add_argument(
        "--allow-non-ready",
        action="store_true",
        help="Only validate that required Noootwo files are complete; do not require the review decision to be ready.",
    )
    parser.add_argument(
        "--deep-mode",
        action="store_true",
        help="Also validate deep-mode style discovery, reference board, and spike comparison evidence.",
    )
    parser.add_argument(
        "--implementation-gate",
        action="store_true",
        help="Also require an approved design spec and approved/delegated implementation plan.",
    )
    args = parser.parse_args()

    target_root = Path(args.target).resolve()
    errors: list[str] = []

    for relative_path in REQUIRED_FILES:
        errors.extend(validate_file(target_root, relative_path))

    errors.extend(validate_directions(target_root, args.deep_mode))
    errors.extend(validate_review(target_root, args.allow_non_ready, args.deep_mode))
    if args.deep_mode:
        errors.extend(validate_deep_mode(target_root))
    if args.implementation_gate:
        errors.extend(validate_implementation_gate(target_root))

    if errors:
        print("Noootwo readiness validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("Noootwo readiness validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
