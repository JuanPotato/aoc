from aoc import *

def solve(input_str):
    nums = list(parse_list(input_str, mapint))
    N = len(nums[0])

    # part1
    gamma = int(''.join(str((2 * sum(num[i] for num in nums)) // len(nums)) for i in range(N)), 2)

    # part2
    def calc_rating(get_next_digit):
        remaining = list(nums)

        digit = 0
        while len(remaining) > 1:
            next_digit = get_next_digit(remaining, digit)
            remaining = [rem for rem in remaining if rem[digit] == next_digit]
            digit += 1

        return int(''.join(map(str, remaining[-1])), 2)

    ox = calc_rating(lambda r, i:     (2 * sum(n[i] for n in r)  // len(r)))
    co = calc_rating(lambda r, i: 1 - (2 * sum(n[i] for n in r)) // len(r))

    return (gamma * ((2**N - 1) ^ gamma), ox * co)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (1025636, 793873)

if __name__ == '__main__':
    main()

