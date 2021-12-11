#!/usr/bin/python3

from aoc import *

def solve(input_str):
    state = list(parse_list(input_str, mapint))
    part1 = 0
    part2 = 0

    i = 0
    while i < 100 or not part2:
        i += 1

        count, state = step(state)
        if count == len(state) * len(state[0]):
            part2 = i
            break

        if i <= 100:
            part1 += count

    return (part1, part2)

def step(state):
    new = [[e + 1 for e in r] for r in state]
    flashing = [(r,c) for r in range(len(state)) for c in range(len(state[0])) if new[r][c] > 9]
    flashed = [[False for _ in r] for r in state]

    while flashing:
        r,c = flashing.pop()
        if not flashed[r][c]:
            flashed[r][c] = True
            neighbors = [(r-1, c-1), (r-1, c), (r-1, c+1), (r,c-1), (r,c+1), (r+1,c-1), (r+1,c), (r+1,c+1)]
            for nr, nc in neighbors:
                if 0<=nr<len(state) and 0<=nc<len(state[0]):
                    new[nr][nc] += 1
                    if new[nr][nc] > 9 and not flashed[nr][nc]:
                        flashing.append((nr, nc))

    for r,c in ((r,c) for r in range(len(state)) for c in range(len(state[0])) if new[r][c] > 9):
        new[r][c] = 0

    return sum(sum(r) for r in flashed),new


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (1735, 400)

if __name__ == '__main__':
    main()

