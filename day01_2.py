#!/usr/bin/env python3

with open("input_day01.txt", "r") as infile:
    raw_text = infile.read()

flr = 0
pos = 0

for char in raw_text:
    if char == "(":
        flr += 1
        pos += 1 
    if char == ")":
        flr -= 1
        pos += 1
    if flr == -1:
        break
print(pos)