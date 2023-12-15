#!/usr/bin/python3

from aoc import *


def solve(input_str):
    ss = input_str.strip().split(",")
    part1 = sum(map(hhhh, ss))
    boxes = [list() for _ in range(256)]
    for s in ss:
        if s[-1] == "-":
            key = s[:-1]
            h = hhhh(key)
            b = boxes[h]
            for i in range(len(b) - 1, 0 - 1, -1):
                if b[i][0] == key:
                    b.pop(i)
        else:
            key = s[:-2]
            val = int(s[-1])
            h = hhhh(key)
            b = boxes[h]
            for i in range(len(b)):
                if b[i][0] == key:
                    b[i][1] = val
                    break
            else:
                b.append([key, val])
    part2 = 0
    for i, b in enumerate(boxes):
        for li, l in enumerate(b):
            part2 += (1 + i) * (li + 1) * l[1]
    
    return part1, part2


def hhhh(s):
    h = 0
    for c in map(ord, s):
        h = (h + c) * 17 % 256
    return h


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (509784, 230197)


if __name__ == "__main__":
    main()
