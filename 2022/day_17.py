#!/usr/bin/python3

from aoc import *

ROCKS = '''####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##'''

class Rock:
    def __init__(self, rock_str):
        self.coords = [(x, y) for y,r in enumerate(lines(rock_str)) for x,c in enumerate(r) if c == '#']
        self.height = max(c[1] for c in self.coords) + 1

    def __repr__(self):
        return f'Rock(coords={self.coords}, height={self.height})'

    def fits(self, grid, loc):
        x,y = loc
        for dx,dy in self.coords:
            if grid[y-dy][x+dx] != 0:
                return False
        return True
                

def solve(input_str):
    rocks = [Rock(rock) for rock in ROCKS.split('\n\n')]
    wind = input_str.strip()

    WIDTH = 7
    grid = []
    grid.append([1] * (WIDTH + 2))

    max_rock = 0
    wind_i = 0
    wind_turn = False
    maxs = []

    for rock_i in range(10000):
        next_rock = rocks[rock_i % len(rocks)]
        x, y = (3, max_rock + 3 + next_rock.height)

        while len(grid) < (max_rock + 1 + 7):
            grid.append([1] + [0] * WIDTH + [1])

        while True:
            wind_turn = not wind_turn

            dx,dy = 0,0
            if wind_turn:
                next_wind = wind[wind_i % len(wind)]
                wind_i += 1
                dx = 1 if next_wind == '>' else -1
            else:
                dy = -1

            if next_rock.fits(grid, (x+dx, y+dy)):
                x += dx
                y += dy
            elif not wind_turn:
                # We we're moving down and we couldn't. We hit rock, we stop
                break
        
        for dx,dy in next_rock.coords:
            grid[y-dy][x+dx] = 1

        for maxy in make_range(len(grid)-1,0):
            if 1 in grid[maxy][1:-1]:
                max_rock = maxy
                maxs.append(max_rock)
                break

    for i in range(10, 5000):
        diff = [maxs[i+j] - maxs[j] for j in range(5000, 5100)]
        if all(d == diff[0] for d in diff):
            period = i
            offset = diff[0]
            break

    for i in range(1000):
        diff = [maxs[i+j+period] - maxs[i+j] for j in range(period)]
        if all(d == diff[0] for d in diff):
            start_repeat = i
            break

    def getgot(goal):
        m, r = divmod(goal, period)
        while r < start_repeat:
            r += period
            m -= 1
        total = maxs[r-1] + m * offset
        return total

    return getgot(2022), getgot(1000000000000)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (3124, 1561176470569)

if __name__ == '__main__':
    main()


