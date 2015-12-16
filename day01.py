#!/usr/bin/env python3

with open("input_day01.txt", "r") as infile:
    raw_text = infile.read()

print(raw_text.count("(")-raw_text.count(")"))