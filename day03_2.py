#!/usr/bin/env python3

with open("input_day03.txt", "r") as infile:
    raw_data = infile.read()

clean_data = []
for char in raw_data:
    if char in "^>v<":
        clean_data.append(char)
clean_data = ''.join(clean_data)

visited_locations = [[(0,0)],[(0,0)]]

for i, char in enumerate(clean_data):
    lat, lon = visited_locations[i%2][-1]
    if char == "^":
        lat += 1
    if char == "v":
        lat -= 1
    if char == "<":
        lon += 1
    if char == ">":
        lon -= 1
    visited_locations[i%2].append((lat,lon))

print(len(set(visited_locations[0]+visited_locations[1])))