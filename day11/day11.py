#!/usr/bin/env python

import time
import copy

def _neighbors(x, ln):
    # find neighbors of a cell
    n = []
    n.extend([x-10, x+10]) # top, bottom
    if x%10 != 9: # not right
        n.extend([x-9, x+1, x+11])
    if x%10 != 0: # not left
        n.extend([x-1, x-11, x+9])
    n = list(set(n))
    n = filter(lambda x: x>=0 and x<ln, n)
    return n


def flash(c, lights):
    # flash a cell and reflects on its neighbors.
    lights[c] = 0
    for n in _neighbors(c, len(lights)):
        if lights[n] != 0:
            lights[n] += 1


def part1(data):
    lights = []
    flashes = 0
    for line in data:
        lights.extend([int(x) for x in line])
    step = 0
    while step < 100:
        lights = [x+1 for x in lights]
        while max(lights) > 9: # there are still cells to flash
            for c in [i for i, x in enumerate(lights) if x > 9]:
                flash(c, lights)
        flashes += lights.count(0)
        step += 1
    return flashes


def part2(data):
    lights = []
    for line in data:
        lights.extend([int(x) for x in line])
    step = 0
    while lights.count(0) != len(lights):
        lights = [x+1 for x in lights]
        while max(lights) > 9:
            to_flash = [i for i, x in enumerate(lights) if x > 9]
            for c in to_flash:
                flash(c, lights)
        step += 1
    return step


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
