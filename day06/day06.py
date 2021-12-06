#!/usr/bin/env python

from collections import Counter

def part1(data):
    fishes = [int(x) for x in data[0].split(',')]
    day = 1
    while day <= 80:
        new_fishes = []
        c = 0
        while c < len(fishes):
            if fishes[c] == 0:
                fishes[c] = 6
                new_fishes.append(8)
            else:
                fishes[c] -=1
            c += 1
        fishes.extend(new_fishes)
        day += 1
    return len(fishes)


def part2(data):
    fishes = sorted(data[0].replace(',', ''))
    day = 1
    timers =[0, 0, 0, 0, 0, 0, 0, 0, 0]
    for fish in fishes:
        timers[int(fish)] += 1
    while day <= 256:
        new = timers.pop(0)
        timers[6] += new
        timers.append(new)
        day += 1
    return sum(timers)

def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %s' % part1(data))
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
# 504500683588 too low
# 1644874076764