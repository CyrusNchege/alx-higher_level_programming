#!/usr/bin/python3
x = 0
for i in range(10):
    for j in range(x, 10):
        if i == j:
            continue
        if i == 8 and j == 9:
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}".format(i, j), end=", ")
    x = x + 1
