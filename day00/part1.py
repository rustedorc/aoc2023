from __future__ import annotations
import sys
sys.path.append("/Users/Tom/Documents/aoc2023")
import support


def do_stuff(f: str) -> None:
    ...


def main() -> int:
    with open("input.txt") as f:
        do_stuff(f.read())


    return 0

if __name__ == '__main__':
    raise SystemExit(main())

