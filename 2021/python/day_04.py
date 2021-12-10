#!/usr/bin/python3

from aoc import *

def solve(input_str):
    lines = input_str.split('\n\n')
    nums = mapint(lines[0].split(','))
    boards = [parse_grid(board_str, int) for board_str in lines[1:]]
    scores = []

    i = 0
    while boards:
        called = nums[:i+1]
        bi = len(boards) - 1

        while bi >= 0:
            if any(all(e in called for e in rc) for rc in rows_cols(boards[bi])):
                scores.append(score(boards.pop(bi), called))
            bi -= 1
        i += 1

    return (scores[0], scores[-1])


def score(board, called):
    return sum(n for r in board for n in r if n not in called) * called[-1];


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (2745, 6594)

if __name__ == '__main__':
    main()

