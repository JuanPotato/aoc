#!/usr/bin/python3

from aoc import *
import heapq

def solve(input_str):
    risk = list(parse_list(input_str, mapint))
    return (solve_maze(risk, (99,99)), solve_maze(risk, (499, 499)))

def get(risk, r, c):
    a = r // 100 + c // 100
    return (((risk[r % 100][c % 100] + a) - 1) % 9) + 1

def solve_maze(risk, goal):
    # Dijkstra ish
    R,C = goal[0]+1,goal[1]+1
    dist = [[1e9 for _ in range(C)] for _ in range(R)]
    dist[0][0] = 0

    visited = set()
    unvisited = [(0, (0,0))]
    heapq.heapify(unvisited)

    node = 0,0

    while unvisited:
        r,c = node

        n = [(r-1, c), (r,c-1), (r,c+1), (r+1,c)]
        for nr, nc in n:
            if not (0<=nr<R and 0<=nc<C): continue
            if (nr,nc) in visited: continue

            nd = dist[r][c] + get(risk, nr, nc)
            if nd < dist[nr][nc]:
                heapq.heappush(unvisited, (nd, (nr, nc)))
                dist[nr][nc] = nd

        visited.add(node)
        if goal in visited:
            break

        while node in visited:
            d,node = heapq.heappop(unvisited)

    return dist[R-1][C-1]


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (487, 2821)

if __name__ == '__main__':
    main()

