#!/usr/bin/python3

from aoc import *
from typing import NamedTuple

die_state = 0

def solve(input_str):
    _, p1, _, p2 = ints(input_str)
    return (game(p1, p2), dirac(p1, p2))

def die():
    global die_state
    ret = die_state + 1
    die_state = (die_state + 1) % 100
    return ret

def game(p1, p2):
    global die_state
    die_state = 0

    score1 = 0
    score2 = 0
    die_roll = 0

    while score1 < 1000 and score2 < 1000:
        p1 = ((p1 - 1) + sum((die(), die(), die()))) % 10 + 1
        die_roll += 3
        score1 += p1
        score1, score2 = score2, score1
        p1, p2 = p2, p1

    return min(score1, score2) * die_roll

class Game(NamedTuple):
    p1: int
    p2: int
    score1: int
    score2: int
    p1_turn: bool

    def play(game, three_die_sum):
        p1, p2, score1, score2, p1_turn = game

        if p1_turn:
            p1 = ((p1 - 1) + three_die_sum) % 10 + 1
            score1 += p1
        else:
            p2 = ((p2 - 1) + three_die_sum) % 10 + 1
            score2 += p2

        p1_turn = not p1_turn
        return Game(p1, p2, score1, score2, p1_turn)

def dirac(p1, p2):
    games = {Game(p1, p2, 0,0, True): 1}
    p1_wins = 0
    p2_wins = 0

    turns = Counter(a+b+c for a in (1,2,3) for b in (1,2,3) for c in (1,2,3))

    while games:
        new_games = defaultdict(int)
        for game, count in games.items():
            for turn, turn_count in turns.items():
                next_game = game.play(turn)
                c = count * turn_count

                if next_game.score1 >= 21:
                    p1_wins += c
                elif next_game.score2 >= 21:
                    p2_wins += c
                else:
                    new_games[next_game] += c

        games = new_games

    return max(p1_wins, p2_wins)


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (752247, 221109915584112)

if __name__ == '__main__':
    main()

