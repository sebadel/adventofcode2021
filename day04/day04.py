#!/usr/bin/env python


class Board():
  def __init__(self, five_lines):
    self.b = []
    for line in five_lines:
      line = line.replace('  ', ' ')
      self.b.extend([int(x) for x in line.split(' ')])

  @property
  def _lines(self):
    lines = []
    i = 0
    while i < len(self.b):
      lines.append(self.b[i:i+5])
      i += 5
    return lines

  @property
  def _columns(self):
    columns = []
    for x, _ in enumerate(self._lines[0]):
      columns.append([l[x] for l in self._lines])
    return columns

  def winning(self, numbers):
    for line in self._lines:
      if set(line).issubset(numbers):
        return True
    for col in self._columns:
      if set(col).issubset(numbers):
        return True
    return False

  def display(self):
    for line in self._lines:
      print(' '.join(['%2s' % x for x in line]))

  def sum_unmarked(self, numbers):
    return sum([x for x in self.b if x not in set(numbers)])


def CreateBoards(data):
  boards = lines = []
  for line in data:
    if line:
      lines.append(line)
    if len(lines) == 5:
      boards.append(Board(lines))
      lines = []
  return boards

def part1(data):
  numbers = [int(x) for x in data[0].split(',')]
  boards = CreateBoards(data[2:])
  draw = []
  for n in numbers:
    draw.append(n)
    for board in boards:
      if board.winning(draw):
        return board.sum_unmarked(draw) * n


def part2(data):
  numbers = [int(x) for x in data[0].split(',')]
  boards = CreateBoards(data[2:])
  draw = []
  for n in numbers:
    draw.append(n)
    for board in boards:
      if board.winning(draw):
        if len(boards) == 1:
          return boards[0].sum_unmarked(draw) * n
        else:
          print('remove this board from %d boards' % len(boards))
          boards.remove(board)



def main():
  data = [line.strip() for line in open('input.txt', 'r').readlines()]
  print('Part 1: %s' % part1(data))
  print('Part 2: %s' % part2(data))


if __name__ == "__main__":
  main()