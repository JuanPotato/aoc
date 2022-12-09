#!/usr/bin/python3

from aoc import *
import re

def solve(input_str):
    snake = [[0,0] for _ in range(10)]
    snake_tracker = [set() for _ in snake]
    for l in lines(input_str):
        d,n = l.split(' ')
        for _ in range(int(n)):
            match d:
                case 'U': snake[0][1] += 1
                case 'D': snake[0][1] -= 1
                case 'R': snake[0][0] += 1
                case 'L': snake[0][0] -= 1

            for i in range(len(snake) - 1):
                h = snake[i]
                t = snake[i+1]
                if h[0] == t[0]:
                    if h[1] - t[1] > 1:
                        t[1] = h[1] - 1
                    elif h[1] - t[1] < -1:
                        t[1] = h[1] + 1

                elif h[1] == t[1]:
                    if h[0] - t[0] > 1:
                        t[0] = h[0] - 1
                    elif h[0] - t[0] < -1:
                        t[0] = h[0] + 1

                if abs(h[0] - t[0]) + abs(h[1] - t[1]) > 2:
                    if h[0] - t[0] > 0:
                        t[0] += 1
                    else:
                        t[0] -= 1

                    if h[1] - t[1] > 0:
                        t[1] += 1
                    else:
                        t[1] -= 1

            for i in range(len(snake)):
                snake_tracker[i].add(tuple(snake[i]))

    return (len(snake_tracker[1]), len(snake_tracker[9]))


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (6486, 2678)

if __name__ == '__main__':
    main()


