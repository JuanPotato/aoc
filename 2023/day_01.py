#!/usr/bin/python3

from aoc import *

def solve(input_str):
    part1 = sum(get_vals(l, False) for l in input_str.split('\n'))
    part2 = sum(get_vals(l, True) for l in input_str.split('\n'))

    return (part1, part2)

def get_vals(l, part2):
    nums = {str(i):str(i) for i in range(1,10)}
    words = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    if part2:
        nums.update(words)
    forward = '|'.join(nums.keys())
    first = re.search(forward, l)[0]
    last = re.search(forward[::-1], l[::-1])[0][::-1]
    return int(nums[first]) * 10 + int(nums[last])


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (55607, 55291)

if __name__ == '__main__':
    main()


