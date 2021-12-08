#!/usr/bin/env python

import time

def part1(data):
    cnt = 0
    for line in data:
        a, b = line.split(' | ')
        values = b.split(' ')
        for v in values:
            if len(v) in [2, 3, 4, 7]:
                cnt += 1
    return cnt


def part2(data):
    cnt = 0
    for line in data:
        a, b = line.split(' | ')
        code = ['', '', '', '', '', '', '', '', '', '']
        a = [set(x) for x in a.split(' ')]
        code[1] = list(filter(lambda v: len(v) == 2, a))[0]
        code[4] = list(filter(lambda v: len(v) == 4, a))[0]
        code[7] = list(filter(lambda v: len(v) == 3, a))[0]
        code[8] = list(filter(lambda v: len(v) == 7, a))[0]

        code[9] = list(filter(lambda v: len(v) == 6 and code[4].issubset(v), a))[0]
        code[6] = list(filter(lambda v: len(v) == 6 and not code[1].issubset(v), a))[0]
        code[0] = list(filter(lambda v: len(v) == 6 and v != code[9] and v != code[6], a))[0]

        code[5] = list(filter(lambda v: len(v) == 5 and v.issubset(code[6]), a))[0]
        code[2] = list(filter(lambda v: len(v) == 5 and not code[1].issubset(v) and not v.issubset(code[6]), a))[0]
        code[3] = list(filter(lambda v: len(v) == 5 and v != code[5] and v != code[2], a))[0]

        numbers = [set(v) for v in b.split(' ')]
        x = 0
        for n in numbers:
            x = x*10 + code.index(n)
        cnt += x
    return cnt


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    start = time.perf_counter()
    print('Part 1: %s' % part1(data), end=' ')
    print ('[%05f secs]' % (time.perf_counter() - start))
    start = time.perf_counter()
    print('Part 2: %s' % part2(data), end=' ')
    print ('[%05f secs]' % (time.perf_counter() - start))


if __name__ == "__main__":
    main()
