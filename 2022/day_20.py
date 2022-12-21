#!/usr/bin/python3

from aoc import *
from dataclasses import dataclass

@dataclass
class Node:
    data: int
    next: 'Node'
    prev: 'Node'

    def move_after(self, other: 'Node'):
        if self is other or other.next is self:
            return

        self.next.prev = self.prev
        self.prev.next = self.next

        self.next = other.next
        self.prev = other

        other.next.prev = self
        other.next = self

    def move(self, n):
        target = self

        if n > 0:
            for _ in range(n):
                target = target.next
            self.move_after(target)

        if n < 0:
            for _ in range(-n+1):
                target = target.prev
            self.move_after(target)

    def __repr__(self):
        return f'Node(data={self.data}, next={self.next.data}, prev={self.prev.data})'

def solve(input_str):
    return mix(input_str, 1, 1), mix(input_str, 811589153, 10)

def mix(input_str, key=1, rounds=1):
    nodes = [Node(n * key, None, None) for n in ints(input_str)]
    N = len(nodes)
    zero = next(n for n in nodes if n.data == 0)

    for i in range(len(nodes)):
        nodes[i].next = nodes[(i + 1) % N]
        nodes[i].prev = nodes[(i - 1) % N]

    for _ in range(rounds):
        for n in nodes:
            d = n.data % (N - 1)
            d = d - ((N - 1) * (2 * d >= N))
            n.move(d)

    s = 0
    nn = zero
    for _ in range(3):
        for _ in range(1000):
            nn = nn.next
        s += nn.data
    return s

def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (7153, 6146976244822)

if __name__ == '__main__':
    main()

