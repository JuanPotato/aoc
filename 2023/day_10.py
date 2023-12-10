from aoc import *


def solve(input_str):
    g = [list(l) for l in input_str.split("\n")]
    pipes = {
        "|": [(0, 1), (0, -1)],
        "-": [(1, 0), (-1, 0)],
        "L": [(0, -1), (1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(0, 1), (-1, 0)],
        "F": [(0, 1), (1, 0)],
        ".": [],
    }

    points = []
    for r, row in enumerate(g):
        if "S" in row:
            points.append((row.index("S"), r))
            break

    def get_pipes(point):
        cc, rr = point
        if g[rr][cc] != "S":
            for dc, dr in pipes[g[rr][cc]]:
                yield (cc + dc, rr + dr)
            return

        for dc in (-1, 0, 1):
            for dr in (-1, 0, 1):
                if (dc, dr) == (0, 0):
                    continue
                nc = cc - dc
                nr = rr - dr
                if nc < 0 or nr < 0 or nc > len(g[0]) or nr > len(g):
                    continue
                if (dc, dr) in pipes[g[nr][nc]]:
                    yield (nc, nr)

    while True:
        ps = list(get_pipes(points[-1]))
        for p in ps:
            if p not in points:
                points.append(p)
                break
        else:
            for p in ps:
                if p == points[0]:
                    points.append(p)

        if points[-1] == points[0]:
            break
    sc, sr = points[0]
    S = set((nc - sc, nr - sr) for nc, nr in get_pipes((sc, sr)))
    for k, v in pipes.items():
        if set(v) == S:
            S = k
            break
    g[sr][sc] = S
    points = set(points)
    part1 = len(points) // 2
    are_in = False
    in_count = 0
    out_count = 0
    for r, row in enumerate(g):
        are_in = False
        last = " "
        for c, v in enumerate(row):
            if (c, r) in points:
                if v == "-":
                    continue

                if v == "|":
                    are_in = not are_in
                if v == "FL":
                    last = v
                if v == "7" and last == "L":
                    are_in = not are_in
                if v == "J" and last == "F":
                    are_in = not are_in
                last = v
                continue
            last = ""
            if v:
                g[r][c] = "I" if are_in else "O"
                in_count += are_in
                out_count += not are_in
    # print('\n'.join(''.join(r) for r in g))
    part2 = in_count
    return part1, part2


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (7173, 291)


if __name__ == "__main__":
    main()
