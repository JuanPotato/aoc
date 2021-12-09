from aoc import *

def solve(input_str):
    lava = list(parse_list(input_str, mapint))
    R = len(lava)
    C = len(lava[0])

    part1 = 0
    basins = []

    def flood(r,c,b):
        coords = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]

        for nr, nc in coords:
            if 0<=nr<R and 0<=nc<C and lava[r][c] < lava[nr][nc] < 9 and (nr, nc) not in basins[b]:
                basins[b].add((nr, nc))
                flood(nr, nc, b)

    for r in range(R):
        for c in range(C):
            coords = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            low = all(lava[r][c] < lava[nr][nc] for nr, nc in coords if 0<=nr<R and 0<=nc<C)

            if low:
                part1 += 1 + lava[r][c]
                basins.append(set())
                basins[-1].add((r,c))
                flood(r, c, len(basins) - 1)

    basins.sort(key=len)
    part2 = len(basins[-1]) * len(basins[-2]) * len(basins[-3])

    return (part1, part2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (550, 1100682)

if __name__ == '__main__':
    main()

