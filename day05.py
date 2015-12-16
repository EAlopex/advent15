#!/usr/bin/env python3

with open("input_day05.txt", "r") as infile:
    data = infile.read().splitlines()

number_of_cute_strings = 0

for string in data:
    if "ab" in string or "cd" in string or "pq" in string or "xy" in string:
        continue
    number_of_vowels = 0
    number_of_doubles = 0
    for i in range(len(string)):
        if string[i] in "aeiou":
            number_of_vowels += 1
        if i>0 and string[i]==string[i-1]:
            number_of_doubles += 1
        if number_of_vowels >= 3 and number_of_doubles >=1:
            number_of_cute_strings += 1
            break

print(number_of_cute_strings)