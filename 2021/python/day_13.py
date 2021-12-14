#!/usr/bin/python3

from aoc import *

def solve(input_str):
    dots, instr = input_str.split('\n\n')

    dots = set(parse_list(dots, eval))
    instr = list(parse_list(instr, str, int, sep='='))

    for i,(axis,val) in enumerate(instr):
        dots = fold(dots, axis[-1], val)
        if i == 0:
            part1 = len(dots)

    xx, yy = max(e[0] for e in dots), max(e[1] for e in dots)
    part2 = ''
    for y in range(yy + 1):
        for x in range(xx + 1):
            part2 += ['  ', '██'][(x, y) in dots]
        part2 += '\n'

    return (part1, part2)

def fold(dots, axis, val):
    if axis == 'x':
        t = lambda x,y: (val - (x - val), y) if x > val else (x,y)
    else:
        t = lambda x,y: (x, val - (y - val)) if y > val else (x,y)

    return set(t(x,y) for x,y in dots)


def main():
    answer = solve(get_input(__file__))
    print(answer[0])
    print(answer[1])
    assert answer[0] == 807

if __name__ == '__main__':
    main()

