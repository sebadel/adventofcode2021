#!/usr/bin/env python


def part1(data):
    cnt = 0
    y = -1
    data = [int(x) for x in data]
    for x in data:
        if y > 0 and x > y:
            cnt += 1
        y = x
    return cnt


def part2(data):
    data = [int(x) for x in data]
    cursor = 0
    sums = []
    while cursor+2 < len(data):
        sums.append(data[cursor] + data[cursor+1] + data[cursor+2])
        cursor += 1
    return part1(sums)


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %s' % part1(data))
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
