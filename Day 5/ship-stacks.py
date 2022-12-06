stacks = [
    ["Z", "T", "F", "R", "W", "J", "G"],
    ["G", "W", "M"],
    ["J", "N", "H", "G"],
    ["J", "R", "C", "N", "W"],
    ["W", "F", "S", "B", "G", "Q", "V", "M"],
    ["S", "R", "T", "D", "V", "W", "C"],
    ["H", "B", "N", "C", "D", "Z", "G", "V"],
    ["S", "J", "N", "M", "G", "C"],
    ["G", "P", "N", "W", "C", "J", "D", "L"]
]

with open("./input.txt", "r", encoding="utf8") as read_file:
    for line in read_file:
        if line[0:4] == "move":
            imove = int(line.strip().split(" ")[1]) * -1
            ifrom = int(line.strip().split(" ")[3]) - 1
            ito = int(line.strip().split(" ")[5]) - 1

            move = stacks[ifrom][imove:]
            # move.reverse()
            stacks[ifrom] = stacks[ifrom][:imove]
            for item in move:
                stacks[ito].append(item)
for col in stacks:
    print(col[-1], end="")
