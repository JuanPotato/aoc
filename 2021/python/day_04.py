from aoc import *

def solve(input_str):
    lines = input_str.split('\n\n')
    nums = list(map(int, lines[0].split(',')))
    boards = [[list(map(int, r.split())) for r in board_str.strip().split('\n')] for board_str in lines[1:]]
    scores = []

    i = 0
    while boards:
        called = nums[:i+1]
        bi = len(boards) - 1

        while bi >= 0:
            if won(boards[bi], called):
                scores.append(score(boards.pop(bi), called))
            bi -= 1
        i += 1

    return (scores[0], scores[-1])


def won(board, called):
    N = len(board)
    return any(all(board[r][n] in called for n in range(N)) for r in range(N)) or \
           any(all(board[n][c] in called for n in range(N)) for c in range(N))


def score(board, called):
    return sum(n for r in board for n in r if n not in called) * called[-1];


if __name__ == '__main__':
    print(solve(get_input(__file__)))
