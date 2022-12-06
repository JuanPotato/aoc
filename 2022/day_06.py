#!/usr/bin/python3

from aoc import *

def solve(input_str):
    def do_thing(n):
        for i, w in enumerate(window(input_str, n)):
            if len(set(w)) == n:
                return i + n

    return (do_thing(4), do_thing(14))


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (1140, 3495)

if __name__ == '__main__':
    main()


