#!/usr/bin/python3

from aoc import *

def solve(input_str):
    p1, p2 = 0, 0

    for r in parse_list(input_str):
        com = set(r[:len(r)//2]) & set(r[len(r)//2:])
        for k in com:
            p1 += ord(k) - (ord('A') - 27 if k.isupper() else ord('a') - 1)

    for r1, r2, r3 in chunk(parse_list(input_str), 3):
        com = set(r1) & set(r2) & set(r3)
        for k in com:
            p2 += ord(k) - (ord('A') - 27 if k.isupper() else ord('a') - 1)

    return (p1, p2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (7908, 2838)

if __name__ == '__main__':
    main()


