cals = 0
fatElf = 0
with open("./input.txt", "r", encoding="utf8") as read_file:
    for line in read_file:
        if line.strip() == "":
            fatElf = max(fatElf, cals)
            cals = 0
            continue
        cals += int(line.strip())
print("Fat Elf calories: "+str(fatElf))
