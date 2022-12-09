dirs = {}
dirtotal = 0
total = 0
currentdir = ""
i = 0


def navigate():
    return


def getFileSize(line):
    return int(line.strip().split(" ")[0])


with open("./Day 7/input.txt", "r", encoding="utf8") as read_file:
    lines = read_file.read().splitlines()

print(dirs)
