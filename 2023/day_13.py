from aoc import *


def solve(input_str):
    part1, part2 = 0, 0
    for g in input_str.split("\n\n"):
        p1, p2 = refl(g)
        part1 += p1
        part2 += p2
    return part1, part2


def refl(inp):
    u = [list(l) for l in inp.split("\n")]
    j = [[None for _ in range(len(u))] for _ in range(len(u[0]))]
    for r in range(len(u)):
        for c in range(len(u[r])):
            j[c][r] = u[r][c]

    answer = []
    for gg, k in ((j, 100), (u, 1)):
        for c in range(len(gg[0]) - 1):
            if len(gg[0][c:]) % 2 == 1:
                continue
            if (
                s := sum(1 if a != b else 0 for r in gg for a, b in zip(r[::-1], r[c:]))
            ) <= 2:
                answer.append((s, (((len(gg[0]) - c) // 2 + c) * k)))

            if (
                s := sum(1 if a != b else 0 for r in gg for a, b in zip(r[::-1][c:], r))
            ) <= 2:
                answer.append((s, ((len(gg[0]) - c) // 2) * k))

    answer.sort(key=lambda k: k[0])
    return answer[0][1], answer[1][1]


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (36041, 35915)


if __name__ == "__main__":
    main()
