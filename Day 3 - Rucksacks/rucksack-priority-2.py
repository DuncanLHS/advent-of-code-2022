import math
import string
from itertools import islice
values = dict()
uppervalues = dict()
total = 0

for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
    uppervalues[letter] = index + 27
values.update(uppervalues)

with open("./input.txt", "r", encoding="utf8") as read_file:
    while True:
        lines = list(islice(read_file, 3))
        if len(lines) <= 0:
            break
        bag1 = set(list(lines[0].strip()))
        bag2 = set(list(lines[1].strip()))
        bag3 = set(list(lines[2].strip()))
        common = bag1 & bag2 & bag3
        for item in common:
            # print(item)
            total += values[item]
print(total)
