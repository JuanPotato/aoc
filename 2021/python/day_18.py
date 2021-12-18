#!/usr/bin/python3

from aoc import *

def solve(input_str):
    numstr = list(parse_list(input_str, str))

    # part1
    nums = list(map(eval, numstr))
    s = reduce(add, nums, nums.pop(0))
    part1 = mag(s)

    # part2
    part2 = 0
    for a in numstr:
        for b in numstr:
            if a == b: continue
            s = add(eval(a), eval(b))
            part2 = max(part2, mag(s))

    return (part1, part2)


def add(x, y):
    s = [x, y]

    while explode(s) or split(s):
        pass

    return s


def mag(l):
    if isinstance(l, list):
        return 3 * mag(l[0]) + 2 * mag(l[1])
    else:
        return l


def split(l):
    for i,e in enumerate(l):
        if isinstance(e, list):
            if split(e):
                return True

        elif e >= 10:
            l[i] = [e//2, (e+1)//2]
            return True

    return False


def explode(l):
    trail = bad(l)
    got = False

    for i, (parent, par_i, par_par, depth) in enumerate(trail):
        if depth == 4:
            ppi = par_par.index(parent)
            par_par[ppi] = 0
            break
    else:
        return False


    vl, vr = parent
    if i != 0:
        ll, li, _,  _ = trail[i-1]
        ll[li] += vl

    if (i + 2) < len(trail):
        rl, ri, _, _ = trail[i+2]
        rl[ri] += vr

    return True


# goes through the nested lists, returns a list of found numbers.
# Each element in the list is a tuple with the list the int was found in, the index of the int,
# the parent of the list, and the depht of the int.
def bad(l, trail=None, depth=0, parent=None):
    if trail == None:
        trail = list()

    for i,e in enumerate(l):
        if isinstance(e, list):
            bad(e, trail, depth+1, l)
        else:
            trail.append((l, i, parent if depth == 4 else None, depth))
    return trail


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (3665, 4775)

if __name__ == '__main__':
    main()

