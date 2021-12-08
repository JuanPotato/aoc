from aoc import *

def solve(input_str):
    l = [[c.split() for c in line.split(' | ')] for line in input_str.strip().split('\n')]

    part1 = sum(len(e) in (2,4,3,7) for i,o in l for e in o)

    part2 = 0
    for i,o in l:
        nums = set(norm(w) for w in i + o)
        numlen = defaultdict(list)
        for n in nums:
            numlen[len(n)].append(set(n))

        cf = numlen[2].pop() # 1

        bcdf = numlen[4].pop() # 4

        acf = numlen[3].pop() # 7

        abcdefg = numlen[7].pop() # 8

        numlen[5].sort(key=lambda n: len(n - cf))
        acdfg = numlen[5].pop(0) # 3

        numlen[5].sort(key=lambda n: len(n - bcdf))
        abdfg = numlen[5].pop(0) # 5

        acdeg = numlen[5].pop(0) # 2

        numlen[6].sort(key=lambda n: len(n - acdfg))
        abcdfg = numlen[6].pop(0) # 9

        numlen[6].sort(key=lambda n: len(n - acf))
        abcefg = numlen[6].pop(0) # 0

        abdefg = numlen[6].pop() # 6

        nums = lmap(norm, (abcefg, cf, acdeg, acdfg, bcdf, abdfg, abdefg, acf, abcdefg, abcdfg))
        nums = {w:str(i) for i,w in enumerate(nums)}

        out_val = int(''.join(nums[norm(w)] for w in o))
        part2 += out_val

    return (part1, part2)

def norm(s):
    return ''.join(sorted(list(s)))


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (525, 1083859)

if __name__ == '__main__':
    main()

