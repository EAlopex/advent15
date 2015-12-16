#!/usr/bin/env python3

with open("input_day05.txt", "r") as infile:
    data = infile.read().splitlines()

number_of_cute_strings = 0

for string in data:
    contains_a_double_pair = False
    contains_a_distant_pair = False
    for i in range(len(string)):
        if string[i:i+2] in string[i+2:]:
            contains_a_double_pair = True
        if i>1 and string[i]==string[i-2]:
            contains_a_distant_pair = True
        if contains_a_double_pair and contains_a_distant_pair:
            number_of_cute_strings += 1
            break

print(number_of_cute_strings)