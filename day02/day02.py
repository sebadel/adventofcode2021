#!/usr/bin/env python


def part1(data):
    depth = pos = 0
    for line in data:
        move, x = line.split(' ')
        x = int(x)
        if move == 'forward':
            pos += x
        elif move == 'up':
            depth -= x
        elif move == 'down':
            depth  += x
    return pos * depth


def part2(data):
    depth = pos = aim = 0
    for line in data:
        move, x = line.split(' ')
        x = int(x)
        if move == 'forward':
            pos += x
            depth += aim * x
        elif move == 'up':
            aim -= x
        elif move == 'down':
            aim  += x
    return pos * depth


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %s' % part1(data))
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
