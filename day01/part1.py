from __future__ import annotations
import sys
sys.path.append("/Users/Tom/Documents/aoc2023")
import support


def do_stuff(f: str) -> None:
    s = f.splitlines()

    lol = []
    for line in s:
        tmp = []
        for char in line:
            if char.isdigit():
                tmp.append(char)
        lol.append(tmp)

    sum = 0 
    for line in lol:
        if len(line) > 1:
            tmp_num = int(line[0] + line[-1])
        else:
            tmp_num = int(line[0] + line[0])
        sum += tmp_num
    print(sum)    




def main() -> int:
    with open("input.txt") as f:
        do_stuff(f.read())
    return 0

if __name__ == '__main__':
    raise SystemExit(main())

