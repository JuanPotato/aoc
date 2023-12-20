#!/usr/bin/python3

from aoc import *
from math import *


def solve(input_str):
    outs = {}
    ins = defaultdict(list)
    types = {}
    data = {}
    LOW = False
    HIGH = True
    for l in input_str.split("\n"):
        name, outputs = l.split(" -> ")
        outputs = outputs.split(", ")
        if name[0] in "%&":
            t = name[0]
            name = name[1:]
        else:
            t = name

        types[name] = t

        if t == "%":
            data[name] = LOW
        outs[name] = outputs
        for out in outputs:
            ins[out].append(name)

    for n, t in types.items():
        if t == "&":
            data[n] = {k: False for k in ins[n]}

    # FROM, TO, SIGNAL
    button = ("button", "broadcaster", False)
    signals = deque([])
    count = [0, 0]

    key = ("mk", "fp", "xt", "zc")
    key_len = {}
    part1 = None
    part2 = None
    for i in range(1, 100000):
        signals.append(button)
        while signals:
            src, dst, sig = signals.popleft()
            count[sig] += 1
            if dst in key and sig == LOW and dst not in key_len:
                key_len[dst] = i
            if part2 == None and len(key_len) == len(key):
                part2 = lcm(*key_len.values())
            match types.get(dst, dst), sig:
                case "broadcaster", _:  # Broadcast
                    for o in outs[dst]:
                        signals.append((dst, o, sig))
                case "%", False:  # flip flop
                    data[dst] = not data[dst]
                    for o in outs[dst]:
                        signals.append((dst, o, data[dst]))
                case "&", _:  # conjunction
                    data[dst][src] = sig
                    val = not all(v for v in data[dst].values())
                    for o in outs[dst]:
                        signals.append((dst, o, val))
        if i == 1000:
            part1 = count[0] * count[1]
        if part1 and part2:
            break
    return part1, part2


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (980457412, 232774988886497)


if __name__ == "__main__":
    main()
