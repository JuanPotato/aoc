#!/usr/bin/python3

from aoc import *

def solve(input_str):
    monkeys = {}
    for l in lines(input_str):
        p = [e.strip(":") for e in l.split(' ')]
        monkeys[p[0]] = makefun(p)
    part1 = monkeys['root'](monkeys)

    monkeys = {}
    for l in lines(input_str):
        p = [e.strip(":") for e in l.split(' ')]
        monkeys[p[0]] = makefun2(p)

    eq = monkeys['root'](monkeys)
    test = eval(f'lambda humn: {eq}')

    l,r = None,None

    i = 1
    while l == None:
        if test(i) > 0:
            l = i
        if test(-i) > 0:
            l = -i
        i *= 2

    while r == None:
        if test(i) < 0:
            r = i
        if test(-i) < 0:
            r = -i
        i *= 2

    if test(r) < 0:
        l,r = r,l

    while l != (r+1):
        m = (l + r) // 2
        if test(m) > 0:
            r = m
        else:
            l = m
    part2 = l

    return (part1, part2)


def makefun2(p):
    if len(p) == 2:
        if p[0] == 'humn':
            p[1] = 'humn'

        def do(d):
            return p[1]
        return do

    mc, ma, ops, mb = p
    if mc == 'root':
        ops = '-'

    def do(d):
        a = d[ma](d)
        b = d[mb](d)
        return f'({a}{ops}{b})'
    return do


def makefun(p):
    if len(p) == 2:
        v = int(p[1])
        def do(d):
            return v
        return do

    mc, ma, ops, mb = p

    match ops:
        case '+': op = lambda a,b:a+b
        case '-': op = lambda a,b:a-b
        case '*': op = lambda a,b:a*b
        case '/': op = lambda a,b:a//b

    def do(d):
        a = d[ma](d)
        b = d[mb](d)
        c = op(a, b)
        return c
    return do



def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (121868120894282, 3582317956029)

if __name__ == '__main__':
    main()


