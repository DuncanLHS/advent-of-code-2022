import numpy as np
treemap = []


def scenicScore(trees):
    for r in range(1, len(trees)-1):
        for t in range(1, len(trees[r])-1):
            ss = 0
            for t2 in range(t+1, len(trees[r])):
                if trees[r][t2] < trees[r][t]:
                    ss += 1
                else:
                    ss += 1
                    break
            treemapres[r][t] = ss * max(treemapres[r][t], 1)


with open("./Day 8/input.txt", "r", encoding="utf8") as read_file:
    for line in read_file:
        treemap.append(list(line.strip()))

treemap = np.array(treemap, dtype=int)
treemapres = np.full([len(treemap), len(treemap[0])], 0)

scenicScore(treemap)
treemap = np.moveaxis(treemap, 0, 1)
treemapres = np.moveaxis(treemapres, 0, 1)
scenicScore(treemap)
treemap = np.flip(treemap)
treemapres = np.flip(treemapres)
scenicScore(treemap)
treemap = np.moveaxis(treemap, 0, 1)
treemapres = np.moveaxis(treemapres, 0, 1)
scenicScore(treemap)
# treemap = np.flip(treemap)
# treemapres = np.flip(treemapres)

print(treemapres.max())
