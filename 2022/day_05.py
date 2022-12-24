#!/usr/bin/python3

from aoc import *

def solve(input_str):
    stacks, instr = input_str.split('\n\n')

    rows = [r[1::4] for r in stacks.split('\n')[::-1]]
    cols = lmap(list, zip(*rows))

    for c in cols:
        c.pop(0)
        while c[-1] == ' ':
            c.pop()

    cols1 = cols
    cols2 = lmap(list, cols)

    for l in lines(instr):
        n, fr, to = ints(l)
        for _ in range(n):
            cols1[to-1].append(cols1[fr-1].pop())

        cols2[to-1] += cols2[fr-1][-n:]
        cols2[fr-1][-n:] = []



    part1 = ''.join(c[-1] for c in cols1)
    part2 = ''.join(c[-1] for c in cols2)
    return (part1, part2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == ('TLFGBZHCN', 'QRQFHFWCL')

if __name__ == '__main__':
    main()


