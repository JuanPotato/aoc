#!/usr/bin/python3

from aoc import *
import itertools


def solve(input_str: str):
    return part1(input_str), part2(input_str)


def part2(input_str: str):
    blocks = []
    file = True
    i = 0
    for c in input_str.strip():
        if file:
            blocks.append((i, int(c)))
            i += 1
        else:
            blocks.append((".", int(c)))
        file = not file

    i = len(blocks) - 1
    while i > 0:
        block_id, block_cnt = blocks[i]
        if block_id == ".":
            i -= 1
            continue

        for dst in (j for j in range(0, i) if (bb := blocks[j])[0] == '.' and bb[1] >= block_cnt):
            if blocks[dst][1] > block_cnt:
                blocks[i] = (".", block_cnt)
                blocks[dst] = (".", blocks[dst][1] - block_cnt)
                blocks.insert(dst, (block_id, block_cnt))
                i += 1
                break

            elif blocks[dst][1] == block_cnt:
                blocks[dst] = (block_id, block_cnt)
                blocks[i] = (".", blocks[dst][1])
                break

        i -= 1

    chck = 0
    i = 0
    for block_id, cnt in blocks:
        if block_id == ".":
            i += cnt
            continue
        for _ in range(cnt):
            chck += i * block_id
            i += 1

    return chck


def part1(input_str: str):
    blocks = deque()
    file = True
    i = 0
    for c in input_str.strip():
        if file:
            blocks.append((i, int(c)))
            i += 1
        else:
            blocks.append((".", int(c)))
        file = not file

    new_blocks = []
    back_id, back_cnt = None, None
    while blocks:
        front_id, front_cnt = blocks.popleft()
        if front_id == ".":
            while front_cnt > 0:
                if not blocks:
                    break
                while back_id == None or back_id == "." or back_cnt == 0:
                    back_id, back_cnt = blocks.pop()
                move_cnt = min(front_cnt, back_cnt)
                if not blocks:
                    move_cnt = back_cnt
                new_blocks.append((back_id, move_cnt))
                front_cnt -= move_cnt
                back_cnt -= move_cnt
        else:
            new_blocks.append((front_id, front_cnt))
    if back_cnt > 0:
        new_blocks.append(back_id, back_cnt)

    chck = 0
    i = 0
    for block_id, cnt in new_blocks:
        for _ in range(cnt):
            chck += i * block_id
            i += 1

    return chck


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (6291146824486, 6307279963620)


if __name__ == "__main__":
    main()
