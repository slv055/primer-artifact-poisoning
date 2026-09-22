"""Stand-in for pyrefly's scripts/primer_classifier/__main__.py."""
import argparse
import json


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--diff-file", required=True)
    args = ap.parse_args()
    with open(args.diff_file) as f:
        lines = [l for l in f if l.startswith("+")]
    print(json.dumps({"new_errors": len(lines)}, indent=2))


if __name__ == "__main__":
    main()
