#!/usr/bin/python3

from aoc import *
from functools import cache

def solve(input_str):
    enh, img = input_str.strip().split('\n\n')
    img = img.strip().split('\n')

    enhl = [c == '#' for c in enh]
    imm = set((r,c) for r in range(len(img)) for c in range(len(img[0])) if img[r][c] == '#')

    R = len(img)
    C = len(img[0])

    @cache
    def get(r, c, step):
        if step == 0:
            return (r,c) in imm

        num = 0
        for br in (r-1,r,r+1):
            for bc in (c-1,c,c+1):
                num = (num << 1) | get(br, bc, step-1)

        return enhl[num]

    def count_on(step):
        return sum(get(r,c,step) for r in range(-(step+1), R+(step+1)) for c in range(-(step+1), C+(step+1)))
    
    return (count_on(2), count_on(50))

def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (5846, 21149)

if __name__ == '__main__':
    main()

