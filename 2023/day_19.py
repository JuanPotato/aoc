#!/usr/bin/python3

from aoc import *


def solve(input_str):
    return part1(input_str), part2(input_str)


def part1(input_str):
    workflows, ratings = input_str.split("\n\n")
    flows = {}
    flows["A"] = lambda a, b: True
    flows["R"] = lambda a, b: False

    for f in workflows.split("\n"):
        name, f = f.split("{")
        rules = f[:-1].split(",")
        flows[name] = make_flow(name, rules)
    total = 0
    for r in ratings.split("\n"):
        x, m, a, s = ints(r)
        parts = {"x": x, "m": m, "a": a, "s": s}
        if flows["in"](parts, flows):
            total += x + m + a + s
    return total


def make_flow(name, rules):
    exprs = []
    for r in rules:
        exprs.append(make_rule(name, r))

    def flow(parts, flows):
        for e in exprs:
            res = e(parts)
            if res == None:
                continue
            return flows[res](parts, flows)

    return flow


def make_rule(name, rule):
    if ":" in rule:
        cond, step = rule.split(":")
        var = cond[0]
        cmp = cond[1]
        n = int(cond[2:])
        if cmp == "<":
            return lambda p: step if p[var] < n else None
        elif cmp == ">":
            return lambda p: step if p[var] > n else None
    else:
        return lambda p: rule


def part2(input_str):
    workflows, ratings = input_str.split("\n\n")
    flows = {}

    def A(p, f):
        x, m, a, s = [b - a for a, b in p.values()]
        return x * m * a * s

    flows["A"] = A
    flows["R"] = lambda p, f: 0

    for f in workflows.split("\n"):
        name, f = f.split("{")
        rules = f[:-1].split(",")
        flows[name] = make_flow2(name, rules)

    parts = {"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)}
    return flows["in"](parts, flows)


def make_flow2(name, rules):
    exprs = []
    for r in rules:
        exprs.append(make_rule2(name, r))

    def flow(parts, flows):
        total = 0
        for e in exprs:
            parts, count = e(parts, flows)
            total += count
        return total

    return flow


def make_rule2(name, rule):
    if ":" in rule:
        cond, step = rule.split(":")
        var = cond[0]
        cmp = cond[1]
        n = int(cond[2:])

        def thing(parts, flows):
            start, stop = parts[var]
            if start <= n < stop:
                new_parts = dict(parts)
                if cmp == "<":
                    new_parts[var] = (start, n)
                    parts[var] = (n, stop)  # return
                elif cmp == ">":
                    new_parts[var] = (n + 1, stop)
                    parts[var] = (start, n + 1)
                return parts, flows[step](new_parts, flows)
            else:
                return parts, 0

        return thing
    else:
        return lambda p, f: (dict(), f[rule](p, f))


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (399284, 121964982771486)


if __name__ == "__main__":
    main()
