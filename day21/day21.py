#!/usr/bin/env python

import time
import copy
from functools import lru_cache

class Player():
    def __init__(self, name, position, max_positions=10):
        self.name = name
        self.position = position
        self.score = 0
        self.played = 0
        self.max_positions = max_positions

    def play(self, die_total):
        self.position += die_total
        if self.position > self.max_positions:
            while self.position > 10:
                self.position -= 10
        self.score += self.position
        self.played += 1

    def win(self):
        return self.score >= 1000

class Die():
    def __init__(self):
        self.cnt = 0
        self.rolled = 0

    def roll(self, x = 3):
        r = 0
        self.rolled += x
        while x > 0:
            self.cnt += 1
            if self.cnt > 100:
                self.cnt = 1
            r += self.cnt
            x -= 1
        return r


def part1(data):
    players = []
    die = Die()
    for p in data:
        players.append(Player(p.split(':')[0], int(p.split(':')[1])))
    game_on = True
    turns = 0
    while game_on:
        p = players[turns % len(players)]
        p.play(die.roll())
        if p.win():
            game_on = False
        turns += 1
    output = players[(turns) % len(players)].score * die.rolled
    return output



TARGET_SCORE = 21


@lru_cache(maxsize=None)
def play(p1_position, p1_score, p2_position, p2_score,
         turn, dice_roll, dice_sum):
#    print('[P%d] roll:%d sum: %d [%d - %d] [%d - %d]' % (
#        turn, dice_roll, dice_sum,
#        p1_position, p1_score, p2_position, p2_score))
    p1_wins = 0
    p2_wins = 0
    players = [
        {'position': p1_position, 'score': p1_score},
        {'position': p2_position, 'score': p2_score}
    ]
    if dice_roll < 3:
        for i in range(1, 4):
            p1_win, p2_win = play(
                players[0]['position'], players[0]['score'],
                players[1]['position'], players[1]['score'],
                turn, dice_roll + 1, dice_sum + i)
            p1_wins += p1_win
            p2_wins += p2_win
    else:    # dice_roll = 3
        players[turn]['position'] += dice_sum
        if players[turn]['position'] > 10:
            players[turn]['position'] -= 10
        players[turn]['score'] += players[turn]['position']
        if players[0]['score'] >= TARGET_SCORE:
            p1_wins += 1
        elif players[1]['score'] >= TARGET_SCORE:
            p2_wins += 1
        else:
            p1_win, p2_win = play(
                players[0]['position'], players[0]['score'],
                players[1]['position'], players[1]['score'],
                (turn + 1) % 2, dice_roll=0, dice_sum=0)
            p1_wins += p1_win
            p2_wins += p2_win
    return p1_wins, p2_wins


def part2(data):
    positions = []
    for p in data:
        positions.append(int(p.split(':')[1]))
    p1_wins, p2_wins = play(positions[0], 0, positions[1], 0,
                            turn=0, dice_roll=0, dice_sum=0)
    print(p1_wins)
    print(p2_wins)
    return max(p1_wins, p2_wins)



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
