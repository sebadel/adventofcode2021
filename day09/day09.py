#!/usr/bin/env python

import time
import numpy


def _low_points(data):
    """Returns list of points surrounded by higher values."""
    low_points = []
    for y, line in enumerate(data):
        prev_line = data[y-1] if y>0 else None
        next_line = data[y+1] if y+1 < len(data) else None
        for x, p in enumerate(line):
            left = line[x-1] if x-1 >= 0 else 9
            right = line[x+1] if x+1 < len(line) else 9
            up = prev_line[x] if prev_line else 9
            down = next_line[x] if next_line else 9
            if p < min(up, down, left, right):
                low_points.append([x, y])
    return low_points


def part1(data):
    output = 0
    for x, y in _low_points(data):
        output += 1 + data[y][x]
    return output


def _explore_basin(h, x, y, data):
    """Recursively explore neighbor positions until hitting a limit.

    Returns:
        list of explored coords.
    """
#    print('[%d, %d]: %d vs %d' % (x, y, data[y][x], h))
    if (y not in range(len(data)) or
        x not in range(len(data[0])) or
        data[y][x] == 9 or
        h >= data[y][x]):
        return []
    basin = [(x, y)]
    basin.extend(_explore_basin(data[y][x], x-1, y, data)) # left
    basin.extend(_explore_basin(data[y][x], x+1, y, data)) # right
    basin.extend(_explore_basin(data[y][x], x, y-1, data)) # bottom
    basin.extend(_explore_basin(data[y][x], x, y+1, data)) # top
    return basin


def part2(data):
    sizes = []
    for x, y in _low_points(data):
        basin = set(_explore_basin(data[y][x]-1, x, y, data))
        sizes.append(len(basin))
    return numpy.prod(sorted(sizes)[-3:])


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    for c, l in enumerate(data):
        data[c] = [int(x) for x in l]

    start = time.perf_counter()
    print('Part 1: %s' % part1(data), end=' ')
    print ('[%05f secs]' % (time.perf_counter() - start))
    start = time.perf_counter()
    print('Part 2: %s' % part2(data), end=' ')
    print ('[%05f secs]' % (time.perf_counter() - start))


if __name__ == "__main__":
    main()
