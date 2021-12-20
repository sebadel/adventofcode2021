#!/usr/bin/env python

import time


class Grid():
    def __init__(self, algo, data):
        self.algo = algo
        self.data = set()
        for y, line in enumerate(data):
            for x, c in enumerate(line):
                if c == '#':
                    self.data.add((x, y))
        self.xmin = 0
        self.xmax = 0
        self.ymin = 0
        self.ymax = 0
        self.step = 0

    def enhance(self, step):
        self.step = step
        self.xmin = min(x for x, y in self.data)
        self.xmax = max(x for x, y in self.data)
        self.ymin = min(y for x, y in self.data)
        self.ymax = max(y for x, y in self.data)
        pic = set()
        for y in range(self.ymin - 1, self.ymax + 2):
            for x in range(self.xmin - 1, self.xmax + 2):
                if self.algo[self.enhanced_pix(x, y)] == '#':
                    pic.add((x, y))
        self.data = pic

    def is_on_the_border(self, x, y):
        return not (self.xmin <= x <= self.xmax and self.ymin <= y <= self.ymax)

    def enhanced_pix(self, x, y):
        pixel = ''
        for ny in range(y - 1, y + 2):
            for nx in range(x - 1, x + 2):
                if (nx, ny) in self.data:
                    pixel += '1'
                elif self.algo[0] == '#' and self.step % 2 == 1 and self.is_on_the_border(nx, ny):
                    pixel += '1'
                else:
                    pixel += '0'
        return int(pixel, 2)


def part1(data, steps=2):
    algo = data[0]
    grid = Grid(algo, data[2:])
    for step in range(steps):
        grid.enhance(step)
    return len(grid.data)


def part2(data):
    return part1(data, 50)


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
