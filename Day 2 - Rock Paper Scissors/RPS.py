points = 0
rounds = []
with open("./input.txt", "r", encoding="utf8") as read_file:
    for line in read_file:
        match line[2]:
            case "X":
                points += 1
                match line[0]:
                    case "A":
                        points += 3
                    case "B":
                        points += 0
                    case "C":
                        points += 6
            case "Y":
                points += 2
                match line[0]:
                    case "A":
                        points += 6
                    case "B":
                        points += 3
                    case "C":
                        points += 0
            case "Z":
                points += 3
                match line[0]:
                    case "A":
                        points += 0
                    case "B":
                        points += 6
                    case "C":
                        points += 3

print(points)
