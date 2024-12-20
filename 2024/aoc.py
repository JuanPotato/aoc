#!/usr/bin/python3

from collections import *
from functools import reduce
from pathlib import Path
import importlib
import traceback
import typing
import time
import sys
import re

Point = namedtuple('Point', ('x', 'y'))

Trie = lambda: defaultdict(Trie)

def main():
    for day in range(1, 26):
        try:
            mod = importlib.import_module(f'day_{day:02}')
            print(f'Running day {day}:')
            start = time.time()
            mod.main()
            stop = time.time()
            ms = (stop - start) * 1000
            print(f'{ms:.02f} ms')

        except ModuleNotFoundError:
            break

        except Exception as e:
            traceback.print_exception(None, e, e.__traceback__)

        print()

# Utility functions
def parse_list(s, *types, line='\n', sep=' '):
    return list(_parse_list(s, *types, line, sep))

def _parse_list(s, *types, line='\n', sep=' '):
    if not types:
        types = (str,)

    for line in s.strip().split('\n'):
        t = tuple(type(word) for type,word in zip(types, line.split(sep, len(types) - 1)))
        if len(t) == 1:
            t = t[0]
        yield t

def parse_grid(s, types, line='\n', sep=' +'):
    return [lmap(types, re.split(sep, row.strip())) for row in re.split(line, s.strip())]

def _every_n(l, n):
    for i in range(n):
        yield l[i::n]

def every_n(l, n):
    return tuple(_every_n(l, n))

def rows_cols(grid):
    R = len(grid)
    C = len(grid[0])
    yield from (list(grid[r]) for r in range(R))
    yield from ([grid[i][c] for i in range(R)] for c in range(C))

def make_range(start, end):
    if start <= end:
        return range(start, end + 1)
    else:
        return range(start, end - 1, -1)

def get_input(script):
    path = Path(script).with_suffix('.input')
    with path.open() as f:
        return f.read()

def sumrange(start, stop=None):
    if stop == None:
        start, stop = 0, start
    return (stop - start + 1) * (start + stop) // 2

def norm(s):
    return ''.join(sorted(list(s)))

def pop_by(l, cond):
    for i in range(len(l)):
        if cond(l[i]):
            return l.pop(i)

def default_counter(it):
    d = defaultdict(int)
    for e in it:
        d[e] += 1
    return d

def lines(input_str, sep='\n'):
    return input_str.strip().split(sep)

def ddict():
    return defaultdict(ddict)

# taken from https://github.com/mcpower/adventofcode/blob/master/utils.py
def chunk(l,n):
    return list(zip(*[iter(l)]*n))

def window(l, n):
    return list(zip(*[l[i:] for i in range(n)]))

def lmap(func, *iterables):
    return list(map(func, *iterables))

def mapint(l):
    return list(map(int, l))

def splitint(s, sep=','):
    return list(map(int, s.split(sep)))

def make_grid(*dimensions: typing.List[int], fill=None):
    "Returns a grid such that 'dimensions' is juuust out of bounds."
    if len(dimensions) == 1:
        return [fill for _ in range(dimensions[0])]
    next_down = make_grid(*dimensions[1:], fill=fill)
    return [list(next_down) for _ in range(dimensions[0])]

def min_max(l):
    return min(l), max(l)

def partial_sum(l):
    "out[i] == sum(in[:i])"
    out = [0]
    for i in l:
        out.append(out[-1] + i)
    return out

def list_diff(x):
    return [b-a for a, b in zip(x, x[1:])]

def flatten(l):
    return [i for x in l for i in x]

def ints(s: str) -> typing.List[int]:
    assert isinstance(s, str), f"you passed in a {type(s)}!!!"
    return lmap(int, re.findall(r"(?:(?<!\d)-)?\d+", s))  # thanks mserrano!

def floats(s: str) -> typing.List[float]:
    assert isinstance(s, str), f"you passed in a {type(s)}!!!"
    return lmap(float, re.findall(r"-?\d+(?:\.\d+)?", s))

def words(s: str) -> typing.List[str]:
    assert isinstance(s, str), f"you passed in a {type(s)}!!!"
    return re.findall(r"[a-zA-Z]+", s)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()

