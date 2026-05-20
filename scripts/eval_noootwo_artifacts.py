#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from pathlib import Path


PENDING_RE = re.compile(r"^Status:\s*pending\b", re.IGNORECASE | re.MULTILINE)
TBD_RE = re.compile(r"(?<!`)\bTBD\b(?!`)")
FULL_REDESIGN_RE = re.compile(r"full redesign trigger\s*:\s*(?:yes|true|triggered)", re.IGNORECASE)
USER_SELECTED_DIRECTION_RE = re.compile(
    r"^\s*-?\s*user selected direction\s*:\s*(?!\s*(?:TBD|not selected yet|not selected|pending|none|no)\s*$).+\S",
    re.IGNORECASE | re.MULTILINE,
)
USER_DECISION_REQUIRED_RE = re.compile(r"decision required before implementation\s*:\s*(?:yes|true|required)", re.IGNORECASE)
USER_SELECTED_OPTION_RE = re.compile(
    r"^\s*-?\s*user selected option\s*:\s*(?!\s*(?:TBD|not selected yet|not selected|pending|none|no|n/a|na)\s*$).+\S",
    re.IGNORECASE | re.MULTILINE,
)
USER_DELEGATED_RE = re.compile(r"^\s*-?\s*user delegated choice to agent\s*:\s*(?:yes|true|delegated)\s*$", re.IGNORECASE | re.MULTILINE)
APPROVED_RE = re.compile(r"approved by user\s*:\s*(?:yes|true|approved)", re.IGNORECASE)
PLAN_APPROVED_RE = re.compile(r"user approved or delegated implementation plan\s*:\s*(?:yes|true|approved|delegated)", re.IGNORECASE)
ARTIFACT_RE = re.compile(r"(artifact reviewed|screenshot|preview|simulator|device|visual proof|url)\s*:\s*(?!\s*(?:TBD|pending|none|no)\s*$).+", re.IGNORECASE)


def read(root: Path, relative: str) -> str:
    path = root / relative
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def has_unresolved(content: str) -> bool:
    return bool(PENDING_RE.search(content) or TBD_RE.search(content) or not content.strip())


def require(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def eval_full_redesign(root: Path) -> list[str]:
    errors: list[str] = []
    directions = read(root, ".noootwo/directions.md")
    require(errors, bool(directions), "missing .noootwo/directions.md")
    require(errors, bool(FULL_REDESIGN_RE.search(directions)), "full redesign trigger not recorded")
    require(errors, bool(USER_SELECTED_DIRECTION_RE.search(directions)), "user selected direction not recorded")
    return errors


def eval_user_decision(root: Path) -> list[str]:
    errors: list[str] = []
    directions = read(root, ".noootwo/directions.md")
    if USER_DECISION_REQUIRED_RE.search(directions):
        require(
            errors,
            bool(USER_SELECTED_OPTION_RE.search(directions) or USER_DELEGATED_RE.search(directions)),
            "required user decision lacks selected option or delegation",
        )
    return errors


def eval_influence(root: Path) -> list[str]:
    errors: list[str] = []
    discovery = read(root, ".noootwo/style-discovery.md")
    board = read(root, ".noootwo/reference-board.md")
    combined = f"{discovery}\n{board}".lower()
    require(errors, "influence shortlist" in discovery.lower(), "influence shortlist missing")
    require(errors, "do not copy" in combined, "do-not-copy boundary missing")
    require(errors, "translation" in combined, "design-system translation missing")
    require(errors, "preservation contract" in combined, "preservation contract missing")
    require(errors, "risk" in combined or "rejected mimicry" in combined, "mimicry/risk record missing")
    require(errors, "in the style of" not in combined, "direct 'in the style of' wording found")
    return errors


def eval_implementation(root: Path) -> list[str]:
    errors: list[str] = []
    spec = read(root, ".noootwo/specs/active-design.md")
    plan = read(root, ".noootwo/plans/active-implementation.md")
    require(errors, bool(spec), "missing approved design spec")
    require(errors, bool(plan), "missing implementation plan")
    require(errors, not has_unresolved(spec), "approved design spec unresolved")
    require(errors, not has_unresolved(plan), "implementation plan unresolved")
    require(errors, bool(APPROVED_RE.search(spec)), "approved design spec not approved by user")
    require(errors, bool(PLAN_APPROVED_RE.search(plan)), "implementation plan not approved or delegated")
    require(errors, "preservation contract" in spec.lower(), "approved design spec preservation contract missing")
    require(errors, "preservation tasks" in plan.lower(), "implementation plan preservation tasks missing")
    return errors


def eval_ready(root: Path) -> list[str]:
    errors: list[str] = []
    for relative in [
        ".noootwo/directions.md",
        ".noootwo/review.md",
        ".noootwo/design-tokens.md",
    ]:
        content = read(root, relative)
        require(errors, bool(content), f"missing {relative}")
        require(errors, not has_unresolved(content), f"{relative} unresolved")
    review = read(root, ".noootwo/review.md")
    require(errors, bool(ARTIFACT_RE.search(review)), "artifact/screenshot/preview evidence missing")
    require(errors, "decision" in review.lower(), "review decision missing")
    require(errors, "preservation contract" in review.lower(), "review preservation contract missing")
    return errors


SCENARIOS = {
    "full-redesign": eval_full_redesign,
    "user-decision": eval_user_decision,
    "influence": eval_influence,
    "implementation": eval_implementation,
    "ready": eval_ready,
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate Noootwo artifact structure for workflow pressure tests.")
    parser.add_argument("target", nargs="?", default=".", help="Target project directory.")
    parser.add_argument(
        "--scenario",
        choices=sorted(SCENARIOS) + ["all"],
        default="all",
        help="Scenario to evaluate. Defaults to all.",
    )
    args = parser.parse_args()

    root = Path(args.target).resolve()
    scenario_names = sorted(SCENARIOS) if args.scenario == "all" else [args.scenario]
    all_errors: list[str] = []

    for name in scenario_names:
        errors = SCENARIOS[name](root)
        if errors:
            all_errors.extend([f"{name}: {error}" for error in errors])

    if all_errors:
        print("Noootwo artifact eval failed:")
        for error in all_errors:
            print(f"  - {error}")
        return 1

    print("Noootwo artifact eval passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
