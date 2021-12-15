#!/usr/bin/env python

import copy
import time
import math
from functools import lru_cache

def _replace(s, swaps):
    n = ''
    i = 0
    while i < len(s)-1:
        sub = '%s%s' % (s[i], s[i+1])
        if sub in swaps:
            n = '%s%s%s' % (n, s[i], swaps[sub])
        else:
            n = '%s%s' % (n, s[i])
        i += 1
    n += s[-1]
    return n

def char_count(p):
    counters = {}
    for c in p:
        if c not in counters:
            counters[c] = 0
        counters[c] += 1
        if counters[c] >= max(counters.values()):
            max_c = counters[c]
        if counters[c] <= min(counters.values()):
            min_c = counters[c]
    print(counters)
    return max_c - min_c

def parse(data):
    p = data[0]
    swaps = {}
    for x in data[2:]:
        a, b = x.split(' -> ')
        swaps[a] = b
    return p, swaps


def part1(data):
    p, swaps = parse(data)
    step = 1
    while step <= 10:
        p = _replace(p, swaps)
        print('%d: %d' % (step, len(p)))
        step += 1
    return char_count(p)


def part2(data):
    p, swaps = parse(data)
    i = 0
    pairs = {}
    while i < len(p)-1:
        pair = p[i] + p[i+1]
        if pair not in pairs:
            pairs[pair] = 0
        pairs[pair] += 1
        i += 1
    print(swaps)
    print(pairs)
    steps = 40
    while steps > 0:
        ppairs = {}
        for pair, cnt in pairs.items():
            if pair not in swaps:
                ppairs[pair] = cnt
            else:
#                ppairs[pair] = 0
                pair1 = pair[0] + swaps[pair]
                pair2 = swaps[pair] + pair[1]

                if pair1 in ppairs:
                    ppairs[pair1] += cnt
                else:
                    ppairs[pair1] = cnt

                if pair2 in ppairs:
                    ppairs[pair2] += cnt
                else:
                    ppairs[pair2] = cnt
        pairs = copy.copy(ppairs)
        steps -= 1
        print(pairs)

    chars = {}
    for pair in pairs:
        if pair[0] not in chars:
            chars[pair[0]] = 0
        if pair[1] not in chars:
            chars[pair[1]] = 0
        chars[pair[0]] += pairs[pair]
        chars[pair[1]] += pairs[pair]
    for x, cnt in chars.items():
        chars[x] = math.ceil(cnt/2)
    print(chars)
    return(max(chars.values()) - min(chars.values()))
    return char_count(n)


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
