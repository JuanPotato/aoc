from aoc import *

def solve(input_str):
    l = [[c.split() for c in line.split(' | ')] for line in input_str.strip().split('\n')]

    part1 = sum(len(e) in (2,4,3,7) for i,o in l for e in o)

    part2 = 0
    for i,o in l:
        nums = defaultdict(list)
        for n in i:
            nums[len(n)].append(set(n))

        cf = nums[2].pop() # 1
        bcdf = nums[4].pop() # 4
        acf = nums[3].pop() # 7
        abcdefg = nums[7].pop() # 8

        acdfg = pop_by(nums[5], lambda n: len(n - cf) == 3) # 3
        abdfg = pop_by(nums[5], lambda n: len(n - bcdf) == 2) # 5
        acdeg = nums[5].pop(0) # 2

        abcdfg = pop_by(nums[6], lambda n: len(n - acdfg) == 1) # 9
        abcefg = pop_by(nums[6], lambda n: len(n - acf) == 3) # 0
        abdefg = nums[6].pop() # 6

        nums = lmap(norm, (abcefg, cf, acdeg, acdfg, bcdf, abdfg, abdefg, acf, abcdefg, abcdfg))
        nums = {w:str(i) for i,w in enumerate(nums)}

        out_val = int(''.join(nums[norm(w)] for w in o))
        part2 += out_val

    return (part1, part2)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (525, 1083859)

if __name__ == '__main__':
    main()

