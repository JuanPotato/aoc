#!/usr/bin/python3

from aoc import *

def solve(input_str):
    return (elf(input_str, 10)[0], elf(input_str)[1])

def elf(inp, rounds=None):
    g = lmap(list, lines(inp))
    neigh = [
        (1, 1), (1, 0), (1, -1),
        (0, 1)        , (0, -1),
        (-1,1), (-1,0), (-1,-1),
    ]
    dirs = [
        ((0, -1), ((1, -1), (0, -1), (-1, -1))),
        ((0,  1), ((1,  1), (0,  1), (-1,  1))),
        ((-1, 0), ((-1, -1), (-1, 0), (-1, 1))),
        (( 1, 0), (( 1, -1), ( 1, 0), ( 1, 1))),
    ]

    round_i = 0
    moved = True
    while moved:
        if rounds != None and round_i == rounds:
            break
        moved = False
        good_size = all(g[0][i] == '.' and g[-1][i] == '.' for i in range(len(g[0])))
        good_size = good_size and all(r[0] == '.' and r[-1] == '.' for r in g)
        if not good_size:
            for r in g:
                r.insert(0, '.')
                r.append('.')

            g.insert(0, list('.'*len(g[0])))
            g.append(list('.'*len(g[0])))

        w = len(g[0])
        h = len(g)

        target = [[True for _ in range(w)] for _ in range(h)]

        for y, r in enumerate(g):
            for x, c in enumerate(r):
                if c == '#':
                    if all(g[cy+y][cx+x] != '#' for cx,cy in neigh):
                        target[y][x] = (x, y)
                        continue

                    for di in range(len(dirs)):
                        d = dirs[(round_i + di) % len(dirs)]
                        dx, dy = d[0]
                        checks = d[1]
                        good = all(g[cy+y][cx+x] != '#' for cx,cy in checks)
                        if good:
                            moved = True
                            break
                    else:
                        target[y][x] = (x, y)
                        continue

                    ny = y + dy
                    nx = x + dx
                    if target[ny][nx] == True:
                        target[ny][nx] = (x, y)

                    elif target[ny][nx] == False:
                        target[y][x] = (x, y)

                    else:
                        rx,ry = target[ny][nx]
                        target[ry][rx] = (rx, ry)
                        target[ny][nx] = False
                        target[y][x] = (x, y)
        for r in target:
            for i in range(len(r)):
                if isinstance(r[i], bool):
                    r[i] = '.'
                else:
                    r[i] = '#'
        g = target
        round_i += 1


    for ri in range(len(g)):
        if all(c == '.' for c in g[ri]):
            start_y = ri
        else:
            break

    for ri in make_range(len(g)-1,0):
        if all(c == '.' for c in g[ri]):
            stop_y = ri
        else:
            break

    for ci in range(len(g[0])):
        if all(g[r][ci] == '.' for r in make_range(start_y, stop_y)):
            start_x = ci
        else:
            break

    for ci in make_range(len(g[0])-1, 0):
        if all(g[r][ci] == '.' for r in make_range(start_y, stop_y)):
            stop_x = ci
        else:
            break

    rect = [r[start_x+1:stop_x] for r in g[start_y+1:stop_y]]
    o = '\n'.join(''.join(r) for r in rect)
    return(o.count('.'), round_i)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (4005, 1008)

if __name__ == '__main__':
    main()


