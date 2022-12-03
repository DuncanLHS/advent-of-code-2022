points = 0
with open("./input.txt", "r", encoding="utf8") as read_file:
    for line in read_file:
        match line[0]:
            case "A":
                match line[2]:
                    case "X":
                        points += 0 + 3
                    case "Y":
                        points += 3 + 1
                    case "Z":
                        points += 6 + 2
            case "B":
                match line[2]:
                    case "X":
                        points += 0 + 1
                    case "Y":
                        points += 3 + 2
                    case "Z":
                        points += 6 + 3
            case "C":
                match line[2]:
                    case "X":
                        points += 0 + 2
                    case "Y":
                        points += 3 + 3
                    case "Z":
                        points += 6 + 1

print(points)
