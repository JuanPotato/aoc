from aoc import *

def solve(input_str):
    fish = [0] * 9
    for n in eval(input_str):
        fish[n] += 1

    counts = [sum(fish)]

    for i in range(256):
        # 1-6, 7 + 0, 8, 0
        fish = fish[1:7] + [fish[7] + fish[0], fish[8], fish[0]]
        counts.append(sum(fish))

    return (counts[80], counts[256])


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (394994, 1765974267455)

if __name__ == '__main__':
    main()

