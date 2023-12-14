from aoc import *
import functools


def solve(input_str):
    part1 = 0
    part2 = 0
    for l in input_str.split("\n"):
        rec, nums = l.split(" ")
        nums = tuple(map(int, nums.split(",")))
        part1 += ways("." + rec + ".", None, nums)
        part2 += ways("." + "?".join([rec] * 5) + ".", None, nums * 5)

    return part1, part2


@functools.cache
def ways(s, n, ns):
    if not ns and not n:
        return "#" not in s
    if not s:
        return not ns and not n

    match s[0], n, ns:
        case "#", 0, _:
            return 0
        case "#", n, ns:
            if n == None:
                n, *ns = ns
            return ways(s[1:], n - 1, tuple(ns))

        case ".", n, ns if n:
            return 0
        case ".", _, ns:
            return ways(s[1:], None, ns)

        case "?", 0, ns:
            return ways(s[1:], None, ns)
        case "?", n, ns if n:
            return ways(s[1:], n - 1, ns)
        case "?", n, ns:
            return ways(f"#{s[1:]}", n, ns) + ways(f".{s[1:]}", n, ns)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (8270, 204640299929836)


if __name__ == "__main__":
    main()
