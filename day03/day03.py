#!/usr/bin/env python

import copy

def part1(data):
    gamma = epsilon = ''
    pos = 0
    while pos < len(data[0]):
        s = ''.join([x[pos] for x in data])
        if s.count('0') >= s.count('1'):
            gamma = '%s%s' % (gamma, 0)
            epsilon = '%s%s' % (epsilon, 1)
        else:
            gamma = '%s%s' % (gamma, 1)
            epsilon = '%s%s' % (epsilon, 0)
        pos += 1
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    output = gamma * epsilon
    return output

def _bit_criteria(data, pos, o=True):
    s = ''.join([x[pos] for x in data])
    if o:
        if s.count('0') > s.count('1'):
            data = filter(lambda x: x[pos] == '0', data)
        else:
            data = filter(lambda x: x[pos] == '1', data)
    else:
        if s.count('0') <= s.count('1'):
            data = filter(lambda x: x[pos] == '0', data)
        else:
            data = filter(lambda x: x[pos] == '1', data)

    print(data)
    return data

def part2(data):
    gamma = epsilon = ''
    o2_data = copy.copy(data)
    co2_data = copy.copy(data)
    pos = 0
    while len(o2_data) > 1:
        o2_data = _bit_criteria(o2_data, pos)
        pos += 1
    pos = 0
    while len(co2_data) > 1:
        co2_data = _bit_criteria(co2_data, pos, False)
        pos += 1

    return int(o2_data[0], 2) * int(co2_data[0], 2)

    output = ''
    for line in data:
        pass
    return output


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %s' % part1(data))
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
