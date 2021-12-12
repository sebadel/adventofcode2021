#!/usr/bin/env python

import copy
import time

options = []
def _next(path, paths):
    for p in paths:
#        print('%s + %s?' % ([','.join(path)], p[1]))
        if p[0] == path[-1]:
            option = copy.copy(path)
            if p[1] == 'end':
                option.append('end')
                if option not in options:
                    options.append(option)
            elif not (p[1].lower() == p[1] and p[1] in path):
                option.append(p[1])
                _next(option, paths)
        elif p[1] == path[-1]:
            if not (p[0].lower() == p[0] and p[0] in path):
                option = copy.copy(path)
                option.append(p[0])
                _next(option, paths)


def _can_visit(path, cave):
    if cave == 'end' or cave == 'start':
        return False
    if cave.upper() == cave:
        return True
    if path.count(cave) > 1: # visited twice already
        return False
    small_caves = list(filter(lambda x: x.lower() == x, path))
    if len(small_caves) > len(set(small_caves)) and path.count(cave) > 0: # Already have 1 double.
        return False
    return True


def _next2(path, paths):
    for p in paths:
        option = copy.copy(path)
        if p[0] == path[-1]:
            if p[1] == 'end':
                option.append('end')
                if option not in options:
                    options.append(option)
            elif _can_visit(option, p[1]):
                option.append(p[1])
                _next2(option, paths)
        elif p[1] == path[-1]:
            if _can_visit(option, p[0]):
                option.append(p[0])
                _next2(option, paths)


def part1(data):
    paths = []
    for line in data:
        a, b = line.split('-')
        if a == 'end' or b == 'start':
            a, b = b, a
        paths.append([a, b])
    for p in paths:
        if p[0] == 'start':
            option = [p[0], p[1]]
            _next(option, paths)
    return len(options)


def part2(data):
    paths = []
    for line in data:
        a, b = line.split('-')
        if a == 'end' or b == 'start':
            a, b = b, a
        paths.append([a, b])
    for p in paths:
        if p[0] == 'start':
            option = [p[0], p[1]]
            _next2(option, paths)
#    print('\n'.join([','.join([o for o in option]) for option in options]))
    return len(options)


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    start = time.perf_counter()
    print('Part 1: %s' % part1(data), end=' ')
    print ('[%05f secs]' % (time.perf_counter() - start))
    options = []
    start = time.perf_counter()
    print('Part 2: %s' % part2(data), end=' ')
    print ('[%05f secs]' % (time.perf_counter() - start))


if __name__ == "__main__":
    main()
