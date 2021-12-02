from aoc import *

def solve(input_str):
    data = list(parse_list(input_str, int))

    part1 = sum(a < b for a,b in zip(data, data[1:]))
    part2 = sum(a < b for a,b in zip(data, data[3:]))

    return (part1, part2)


if __name__ == '__main__':
    print(solve(get_input(__file__)))
