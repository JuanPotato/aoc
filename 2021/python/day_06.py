from aoc import *

def solve(input_str):
    fish = Counter()
    fish.update(eval(input_str))
    counts = [sum(fish.values())]

    for i in range(256):
        new_fish = {k - 1: v for k,v in fish.items()}
        new_fish[6] = new_fish.get(6, 0) + new_fish.pop(-1, 0)
        new_fish[8] = fish.get(0, 0)
        fish = new_fish
        counts.append(sum(fish.values()))

    return (counts[80], counts[256])


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (394994, 1765974267455)

if __name__ == '__main__':
    main()

