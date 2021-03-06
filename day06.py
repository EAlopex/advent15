#!/usr/bin/env python3

import numpy, re

with open("input_day06.txt", "r") as infile:
    data = infile.read().splitlines()

instructions = []
for line in data:
    if "turn off" in line:
        op = "off"
    if "turn on" in line:
        op = "on"
    if "toggle" in line:
        op = "toggle"
    coords = [int(x) for x in re.findall('\d+', line)]
    instructions.append([op] + coords)

lights = numpy.zeros((1000,1000), dtype=bool)

for ins in instructions:
    if ins[0] == "on":
        lights[ins[1]:ins[3]+1,ins[2]:ins[4]+1] = True
    if ins[0] == "off":
        lights[ins[1]:ins[3]+1,ins[2]:ins[4]+1] = False
    if ins[0] == "toggle":
        lights[ins[1]:ins[3]+1,ins[2]:ins[4]+1] = numpy.invert(lights[ins[1]:ins[3]+1,ins[2]:ins[4]+1])

print(sum(sum(lights)))