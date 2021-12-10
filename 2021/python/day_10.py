#!/usr/bin/python3

from aoc import *

def solve(input_str):
    lines = list(parse_list(input_str, str))
    part1 = 0
    auto_scores = []

    braces = { '(':')', '[':']', '{':'}', '<':'>'}
    illegal_points = {')':3, ']':57, '}':1197, '>':25137}
    closing_points = {')':1, ']':2, '}':3, '>':4}

    for l in lines:
        s = []
        corrupt = False
        for o in l:
            if o in braces:
                s.append(o)
            else:
                c = s.pop()
                if o != braces[c]:
                    part1 += illegal_points[o]
                    corrupt = True
                    break

        if corrupt:
            continue

        auto_scores.append(reduce(lambda a,x: a*5+closing_points[braces[x]], s[::-1], 0))

    auto_scores.sort()
    return (part1, auto_scores[len(auto_scores) // 2])


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (243939, 2421222841)

if __name__ == '__main__':
    main()

