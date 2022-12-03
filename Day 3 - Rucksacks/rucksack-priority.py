import math
import string
values = dict()
uppervalues = dict()
total = 0

for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index + 1
for index, letter in enumerate(string.ascii_uppercase):
    uppervalues[letter] = index + 27
values.update(uppervalues)

with open("./input.txt", "r", encoding="utf8") as read_file:
    for line in read_file:
        half = math.floor(len(line)/2)
        comp1 = set(list(line[:half].strip()))
        comp2 = set(list(line[half:].strip()))
        common = comp1 & comp2
        for item in common:
            total += values[item]
print(total)
