#!/usr/bin/env python3
import hashlib

secret_key = "iwrupvqb"
number = 0

while True:
    number += 1
    md5 = hashlib.md5((secret_key+str(number)).encode()).hexdigest()
    if md5.startswith("000000"):
        print(number)
        break