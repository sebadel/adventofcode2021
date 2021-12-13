#!/usr/bin/env python

import time

def display(coords):
    x = y = 0
    max_x = max([coord[0] for coord in coords])
    max_y = max([coord[1] for coord in coords])
    while y <= max_y:
        x = 0
        while x <= max_x:
            if [x, y] in coords:
                print('#', end='')
            else:
                print(' ', end='')
            x+=1
        print()
        y += 1

def parser(data):
    coords = []
    foldings = []
    for line in data:
        if ',' in line:
            coords.append([int(x) for x in line.split(',')])
        elif '=' in line:
            folding = line.split('=')
            folding[0] = folding[0].split(' ')[-1]
            folding[1] = int(folding[1])
            foldings.append(folding)
    return coords, foldings


def fold(fold, coords):
    folded = []
    for coord in coords:
        x, y = coord
        if fold[0] == 'x':
            if x > fold[1]:
                coord = [fold[1] - (x-fold[1]), y]
        elif fold[0] == 'y':
            if y > fold[1]:
                coord = [x, fold[1] - (y-fold[1])]
        if coord not in folded:
            folded.append(coord)
    return folded


def part1(data):
    coords, foldings = parser(data)
    coords = fold(foldings[0], coords)
    return len(coords)


def part2(data):
    coords, foldings = parser(data)
    for folding in foldings:
        coords = fold(folding, coords)
    display(coords)
    return 0


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
