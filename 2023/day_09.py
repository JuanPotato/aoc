from aoc import *


def solve(input_str):
    data = parse_grid(input_str, int)
    part1 = sum(extrapolate(l) for l in data)
    part2 = sum(extrapolate(l[::-1]) for l in data)
    return part1, part2


def extrapolate(l):
    gens = [l]
    while not all(e == 0 for e in gens[-1]):
        gens.append([gens[-1][i + 1] - gens[-1][i] for i in range(len(gens[-1]) - 1)])
    gens[-1].append(0)
    for i in range(len(gens) - 2, 0 - 1, -1):
        gens[i].append(gens[i][-1] + gens[i + 1][-1])
    return gens[0][-1]


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (1861775706, 1082)


if __name__ == "__main__":
    main()
