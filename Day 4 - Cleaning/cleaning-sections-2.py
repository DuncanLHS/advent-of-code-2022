pair = []


def isOverlapping(list1, list2):
    if (list1[0] <= list2[0] and list1[1] >= list2[0]) or (list2[0] <= list1[0] and list2[1] >= list1[0]):
        return True
    else:
        return False


with open("./input.txt", "r", encoding="utf8") as read_file:
    count = 0
    for line in read_file:
        pair = line.strip().split(",")
        elf1 = pair[0].split("-")
        elf2 = pair[1].split("-")
        elf1 = [int(elf1[0]), int(elf1[1])]
        elf2 = [int(elf2[0]), int(elf2[1])]
        if isOverlapping(elf1, elf2):
            count += 1

print(isOverlapping([1, 5], [3, 8]))
print(count)
