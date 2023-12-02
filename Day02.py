#!/usr/bin/env python
# coding: utf-8

import re

# read input
inp = open("inp/input_02.txt").read().splitlines()

def count_cubes(input_file, part):
    game_sum = 0
    for line in input_file:
        game, draws = line.split(": ")
        game_ID = game.replace("Game ","")
        reds = re.findall(r"(\d+) red", draws)
        reds = [int(i) for i in reds]
        greens = re.findall(r"(\d+) green", draws)
        greens = [int(i) for i in greens]
        blues  = re.findall(r"(\d+) blue", draws)
        blues = [int(i) for i in blues]
        if part == 1:
            if max(reds) <= 12 and max(greens) <= 13 and max(blues) <= 14:
                game_sum += int(game_ID)
        if part == 2:
            game_sum += max(reds) * max(greens) * max(blues)
    return game_sum


# part 1
print("Result for part 1: ", count_cubes(inp, 1))  # 2085

# part 2
print("Result for part 2: ", count_cubes(inp, 2))  # 79315