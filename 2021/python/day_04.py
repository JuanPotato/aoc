from aoc import *

def solve(input_str):
    lines = input_str.split('\n\n')
    nums = list(map(int, lines[0].split(',')))
    boards = [[list(map(int, r.split())) for r in board_str.strip().split('\n')] for board_str in lines[1:]]

    # part 1
    done = False
    for i in range(len(nums)):
        called = nums[:i+1]
        for board in boards:
            if won(board, called):
                first_score = score(board, called)
                done = True
                break
        if done:
            break

    # part 2
    done = False
    not_win = list(boards)
    for i in range(len(nums)):
        called = nums[:i+1]
        new_not_win = [j for j in not_win if not won(j, called)]
        if len(new_not_win) == 0:
            last_score = score(not_win[-1], called)
            break
        else:
            not_win = new_not_win
    
    return (first_score, last_score)


def won(board, called):
    N = len(board)

    for r in range(N):
        if all(n in called for n in board[r]):
            return True

    for c in range(len(board[0])):
        if all(board[n][c] in called for n in range(N)):
            return True

    if all(board[d][d] in called for d in range(N)):
        return True

    if all(board[len(board) - 1 - d][d] in called for d in range(N)):
        return True

    return False


def score(board, called):
    a = sum(n for r in board for n in r if n not in called)
    return a * called[-1]


if __name__ == '__main__':
    print(solve(get_input(__file__)))
