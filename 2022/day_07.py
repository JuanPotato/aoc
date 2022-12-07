#!/usr/bin/python3

from aoc import *
import re

def solve(input_str):
    fs = ddict()
    cur_path = []

    for l in lines(input_str):
        if m := re.match(r"\$ cd (.+)", l):
            arg = m.group(1)
            if arg == "/":
                cur_path = []
            elif arg == "..":
                cur_path.pop()
            else:
                cur_path.append(arg)

        elif m := re.match(r"(\d+) (.+)", l):
            size = int(m.group(1))
            file = m.group(2)
            cur_dir = fs
            for p in cur_path:
                cur_dir = cur_dir[p]
            cur_dir[file] = size

    sz = {}
    sizes(fs, "/", sz)

    part1 = sum(v for k,v in sz.items() if v <= 100000)
    part2 = min(v for v in sz.values() if v >= (30000000 - (70000000 - sz["/"])))

    return (part1, part2)


def sizes(dir, cur_path="/", cur_sizes=None):
    if cur_sizes == None:
        cur_sizes = {}
    size = 0
    for k,v in dir.items():
        if isinstance(v, int):
            size += v
        else:
            size += sizes(v, f"{cur_path}{k}/", cur_sizes)
    cur_sizes[cur_path] = size
    return size


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (1778099, 1623571)

if __name__ == '__main__':
    main()


