#!/usr/bin/python3

from aoc import *

def solve(input_str):
    return (part1(input_str), part2(input_str))

def parse(l):
    g,l = l.split(':')
    id = ints(g)[0]
    sets = [{k:v for k,v in zip(words(s),ints(s))} for s in l.split(';')]
    return id,sets


def part1(input_str):
    total = 0
    for b in input_str.split('\n'):
        i,s = parse(b)
        total += all(all(bag[k] >= v for k,v in ss.items()) for ss in s) * i
    return total


def part2(input_str):
    total = 0
    for b in input_str.split('\n'):
        i,s = parse(b)
        m = {}
        for ss in s:
            for k,v in ss.items():
                m[k] = max(m.get(k,0), v)

        power = 1
        for k in m.values():
            power *= k
        total += power
    return total


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (2265, 64097)

if __name__ == '__main__':
    main()


