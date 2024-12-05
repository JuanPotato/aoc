#!/usr/bin/python3

from aoc import *
import numpy as np


def solve(input_str: str):
    rules_str, pages = input_str.strip().split("\n\n")
    rules = defaultdict(set)

    for r in parse_grid(rules_str, int, "\n", r"\|"):
        rules[int(r[0])].add(int(r[1]))

    pages = parse_grid(pages, int, "\n", ",")

    part1 = 0
    part2 = 0
    for page in pages:
        if valid(rules, page):
            part1 += page[len(page) // 2]
        else:
            new_page = sort_page(rules, page)
            part2 += new_page[len(new_page) // 2]

    return part1, part2


def valid(rules, page):
    for i in range(len(page)):
        pre = page[i]
        for j in range(i, len(page)):
            post = page[j]
            if pre in rules[post]:
                return False
    return True


def sort_page(rules, page):
    page = list(page)
    made_change = True
    while made_change:
        made_change = False
        for i in range(len(page)):
            pre = page[i]
            for j in range(i, len(page)):
                post = page[j]
                if pre in rules[post]:
                    # bubble sort
                    page[j], page[i] = page[i], page[j]
                    made_change = True
                    break
            else:
                continue
        else:
            continue

    return page


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (5991, 5479)


if __name__ == "__main__":
    main()
