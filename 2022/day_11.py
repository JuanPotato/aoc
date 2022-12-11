#!/usr/bin/python3

from aoc import *
from typing import List, Any
import math
from dataclasses import dataclass
import re


def solve(input_str):
    monks = re.findall(r'Monkey \d+:\D+([\d, ]+)[^=]+= (.+)\D+(\d+)\D+(\d+)\D+(\d+)', input_str)
    template = 'Monkey([{}], lambda old: {}, {}, {}, {})'
    monkeys = [eval(template.format(*m)) for m in monks]

    part1 = monkey_business(monkeys, 20, 3)
    part2 = monkey_business(monkeys, 10000, 1)
    return (part1, part2)


@dataclass
class Monkey:
    starters: List[int]
    op: Any
    div_test: int
    monk_true: int
    monk_false: int

    def reset(self):
        self.items = list(self.starters)
        self.count = 0


def monkey_business(monkeys, rounds, relief_factor):
    crazy = math.lcm(*[m.div_test for m in monkeys])

    for m in monkeys:
        m.reset()

    for _ in range(rounds):
        for m in monkeys:
            while m.items:
                m.count += 1
                w = m.items.pop(0) % crazy
                w = m.op(w)
                w //= relief_factor
                monkeys[m.monk_false if w % m.div_test else m.monk_true].items.append(w)

    count = sorted(m.count for m in monkeys)
    return count[-1] * count[-2]


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (121450, 28244037010)

if __name__ == '__main__':
    main()


