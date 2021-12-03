from aoc import *

def solve(input_str):
    nums = list(parse_list(input_str, lambda n: tuple(map(int, n))))
    N = len(nums[0])

    # part1
    gamma = int(''.join(str((2 * sum(num[i] for num in nums)) // len(nums)) for i in range(N)), 2)

    # part2
    oxs = list(nums)
    cos = list(nums)

    digit = 0
    while len(oxs) > 1:
        next_ox = (2 * sum(ox[digit] for ox in oxs)) // len(oxs)
        oxs = [ox for ox in oxs if ox[digit] == next_ox]
        digit += 1
    ox = int(''.join(map(str, oxs[-1])), 2)

    digit = 0
    while len(cos) > 1:
        next_co = 1 - (2 * sum(co[digit] for co in cos)) // len(cos)
        cos = [co for co in cos if co[digit] == next_co]
        digit += 1
    co = int(''.join(map(str, cos[-1])), 2)

    return (gamma * ((2**N - 1) ^ gamma), ox * co)


if __name__ == '__main__':
    print(solve(get_input(__file__)))
