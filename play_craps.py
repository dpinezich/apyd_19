#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Craps is a dice game developed in the United States and has its origin from the western game 'hazard'.
For more information please have a look at: https://en.wikipedia.org/wiki/Craps.
This short code does not cover all known rules but gives a playable version at hand.
"""

from random import randrange


def roll():
    roll = randrange(1, 7) + randrange(1, 7)
    return roll


def is_game_won_after_first_roll(first_roll):
    new_roll = roll()
    while new_roll != 7 or new_roll != first_roll:
        if new_roll == 7:
            return False
        elif new_roll == first_roll:
            return True
        else:
            new_roll = roll()


def is_game_won():
    first_roll = roll()
    if first_roll == 2 or first_roll == 3 or first_roll == 12:
        return False
    elif first_roll == 7 or first_roll == 11:
        return True
    else:
        return is_game_won_after_first_roll(first_roll)


def sim_games(n):
    wins = losses = 0
    for i in range(n):
        if is_game_won():
            wins += 1
        else:
            losses += 1
    return wins, losses


def main():
    n = eval(input("How many games of craps would you like to play? "))
    wins, losses = sim_games(n)

    print("wins: " + str(wins) + " losses: " + str(losses))


main()
