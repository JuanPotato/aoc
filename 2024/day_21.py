#!/usr/bin/python3

from aoc import *
from math import comb

DIRS = (
    (0, -1),  # ^
    (1, 0),  # >
    (0, 1),  # v
    (-1, 0),  # <
)

# valid coords for numpad
NUMPAD_W = 3
NUMPAD_H = 4
NUMPAD_INVALID = (0, 3)

NUMPAD_LAYOUT = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}

ARROWS_W = 3
ARROWS_H = 2
ARROWS_INVALID = (0, 0)

ARROWS_LAYOUT = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}


def generic_move_dist(src, dst, layout, invalid):
    srcx, srcy = layout[src]
    dstx, dsty = layout[dst]
    dy = dsty - srcy
    dx = dstx - srcx
    ways = comb(abs(dy) + abs(dx), abs(dx))
    if invalid in ((srcx, dsty), (dstx, srcy)):
        ways -= 1
    return (dx, dy)


def numpad_move_dist(src, dst):
    return generic_move_dist(src, dst, NUMPAD_LAYOUT, NUMPAD_INVALID)


def arrows_move_dist(src, dst):
    return generic_move_dist(src, dst, ARROWS_LAYOUT, ARROWS_INVALID)


def solve(input_str: str):
    codes = parse_list(input_str, str)
    part1 = 0
    part2 = 0

    for code in codes:
        l = layer1(code)
        c = make_counter("A" + l)
        for i in range(25):
            if i == 2:
                part1 += sum(c.values()) * int(code[:-1])
            c = layer2v2(c)
        part2 += sum(c.values()) * int(code[:-1])

    return (part1, part2)


def layer1(code: str):
    cur = "A"
    output = ""
    for c in code:
        dx, dy = numpad_move_dist(cur, c)
        if cur in "741" and c in "0A":
            output += ">" * dx
            output += "v" * dy
        elif cur in "0A" and c in "741":
            output += "^" * -dy
            output += "<" * -dx
        else:
            output += "<" * max(0, -dx)
            output += "^" * max(0, -dy)
            output += "v" * max(0, dy)
            output += ">" * max(0, dx)
        output += "A"
        cur = c
    return output


def make_counter(moves):
    counter = Counter()
    for a, b in window(moves, 2):
        counter[(a, b)] += 1
    return counter


def layer2v2(move_counter):
    counter = Counter()
    for move, num in move_counter.items():
        for new_move, new_num in sub_layer2v2(*move).items():
            counter[new_move] += num * new_num
    return counter


def sub_layer2v2(src, dst):
    counter = Counter()
    dx, dy = arrows_move_dist(src, dst)
    output = "A"
    if src in "^A" and dst in "<":
        output += "v" * dy
        output += "<" * -dx
    elif src in "<" and dst in "^A":
        output += ">" * dx
        output += "^" * -dy
    else:
        output += "<" * max(0, -dx)
        output += "^" * max(0, -dy)
        output += "v" * max(0, dy)
        output += ">" * max(0, dx)
    output += "A"
    for a, b in window(output, 2):
        counter[(a, b)] += 1
    return counter


def layer2(code: str):
    dists = Counter()
    cur = "A"
    output = ""
    for c in code:
        dists[(cur, c)] += 1
        dx, dy = arrows_move_dist(cur, c)
        if cur in "^A" and c in "<":
            output += "v" * dy
            output += "<" * -dx
        elif cur in "<" and c in "^A":
            output += ">" * dx
            output += "^" * -dy
        else:
            output += "<" * max(0, -dx)
            output += "^" * max(0, -dy)
            output += "v" * max(0, dy)
            output += ">" * max(0, dx)
        output += "A"
        cur = c
    return output


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (105458, 129551515895690)


if __name__ == "__main__":
    main()
