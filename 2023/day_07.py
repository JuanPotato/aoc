from aoc import *
from functools import cmp_to_key


def solve(input_str):
    cards = {ll[0]: int(ll[1]) for l in input_str.split("\n") if (ll := l.split(" "))}
    part1 = play(cards, cmp_hand1)
    part2 = play(cards, cmp_hand2)
    return part1, part2


def play(cards, cmp):
    hands = sorted(cards.keys(), key=cmp_to_key(cmp))
    return sum(cards[h] * (i + 1) for i, h in enumerate(hands))


def cmp_hand1(h1, h2):
    return cmp_hand(h1, h2, "23456789TJQKA", score)


def cmp_hand2(h1, h2):
    return cmp_hand(h1, h2, "J23456789TQKA", score2)


def cmp_hand(h1, h2, points_str, score_func):
    if s := sign(score_func(h1) - score_func(h2)):
        return s
    else:
        for c1, c2 in zip(h1, h2):
            if s := sign(points_str.index(c1) - points_str.index(c2)):
                return s
        return 0


def sign(n):
    return 0 if n == 0 else n // abs(n)


def score2(hand):
    return max(score(hand.replace("J", nc)) for nc in "23456789TQKA")


def score(hand):
    match tuple(sorted(Counter(hand).values())):
        case (5,):
            return 6
        case (1, 4):
            return 5
        case (2, 3):
            return 4
        case (1, 1, 3):
            return 3
        case (1, 2, 2):
            return 2
        case (1, 1, 1, 2):
            return 1
        case (1, 1, 1, 1, 1):
            return 0
        case _:
            raise ValueError("!")


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (254024898, 254115617)


if __name__ == "__main__":
    main()
