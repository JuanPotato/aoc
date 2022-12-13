#!/usr/bin/python3

from aoc import *

def solve(input_str):
    input_str = input_str.strip()
    part1 = 0
    for i,(l,r) in enumerate([lmap(eval, p.split('\n')) for p in input_str.split('\n\n')]):
        if compare(l, r):
            part1 += i + 1

    lis = lmap(eval, input_str.strip().replace('\n\n', '\n').split('\n'))

    two = [[2]]
    six = [[6]]
    lis.append(two)
    lis.append(six)

    is_sort = False
    while not is_sort:
        is_sort = True
        for i in range(len(lis) - 1):
            if not compare(lis[i], lis[i+1]):
                lis[i],lis[i+1] = lis[i+1],lis[i]
                is_sort = False

    part2 = (1 + lis.index(two)) * (1 + lis.index(six))

    return (part1, part2)

def compare(L, R):
    #print(' ', L, R)
    Li = isinstance(L, int)
    Ri = isinstance(R, int)

    if Li and Ri:
        if L < R:
            return True
        elif L > R:
            return False
        else:
            return None
    else:
        if Li:
            L = [L]
        if Ri:
            R = [R]
        for i in range(max((len(L), len(R)))):
            if not i < len(L):
                return True
            if not i < len(R):
                return False
            if (out := compare(L[i], R[i])) != None:
                return out


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (6428, 22464)

if __name__ == '__main__':
    main()


