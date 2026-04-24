#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Bootstrap the .noootwo harness into a target project."
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target project directory. Defaults to the current working directory.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing files inside the destination .noootwo directory.",
    )
    args = parser.parse_args()

    package_root = Path(__file__).resolve().parent.parent
    source_root = package_root / "assets" / "noootwo-harness-template"
    target_root = Path(args.target).resolve()
    destination_root = target_root / ".noootwo"

    if not source_root.exists():
        raise SystemExit(f"Template source not found: {source_root}")

    copied: list[Path] = []
    skipped: list[Path] = []

    for source_path in sorted(source_root.rglob("*")):
        relative_path = source_path.relative_to(source_root)
        destination_path = destination_root / relative_path

        if source_path.is_dir():
            destination_path.mkdir(parents=True, exist_ok=True)
            continue

        destination_path.parent.mkdir(parents=True, exist_ok=True)
        if destination_path.exists() and not args.force:
            skipped.append(destination_path)
            continue

        shutil.copy2(source_path, destination_path)
        copied.append(destination_path)

    print(f"Bootstrapped {destination_root}")
    if copied:
        print("Copied:")
        for path in copied:
            print(f"  - {path}")
    if skipped:
        print("Skipped existing files:")
        for path in skipped:
            print(f"  - {path}")
    if skipped and not args.force:
        print("Re-run with --force to overwrite existing files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
