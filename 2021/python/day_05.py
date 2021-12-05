from aoc import *
from collections import Counter

def solve(input_str):
    straight = Counter()
    diag = Counter()

    for (ax, ay), _, (bx, by) in parse_list(input_str, eval, str, eval):
        x0, x1, xs = (ax, bx + 1, 1) if ax < bx else (ax, bx - 1, -1)
        y0, y1, ys = (ay, by + 1, 1) if ay < by else (ay, by - 1, -1)

        if ax == bx or ay == by:
            straight.update((x, y) for y in range(y0, y1, ys) for x in range(x0, x1, xs))

        else:
            diag.update(zip(range(x0,x1,xs), range(y0,y1,ys)))

    part1 = sum(1 for v in straight.values() if v >= 2)
    part2 = sum(1 for v in (straight + diag).values() if v >= 2)

    return (part1, part2)


if __name__ == '__main__':
    print(solve(get_input(__file__)))
