#!/usr/bin/env python
# coding: utf-8

# read input
inp = open("inp/input_09.txt").read().splitlines()
inp = [line.split() for line in inp]


def predict_next_value(sequence, part):

    seq = [int(num) for num in sequence]
    last_elements = [seq[-1]] if part == 1 else [seq[0]]
    
    while all(num == 0 for num in seq) == False:
        difference = [seq[i] - seq[i-1] for i in range(1,len(seq))]
        last = difference[-1] if part == 1 else difference[0]
        last_elements.append(last)
        seq = difference

    lst = list(reversed(last_elements))
    
    prediction = 0
    for i in range(len(lst) - 1):
        prediction = (prediction + lst[i+1]) if part == 1 else (lst[i+1] - prediction)
       
    return prediction


def get_sum(input, part):
    suma = 0
    for line in input:
        suma += predict_next_value(line, part)
    return suma
        

# part 1
print("Result for part 1: ", get_sum(inp, 1))  # 2005352194

# part 2
print("Result for part 2: ", get_sum(inp, 2))  # 1077