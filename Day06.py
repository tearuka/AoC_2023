#!/usr/bin/env python
# coding: utf-8

import re

# read and parse input
time, distance = open("inp/input_06.txt").read().splitlines()
time = re.findall(r'\d+', time)
distance = re.findall(r'\d+', distance)


def find_ways_to_win(max_time, max_distance):
    
    ways_to_win = 0

    for button_hold_time in range(max_time):
        speed = button_hold_time
        time_left = max_time - button_hold_time
        dist = speed * time_left
        if dist > max_distance:
            ways_to_win += 1

    return ways_to_win


def compute_wins(time, distance, part):
    
    if part == 1:
        race_time = [int(num) for num in time]
        race_distance = [int(num) for num in distance]
        final_score = 1
        for race_number in range(len(race_time)):
            final_score *= find_ways_to_win(race_time[race_number], race_distance[race_number])
    
    if part == 2:
        race_time = int(''.join(time))
        race_distance = int(''.join(distance))
        final_score = find_ways_to_win(race_time, race_distance)
    
    return final_score
        

# part 1
print("Result for part 1: ", compute_wins(time, distance, 1))  # 170000

# part 2
print("Result for part 2: ", compute_wins(time, distance, 2))  # 20537782