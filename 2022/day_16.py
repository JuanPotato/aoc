#!/usr/bin/python3

from aoc import *
import math

def solve(input_str):
    tnl = {}
    rts = {}
    for l in lines(input_str):
        rate = ints(l)[0]
        f,*t = re.findall('[A-Z]{2}', l)
        tnl[f] = t
        rts[f] = rate

    # bbs (big brain strat) #1
    # I calculated a cost matrix to get the time it takes to travel between
    # any two valves. This way you can assume each valve is connected to all
    # others, just with different sized tunnels.
    cost_matrix = defaultdict(dict)
    for frm,tos in tnl.items():
        for to in tos:
            cost_matrix[frm][to] = 1

    # there might be a better way to do this but who cares lol
    changed = True
    while changed:
        changed = False
        for frm, frm_costs in cost_matrix.items():
            for to, to_cost in list(frm_costs.items()):
                for toto, toto_cost in cost_matrix[to].items():
                    if frm_costs.get(toto, math.inf) > (to_cost + toto_cost):
                        changed = True
                        frm_costs[toto] = to_cost + toto_cost

    # bbs #2
    # I turned the amount of pressure relief we get from a valve into a single
    # number which is the total pressure relief you would get from a valve
    # given the current time, and your index.
    # Basically this is just taking the pressure of the valve and * by time
    # left once you travel and open it
    def benefit(time_left, you, target):
        cost = cost_matrix[you][target] + 1
        return rts[target] * max(0, time_left - cost)

    # This function just returns all possible valves you could open from your
    # current position, and given the current time, what total pressure relief
    # they would give. Any valves giving 0 pressure relief are pruned here.
    def options(time, you, open):
        benefits = {t:benefit(time, you, t) for t in tnl}
        for o in open:
            benefits[o] = 0
        for t,v in list(benefits.items()):
            if not v:
                benefits.pop(t)

        return benefits

    # Finally the function that will find the optimal selection of valves to open.
    # This is essentially dijkstra's? Maybe?
    #
    # It's BFS but sorted so that I sort the paths based on the current total
    # pressure they have managed to achieve. Paths with pressures that are so
    # low that they could never beat the current best pressure are dropped. So
    # by improving on the best paths first, we are able to quickly prune the rest.
    #
    # function also takes in a list of valves that are already open.
    # It's a surprise tool that will help us later 
    def best_score(total_time, start_valve, not_allowed=tuple()):
        # time, presure, loc, open
        q = [(total_time, 0, start_valve, not_allowed)]
        best = 0
        done_valves = None

        while q:
            # Sort pressures highest to lowest
            q.sort(key=lambda x:-x[1])
            tim, pres, loc, open = q.pop(0)
            my_options = options(tim, loc, open)

            # bbs #3
            # If this path could instantly visit all valves and open them and
            # still not do as well as the best, drop it.
            # There is likely a better upper bound to do this test with but this works really well.
            # Drops execution time by 10x
            if pres + sum(my_options.values()) < best:
                continue

            for opt, new_pres in my_options.items():
                new_time = tim - cost_matrix[loc][opt] - 1
                if new_time < 0:
                    continue
                new_open = open + (opt,)
                q.append((new_time, pres + new_pres, opt, new_open))

            if pres > best:
                done_valves = open
            best = max(pres, best)

        # returns best scores and the valves (in order) it did
        return best, done_valves

    part1 = best_score(30, 'AA')[0]
    # Get the best score with 26 minutes
    human = best_score(26, 'AA')
    # Get the best score with 26 minutes again, but don't do the valves we did
    elephant = best_score(26, 'AA', human[1])
    return (part1, human[0] + elephant[0])


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (1754, 2474)

if __name__ == '__main__':
    main()


