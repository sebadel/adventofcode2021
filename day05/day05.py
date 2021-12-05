#!/usr/bin/env python


def vent_positions(x1, y1, x2, y2, diagonal=False):
    positions = []
    if x1 == x2: # hortizontal
        if y1 > y2:
            y1, y2 = y2, y1
        while y1 <= y2:
            positions.append('%s,%s' % (x1, y1))
            y1 += 1

    elif y1 == y2: # vertical
        if x1 > x2:
            x1, x2 = x2, x1
        while x1 <= x2:
            positions.append('%s,%s' % (x1, y1))
            x1 += 1

    elif diagonal and x1 != x2 and y1 != y2: # diagonal
        positions.append('%s,%s' % (x1, y1))
        while x1 != x2:
            x1 = x1 + 1 if x1 < x2 else x1 - 1
            y1 = y1 + 1 if y1 < y2 else y1 - 1
            positions.append('%s,%s' % (x1, y1))

    return positions


def part1(data, diagonal=False):
    coords = {}
    for line in data:
        x1, y1, x2, y2 = line.replace(' -> ', ',').split(',')
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        for pos in vent_positions(x1, y1, x2, y2, diagonal):
            if pos not in coords:
                coords[pos] = 0
            coords[pos] += 1
    return len([x for x in filter(lambda x: x > 1, coords.values())])


def part2(data):
    return part1(data, diagonal = True)

def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %s' % part1(data))
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
