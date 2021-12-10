#!/usr/bin/env python

import time
import copy
import re
import math

SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}



def _first_illegal_character(line):
    """Returns either an illegal character or an incomplete stack."""
    MATCHES = ( ['{', '}'], ['(', ')'], ['<', '>'], ['[', ']'])
    stack = []
    for c in line:
        if stack and [stack[-1], c] in MATCHES: # Remove matching element.
            stack = stack[0:-1]
        elif c in [m[1] for m in MATCHES]: # Next character is illegal
             return c, None
        else: # Next character is an open char.
            stack.append(c)
    return None, stack # Returns incomplete stack


def part1(data):
    total = 0
    for line in data:
        fil, _ = _first_illegal_character(line)
        if fil:
            total += SCORES[fil]
    return total


def part2(data):
    SCORES = ['(', '[', '{', '<']
    totals = []
    for line in data:
        _, incomplete = _first_illegal_character(line)
        if incomplete:
            score = 0
            while incomplete:
                c = incomplete.pop()
                score = (score * 5) + SCORES.index(c) + 1
            totals.append(score)
    totals = sorted(totals)
    return totals[int(len(totals)/2)]


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
