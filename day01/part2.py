from __future__ import annotations
import sys
sys.path.append("/Users/Tom/Documents/aoc2023")
import support
import re

digit_to_num = {"one" : "1", "two" : "2", "three": "3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight": "8", "nine": "9"}


def do_stuff(f: str) -> None:
    s = f.splitlines()
    sum = 0
    for line in s:
        words = re.findall("(?=(" + "|".join(digit_to_num.keys()) + "|\d))" , line)
        sum += int(''.join([d if d.isdigit() else digit_to_num[d] for d in [words[0], words[-1]]]))
    print(sum)    

def main() -> int:
    with open("input.txt") as f:
        do_stuff(f.read())
    return 0

if __name__ == '__main__':
    raise SystemExit(main())

