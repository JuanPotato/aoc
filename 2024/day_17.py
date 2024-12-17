#!/usr/bin/python3

from aoc import *


def solve(input_str: str):
    a, b, c, *program = ints(input_str)
    part1 = computer(a, b, c, program)
    do_program = lambda a: computer(a, b, c, program)
    part2 = create_a(program, do_program)
    return (",".join(map(str, part1)), part2)


# a planck weight of clever for part2
def create_a(expected, do_program, a_sofar=0):
    if not expected:
        return a_sofar

    for i in range(not a_sofar, 8):
        test_a = (a_sofar << 3) + i
        res = do_program(test_a)
        if res[0] == expected[-1]:
            new_a = create_a(expected[:-1], do_program, test_a)
            if new_a != None:
                return new_a


# nothing clever, just the computer
def computer(a, b, c, program):
    def value(op):
        match op:
            case 0 | 1 | 2 | 3:
                return op
            case 4:
                return a
            case 5:
                return b
            case 6:
                return c

    ip = 0
    output = []

    while ip < len(program):
        opcode = program[ip]
        literal = program[ip + 1]
        combo = value(literal)
        match opcode:
            case 0:  # adv
                a = int(a / (2**combo))

            case 6:  # bdv
                b = int(a / (2**combo))

            case 7:  # cdv
                c = int(a / (2**combo))

            case 1:  # bxl
                b = b ^ literal

            case 2:  # bst
                b = combo % 8

            case 3:  # jnz
                if a != 0:
                    ip = literal - 2

            case 4:  # bxc
                b = b ^ c

            case 5:  # out
                output.append(combo % 8)

        ip += 2

    return output


def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == ("1,5,0,1,7,4,1,0,3", 47910079998866)


if __name__ == "__main__":
    main()
