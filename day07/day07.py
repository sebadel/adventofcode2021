#!/usr/bin/env python

import math
import numpy
import time


def part1(data):
    positions = [int(x) for x in data[0].split(',')]
    min_cost = None
    for x in range(min(positions), max(positions)+1):
        cost = sum([abs(p - x) for p in positions])
        min_cost = min(min_cost, cost) if min_cost else cost
    return min_cost


def _cost(x, y): # 176 secs
    cost = 0
    step = 1
    if y < x:
        x, y = y, x
    while(x != y):
        x += 1
        cost += step
        step += 1
    return cost


def part2(data):
    positions = [int(x) for x in data[0].split(',')]
    costs = {}
    for x in range(min(positions), max(positions)+1):
        costs[x] = sum([_cost(x,p) for p in positions])
    min_cost = min(costs.values())
    for pos, cost in costs.items():
        if cost == min_cost:
            return min_cost


def part3(data): # 0.025 secs
    positions = [int(x) for x in data[0].split(',')]
    center = math.floor(numpy.mean(positions))
    fuel = 0
    for p in positions:
        for c, _ in enumerate(range(min(p, center), max(p, center)+1)):
            fuel += c
    return fuel


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    start = time.perf_counter()
    print('Part 1: %s' % part1(data), end=' ')
    print ('[%05f secs]' % (time.perf_counter() - start))

    # start = time.perf_counter()
    # print('Part 2b: %s' % part2b(data), end=' ')
    # print ('[%05f secs]' % (time.perf_counter() - start))

    start = time.perf_counter()
    print('Part 3: %s' % part3(data), end=' ')
    print ('[%05f secs]' % (time.perf_counter() - start))


if __name__ == "__main__":
    main()
