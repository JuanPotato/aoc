#!/usr/bin/python3

from aoc import *
import re

def solve(input_str):
    x = 1
    c = 0
    signal = []
    crt = [[' ' for _ in range(40)] for _ in range(6)]
    def cycle():
        row, col = divmod(c - 1, 40)
        if abs(col - x) <= 1:
            crt[row][col] = '█'
        signal.append(x * c)

    for l in lines(input_str):
        if l == "noop":
            c += 1
            cycle()
        else:
            c += 1
            cycle()
            c += 1
            cycle()
            x += ints(l)[0]

    part1 = sum(signal[i-1] for i in range(20, 221, 40))
    part2 = '\n'.join(''.join(r) for r in crt)
    return (part1, part2)


def main():
    answer = solve(get_input(__file__))
    print(answer[0])
    print(answer[1])
    assert answer[0] == 13680

if __name__ == '__main__':
    main()


