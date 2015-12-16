#!/usr/bin/env python3

with open("input_day02.txt", "r") as infile:
    raw_data = infile.readlines()

sizes = [[int(size) for size in line.split("x")] for line in raw_data]
print(sum([2*(a+b+c-max(a,b,c)) + a*b*c for a,b,c in sizes]))