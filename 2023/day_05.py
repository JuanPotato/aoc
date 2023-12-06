#!/usr/bin/python3

from aoc import *


def solve(input_str):
    inp = input_str.split("\n\n")
    seeds1 = [(s, s + 1) for s in ints(inp[0])]
    seeds2 = [(s, s + n) for s, n in chunk(ints(inp[0]), 2)]
    maps = [chunk(ints(p), 3) for p in inp[1:]]
    return magic(seeds1, maps), magic(seeds2, maps)


def magic(seeds, maps):
    stage = []
    for m in maps:
        for s in seeds:
            seed = [s]
            seed2 = []
            for dst, src, n in m:
                for ns in seed:
                    a, b, c = clip(ns, (src, src + n))
                    if a:
                        seed2.append(a)
                    if b:
                        stage.append((b[0] - src + dst, b[1] - src + dst))
                    if c:
                        seed2.append(c)
                seed, seed2 = seed2, []
            stage.extend(seed)
        seeds, stage = stage, []
    return min(seeds)[0]


def clip(r1, r2):
    r1_start, r1_stop = r1
    r2_start, r2_stop = r2
    #   [  1  )
    #     [2)
    # = [a) [c)
    #     [b)
    a, b, c = None, None, None
    b_start, b_stop = None, None

    # r1 [  r2 [
    if r1_start < r2_start:
        # r1 [  r1 )  r2 [
        # r1 [  r2 [  r2 )
        a = (r1_start, min(r1_stop, r2_start))
        b_start = r2_start
    # r2 [  r1 [  r2 )
    elif r1_start < r2_stop:
        b_start = r1_start

    # r2 )  r1 )
    if r1_stop > r2_stop:
        # r2 )  r1 [  r1 )
        # r1 [  r2 )  r1 )
        c = (max(r1_start, r2_stop), r1_stop)
        b_stop = r2_stop
    # r2 [  r1 )  r2 )
    elif r1_stop > r2_start:
        b_stop = r1_stop

    if b_start is not None and b_stop is not None:
        b = (b_start, b_stop)

    return a, b, c


#      [ )
# [ )
assert clip((7, 9), (1, 3)) == (None, None, (7, 9))

# [ )
# [ )
assert clip((1, 9), (1, 9)) == (None, (1, 9), None)

#   [ )
# [     )
assert clip((5, 7), (1, 9)) == (None, (5, 7), None)

#   [   )
# [   )
assert clip((5, 9), (1, 7)) == (None, (5, 7), (7, 9))

# [ )
#      [ )
assert clip((1, 3), (7, 9)) == ((1, 3), None, None)

# [   )
#   [   )
assert clip((1, 7), (5, 9)) == ((1, 5), (5, 7), None)

# [     )
#   [ )
assert clip((1, 9), (5, 7)) == ((1, 5), (5, 7), (7, 9))


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (1181555926, 37806486)


if __name__ == "__main__":
    main()
