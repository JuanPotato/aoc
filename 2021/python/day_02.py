from aoc import *

def solve(input_str):
    x = 0
    # y1 is also aim
    y1, y2 = 0, 0

    for action, n in parse_list(input_str, str, int):
        if action == 'up':
            y1 -= n
        elif action == 'down':
            y1 += n
        elif action == 'forward':
            x += n
            y2 += y1 * n

    return (x * y1, x * y2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (1868935, 1965970888)

if __name__ == '__main__':
    main()

