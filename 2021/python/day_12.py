#!/usr/bin/python3

from aoc import *

def solve(input_str):
    v = defaultdict(list)
    for s,e in parse_list(input_str, str, str, sep='-'):
        v[s].append(e)
        v[e].append(s)

    return dfs1(v, ['start']), dfs2(v, ['start'])

def dfs1(vert, path):
    count = 0
    for n in vert[path[-1]]:
        if n == 'start': continue
        if n.isupper() or n not in path:
            path.append(n)
            if n == 'end':
                count += 1
            else:
                count += dfs1(vert, path)
            path.pop()

    return count

def dfs2(vert, path):
    count = 0
    for n in vert[path[-1]]:
        if n == 'start': continue
        smalls = Counter(e for e in path if e.islower())

        if n not in smalls or 2 not in smalls.values():
            path.append(n)
            if n == 'end':
                count += 1
            else:
                count += dfs2(vert, path)
            path.pop()

    return count


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (3298, 93572)

if __name__ == '__main__':
    main()

