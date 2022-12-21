#!/usr/bin/python3

from aoc import *

from enum import Enum, global_enum
from dataclasses import dataclass
import itertools

ORE = 0
CLAY = 1
OBS = 2
GEO = 3
Mat = (ORE, CLAY, OBS, GEO)

# M1 +0
# M2 +1
# M3 +2
# M4 +3


WIPEOUT = tuple(((m - 1) * m) // 2 for m in range(32 + 1))

@dataclass
class State:
    time: int
    mats: list
    bots: list
    bot_costs: tuple
    limits: tuple
    next_bot: int
    bot_hist: tuple

    def step(self):
        self.mats[0] += self.bots[0]
        self.mats[1] += self.bots[1]
        self.mats[2] += self.bots[2]
        self.mats[3] += self.bots[3]
        self.time -= 1
        return self.time >= 0

    def can(self, bot):
        s = True
        for m in Mat:
            s = s and self.mats[m] >= self.bot_costs[bot][m]
        return s

    def make_bot(self, bot):
        for m,c in enumerate(self.bot_costs[bot]):
            self.mats[m] -= c
        self.bots[bot] += 1
        self.bot_hist += (bot,)

    def make_bots(self, bots):
        for b in bots:
            self.make_bot(b)

    def consider(self, bot):
        s = self.bots[bot] < self.limits[bot]
        for m in Mat:
            s = s and (self.bot_costs[bot][m] == 0 or self.bots[m] > 0)
        return s

def iter_bot_costs(input_str):
    for i,ore_ore_cost,clay_ore_cost,obs_ore_cost,obs_clay_cost,geo_ore_cost,geo_obs_cost in chunk(ints(input_str), 7):
        yield (i, (
            (ore_ore_cost, 0, 0, 0), # ORE
            (clay_ore_cost, 0, 0, 0), # CLAY
            (obs_ore_cost, obs_clay_cost, 0, 0), # OBS
            (geo_ore_cost, 0, geo_obs_cost, 0), # GEO
        ))


def solve(input_str):
    geodes = []
    for i,bot_costs in iter_bot_costs(input_str):
        if i > 3:
            break
        geodes.append(evolve(bot_costs, 32))
    part2 = geodes[0] * geodes[1] * geodes[2]


    quality_levels = []
    for i,bot_costs in iter_bot_costs(input_str):
        quality_levels.append(i * evolve(bot_costs, 24))
    part1 = sum(quality_levels)

    return (part1, part2)

def evolve(bot_costs, time):
    limits = list(max(m) for m in zip(*bot_costs))
    limits[-1] = time
    limits = tuple(limits)
    #print(bot_costs)
    #print(limits)

    mats = [0, 0, 0, 0]
    bots = [1, 0, 0, 0]
    all_states = []

    for todo in Mat:
        all_states.append(State(time, list(mats), list(bots), bot_costs, limits, todo, tuple()))

    best = 0
    n = 0
    while all_states:
        s = all_states.pop()
        make = False

        # I am speed
        if best >= s.mats[GEO] + ((s.bots[GEO] * s.time) + ((s.time - 1) * s.time) // 2):
            continue

        while not make and s.time > 0:
            make = s.can(s.next_bot)
            s.step()
            #print(s.time, s.bot_hist)

        if s.time <= 0:
            # We've reached the end of time
            if s.mats[GEO] > best:
                best = s.mats[GEO]
                #print('Score', best, s.bot_hist)

        elif make:
            # We've got a bot to make
            s.make_bot(s.next_bot)
            for m in Mat:
                if s.consider(m):
                    all_states.append(State(s.time, list(s.mats), list(s.bots), s.bot_costs, s.limits, m, s.bot_hist))

    return best


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (1613, 46816)

if __name__ == '__main__':
    main()

