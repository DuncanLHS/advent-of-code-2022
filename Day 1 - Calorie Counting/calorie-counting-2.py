cals = 0
elves = []
with open("./input.txt", "r", encoding="utf8") as read_file:
    for line in read_file:
        if line.strip() == "":
            elves.append(cals)
            cals = 0
            continue
        cals += int(line.strip())
elves.sort(reverse=True)
print(sum(elves[0:3]))
