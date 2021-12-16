#!/usr/bin/python3

from aoc import *

def solve(input_str):
    p = Parser(''.join(f'{int(n,16):04b}' for n in input_str.strip()))
    outer ,= p.parse()

    return (p.ver, outer[2])


class Parser:
    def __init__(self, data):
        self.data = data
        self.bits_read = 0
        self.ver = 0

    def read(self, n):
        self.bits_read += n
        bits, self.data = self.data[:n], self.data[n:]
        return bits

    def readint(self, n):
        return int(self.read(n), 2)

    def parse(self, num_bits=None, num_packets=1):
        start = self.bits_read
        packets = []

        if num_bits != None:
            num_packets = None

        while True:
            v = self.readint(3)
            t = self.readint(3)
            self.ver += v

            if t == 4:
                chunks = []

                while True:
                    chunk = self.read(5)
                    chunks.append(chunk[1:])
                    if chunk[0] == '0':
                        break

                val = int(''.join(chunks), 2)

            else:
                i = self.readint(1)

                if i == 0:
                    l = self.readint(15)
                    s = self.parse(num_bits=l)
                else:
                    l = self.readint(11)
                    s = self.parse(num_packets=l)

                if t == 0:
                    val = sum(num for _,_,num in s)
                elif t == 1:
                    val = reduce(lambda a,x:a*x, (n for _,_,n in s), 1)
                elif t == 2:
                    val = min(num for _,_,num in s)
                elif t == 3:
                    val = max(num for _,_,num in s)
                elif t == 5:
                    val = int(s[0][2] > s[1][2])
                elif t == 6:
                    val = int(s[0][2] < s[1][2])
                elif t == 7:
                    val = int(s[0][2] == s[1][2])

            packets.append((v, t, val))
        
            if num_bits and (self.bits_read - start) >= num_bits:
                break

            if num_packets and len(packets) >= num_packets:
                break

        return packets

def main():
    answer = solve(get_input(__file__))
    print(answer)
    assert answer == (904, 200476472872)

if __name__ == '__main__':
    main()

