import numpy as np
treemap = []


def countIsVisible(trees):
    global total
    for r in range(0, len(trees)):
        for t in range(0, len(trees[r])):
            if t == 0:
                treemapres[r][t] = True
                continue
            if trees[r][t] > max(trees[r][:t]):
                treemapres[r][t] = True


with open("./Day 8/input.txt", "r", encoding="utf8") as read_file:
    for line in read_file:
        treemap.append(list(line.strip()))

treemap = np.array(treemap, dtype=int)
treemapres = np.full([len(treemap), len(treemap[0])], False)

countIsVisible(treemap)
treemap = np.moveaxis(treemap, 0, 1)
treemapres = np.moveaxis(treemapres, 0, 1)
countIsVisible(treemap)
treemap = np.flip(treemap)
treemapres = np.flip(treemapres)
countIsVisible(treemap)
treemap = np.moveaxis(treemap, 0, 1)
treemapres = np.moveaxis(treemapres, 0, 1)
countIsVisible(treemap)

print(treemapres.sum())
