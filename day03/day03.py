#!/usr/bin/env python

import copy
import math

def _count(data, position):
  """How many zeroes, how many ones.

   Inspects each entry of an array and counts the occurrences of
   '0' and '1' at a specific position.

   Returns:
    number of zeroes
    number of ones.
  """
  return (
    [line[position] for line in data].count('0'),
    [line[position] for line in data].count('1')
  )


def _most_common_bit(data, position):
  """What is the most common bit at a specific position.

  If equal number of 0s and 1s, return 1.

  Returns:
   int.
  """
  zeroes, ones = _count(data, position)
  return int(zeroes == ones or zeroes < ones)


def part1(data):
  gamma = epsilon = 0
  for x, _ in enumerate(data[0]):
    gamma = gamma * 2 + _most_common_bit(data, x)
    epsilon = epsilon * 2 + int(not _most_common_bit(data, x))
  print(gamma)
  return gamma * epsilon


def _bit_criteria(data, pos, rating='oxygen'):
  if rating == 'oxygen':
    return list(filter(
        lambda x: int(x[pos]) == _most_common_bit(data, pos),
        data))
  return list(filter(
      lambda x: int(x[pos]) != _most_common_bit(data, pos),
      data))


def part2(data):
  o2_data = copy.copy(data)
  co2_data = data
  pos = 0
  while len(o2_data) > 1:
    o2_data = _bit_criteria(o2_data, pos)
    pos += 1
  pos = 0
  while len(co2_data) > 1:
    co2_data = _bit_criteria(co2_data, pos, 'co2')
    pos += 1
  return int(o2_data[0], 2) * int(co2_data[0], 2)


def main():
    data = [line.strip() for line in open('input.txt', 'r').readlines()]
    print('Part 1: %s' % part1(data))
    print('Part 2: %s' % part2(data))


if __name__ == "__main__":
    main()
