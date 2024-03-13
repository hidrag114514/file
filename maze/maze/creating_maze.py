import random
import sys
import os

# textpath = os.path.join(os.path.dirname(__file__), "maze.txt")


def create(cols, raws):
    col = cols * 2  # 列
    raw = raws  # 行
    maze = [["#" for i in range(col + 1)]]
    for i in range(raw):
        maze.append(["0" for j in range(col + 1)])
        maze.append(["#" for j in range(col + 1)])

    for i in range(1, raw * 2 + 1, 2):
        for j in range(0, col + 1, 2):
            maze[i][j] = "#"
    orginy = random.randint(1, raw - 2) * 2 + 1
    orginx = random.randint(1, cols - 2) * 2 + 1
    walllist = [
        [orginy, orginx + 1],
        [orginy, orginx - 1],
        [orginy + 1, orginx],
        [orginy - 1, orginx],
    ]
    maze[orginy][orginx] = "1"
    while walllist:
        wall = random.choice(walllist)
        if maze[wall[0] + 1][wall[1]] == "0":
            maze[wall[0] + 1][wall[1]] = "1"
            newroom = [wall[0] + 1, wall[1]]
        elif maze[wall[0] - 1][wall[1]] == "0":
            maze[wall[0] - 1][wall[1]] = "1"
            newroom = [wall[0] - 1, wall[1]]
        elif maze[wall[0]][wall[1] + 1] == "0":
            maze[wall[0]][wall[1] + 1] = "1"
            newroom = [wall[0], wall[1] + 1]
        elif maze[wall[0]][wall[1] - 1] == "0":
            maze[wall[0]][wall[1] - 1] = "1"
            newroom = [wall[0], wall[1] - 1]
        else:
            continue
        maze[wall[0]][wall[1]] = "1"
        walllist.remove(wall)
        if maze[newroom[0] + 1][newroom[1]] == "#" and newroom[0] + 1 < raw * 2:
            walllist.append([newroom[0] + 1, newroom[1]])
        if maze[newroom[0] - 1][newroom[1]] == "#" and newroom[0] - 1 > 0:
            walllist.append([newroom[0] - 1, newroom[1]])
        if maze[newroom[0]][newroom[1] + 1] == "#" and newroom[1] + 1 < col:
            walllist.append([newroom[0], newroom[1] + 1])
        if maze[newroom[0]][newroom[1] - 1] == "#" and newroom[1] - 1 > 0:
            walllist.append([newroom[0], newroom[1] - 1])
        flag = True
        for i in maze:
            if "0" in i:
                flag = False

        if flag:
            break

    maze[1][0] = "S"
    maze[raw * 2 - 1][col] = "E"
    return maze


# with open(textpath, "w") as f:
#     for i in maze:
#         for j in i:
#             j = "%s" % j
#             f.write(j)
#         f.write("\n")
# for i in maze:
#     for j in i:
#         print(j, end="  ")
#     print("")
"""


['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']      
['#', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '#', '1', '1', '1', '1', '1', '#']      
['#', '1', '#', '#', '#', '1', '#', '#', '#', '#', '#', '#', '#', '#', '#', '1', '#', '#', '#', '1', '#']      
['#', '1', '#', '1', '1', '1', '1', '1', '1', '1', '#', '1', '#', '1', '#', '1', '#', '1', '#', '1', '#']      
['#', '1', '#', '1', '#', '1', '#', '#', '#', '1', '#', '1', '#', '1', '#', '1', '#', '1', '#', '1', '#']      
['#', '1', '#', '1', '#', '1', '1', '1', '#', '1', '1', '1', '1', '1', '1', '1', '#', '1', '#', '1', '#']      
['#', '1', '#', '1', '#', '1', '#', '1', '#', '#', '#', '#', '#', '#', '#', '#', '#', '1', '#', '#', '#']      
['#', '1', '#', '1', '#', '1', '#', '1', '#', '1', '1', '1', '1', '1', '#', '1', '#', '1', '1', '1', '#']      
['#', '#', '#', '1', '#', '#', '#', '#', '#', '1', '#', '#', '#', '#', '#', '1', '#', '1', '#', '1', '#']      
['#', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '#', '1', '#']      
['#', '1', '#', '#', '#', '1', '#', '1', '#', '#', '#', '#', '#', '1', '#', '1', '#', '1', '#', '#', '#']      
['#', '1', '#', '1', '1', '1', '#', '1', '1', '1', '1', '1', '#', '1', '#', '1', '#', '1', '1', '1', '#']      
['#', '1', '#', '#', '#', '1', '#', '1', '#', '#', '#', '#', '#', '1', '#', '#', '#', '#', '#', '#', '#']      
['#', '1', '#', '1', '1', '1', '#', '1', '1', '1', '1', '1', '#', '1', '1', '1', '1', '1', '1', '1', '#']      
['#', '#', '#', '1', '#', '#', '#', '1', '#', '1', '#', '#', '#', '1', '#', '#', '#', '1', '#', '1', '#']      
['#', '1', '1', '1', '#', '1', '1', '1', '#', '1', '1', '1', '#', '1', '1', '1', '#', '1', '#', '1', '#']      
['#', '#', '#', '1', '#', '#', '#', '1', '#', '#', '#', '#', '#', '1', '#', '1', '#', '1', '#', '1', '#']      
['#', '1', '1', '1', '1', '1', '#', '1', '#', '1', '1', '1', '#', '1', '#', '1', '#', '1', '#', '1', '#']      
['#', '#', '#', '#', '#', '#', '#', '1', '#', '1', '#', '#', '#', '#', '#', '#', '#', '1', '#', '1', '#']      
['#', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '#', '1', '1', '1', '1', '1', '#', '1', '#']      
['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'] 
"""
