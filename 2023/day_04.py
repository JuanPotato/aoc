#!/usr/bin/python3

from aoc import *

def solve(input_str):
    score = 0
    nums = {}
    N = len(input_str.split('\n'))
    cnt = {n:1 for n in range(1,N+1)}
    for l in input_str.split('\n'):
        i = ints(l)[0]
        win = ints(l.split('|')[0])[1:]
        me = ints(l.split('|')[1])
        k = sum(n in win for n in me)
        if k:
            score += 2**(k-1)
        nums[i] = k

    for k in range(1,N+1):
        for nk in range(k+1, k+nums.get(k)+1):
            cnt[nk] += cnt.get(k)

    return score, sum(cnt.values())


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (27059, 5744979)

if __name__ == '__main__':
    main()
