#!/usr/bin/python3

from aoc import *

def solve(input_str):
    polym, rules = input_str.split('\n\n')
    rules = {k:v for k,_,v in parse_list(rules, str, str, str)}

    state = Counter(polym[i:i+2] for i in range(len(polym) - 1))

    def max_minus_min(state):
        elements = Counter()
        for (a,b),v in state.items():
            elements[a] += v
            elements[b] += v

        elements[polym[0]] += 1
        elements[polym[-1]] += 1
        for e in elements:
            elements[e] //= 2

        return max(elements.values()) - min(elements.values())

    for i in range(40):
        nstate = Counter()
        for k,v in state.items():
            nstate[k[0] + rules[k]] += v
            nstate[rules[k] + k[1]] += v
        state = nstate

        if i == 9:
            part1 = max_minus_min(state)

    return (part1, max_minus_min(state))


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (2027, 2265039461737)

if __name__ == '__main__':
    main()

