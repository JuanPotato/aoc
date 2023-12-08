from aoc import *
from math import lcm


def solve(input_str):
    rl, elems = input_str.split("\n\n")
    elems = {e: (l, r) for e, l, r in chunk(re.findall("\w+", elems), 3)}

    es = [e for e in elems.keys() if e[2] == "A"]
    loop = {}
    for start in es:
        e = start
        i = 0
        while e[2] != "Z":
            s = rl[i % len(rl)]
            e = elems[e][s == "R"]
            i += 1
        loop[start] = i
    return loop["AAA"], lcm(*loop.values())


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (17621, 20685524831999)


if __name__ == "__main__":
    main()
