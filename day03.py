#!/usr/bin/env python3

with open("input_day03.txt", "r") as infile:
    raw_data = infile.read()

visited_locations = [(0,0)]

for char in raw_data:
    lat, lon = visited_locations[-1]
    if char == "^":
        lat += 1
    if char == "v":
        lat -= 1
    if char == "<":
        lon += 1
    if char == ">":
        lon -= 1
    visited_locations.append((lat,lon))

print(len(set(visited_locations)))