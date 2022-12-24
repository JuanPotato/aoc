#!/usr/bin/python3

from aoc import *

def solve(input_str):
    return (ssolve(input_str, 1), ssolve(input_str, 3))

def ssolve(inp, goal_state):
    grid = lmap(list, lines(inp))

    RIGHT,DOWN,LEFT,UP = 0,1,2,3
    dirs = ('>', 'v', '<', '^')
    grid = [r[1:-1] for r in grid[1:-1]]
    grid = [[(c=='>',c=='v',c=='<',c=='^') for c in r] for r in grid]

    H = len(grid)
    W = len(grid[0])

    next_grid = [[0 for _ in range(W)] for r in range(H)]

    start = (0, -1)
    end = (W-1, H)

    all_states = [(*start, 0)]

    round_i = -1
    while True:
        round_i += 1

        for ri in range(H):
            for ci in range(W):
                from_left = grid[ri][(ci - 1) % W][RIGHT]
                from_down = grid[(ri + 1) % H][ci][UP]
                from_right = grid[ri][(ci + 1) % W][LEFT]
                from_up = grid[(ri - 1) % H][ci][DOWN]
                next_grid[ri][ci] = (from_left, from_up, from_right, from_down)

        grid,next_grid = next_grid,grid

        new_states = set()
        for x,y,f in all_states:
            match f:
                case 0: f += (x, y) == end
                case 1: f += (x, y) == start
                case 2: f += (x, y) == end

            if f == goal_state:
                return round_i

            n = [(x, y), (x-1, y), (x+1, y), (x, y-1), (x, y+1)]

            for nx, ny in n:
                if (nx, ny) == start or (nx, ny) == end or ((0 <= nx < W and 0 <= ny < H) and grid[ny][nx] == (0,0,0,0)):
                    new_states.add((nx, ny, f))

        all_states = new_states


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (253, 794)

if __name__ == '__main__':
    main()


