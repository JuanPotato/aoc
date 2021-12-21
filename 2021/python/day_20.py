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

    steps = 50
    goalr = (-(steps+1), R+(steps+1))
    goalc = (-(steps+1), C+(steps+1))

    startr = (goalr[0]-steps, goalr[1]+steps)
    startc = (goalc[0]-steps, goalc[1]+steps)

    images = []
    start_img = [[(r,c) in imm for c in range(startc[0], startc[1])] for r in range(startr[0], startr[1])]

    images.append(start_img)

    def enhance(r,c, prev):
        num = 0

        for br in (r,r+1,r+2):
            for bc in (c,c+1,c+2):
                num = (num << 1) | prev[br][bc]

        return enhl[num]

    for _ in range(steps):
        nr = len(images[-1]) - 2
        nc = len(images[-1][0]) - 2

        new_img = [[enhance(r,c,images[-1]) for c in range(nc)] for r in range(nr)]
        images.append(new_img)
    
    return (sum(map(sum, images[2])), sum(map(sum, images[50])))

def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (5846, 21149)

if __name__ == '__main__':
    main()

