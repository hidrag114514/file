import creating_maze as mazer
import pygame
import time

col = 50
raw = 30
bh = 8
bw = bh
once = True

maze = mazer.create(col, raw)
maze[1][1] = "S"
rawmaze = maze
path = []


def find_path(maze, sx, sy):
    global path
    left, right, up, down = False, False, False, False
    try:
        if (sx < len(maze[0]) - 1 and maze[sy][sx + 1] == "1") or maze[sy][
            sx + 1
        ] == "E":
            x = maze
            x[sy][sx + 1] = "S"
            left, resultm = find_path(x, sx + 1, sy)
            if left:
                path.append([sy, sx + 1])

            if resultm[-2][-1] == "S":
                return True, resultm
    except:
        pass
    try:
        if (sx > 0 and maze[sy][sx - 1] == "1") or maze[sy][sx - 1] == "E":
            x = maze
            x[sy][sx - 1] = "S"
            right, resultm = find_path(x, sx - 1, sy)
            if right:
                path.append([sy, sx - 1])
            if resultm[-2][-1] == "S":
                return True, resultm
    except:
        pass
    try:
        if (sy > 0 and maze[sy - 1][sx] == "1") or maze[sy - 1][sx] == "E":
            x = maze
            x[sy - 1][sx] = "S"
            up, resultm = find_path(x, sx, sy - 1)
            if up:
                path.append([sy - 1, sx])
            if resultm[-2][-1] == "S":
                return True, resultm
    except:
        pass
    try:
        if (sy < len(maze) - 2 and maze[sy + 1][sx] == "1") or maze[sy + 1][sx] == "E":
            x = maze
            x[sy + 1][sx] = "S"
            down, resultm = find_path(x, sx, sy + 1)
            if down:
                path.append([sy + 1, sx])
            if resultm[-2][-1] == "S":
                return True, resultm
    except:
        pass
    if not (left or right or up or down):
        # print("---")
        return False, maze


a, result = find_path(maze, sy=1, sx=1)
# print(result)


pygame.init()
windoww = 1000
windowh = 600
screen = pygame.display.set_mode([windoww, windowh])
hero = [1, 0]
flag = True
showresult = False
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not (maze[hero[0] - 1][hero[1]] == "#"):
                hero[0] -= 1
            elif event.key == pygame.K_DOWN and not (maze[hero[0] + 1][hero[1]] == "#"):
                hero[0] += 1
            elif event.key == pygame.K_LEFT and not (maze[hero[0]][hero[1] - 1] == "#"):
                hero[1] -= 1
            elif event.key == pygame.K_RIGHT and not (
                maze[hero[0]][hero[1] + 1] == "#"
            ):
                hero[1] += 1
            elif event.key == pygame.K_0:
                hero = [1, 0]
            elif event.key == pygame.K_1:
                once = True
                maze = mazer.create(col, raw)
                hero = [1, 0]
                path = []
                a, result = find_path(maze, sy=1, sx=1)
            elif event.key == pygame.K_ESCAPE:
                flag = False
            elif event.key == pygame.K_2:
                if showresult:
                    showresult = False
                else:
                    showresult = True

    screen.fill((255, 255, 255))
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if showresult:
                if [y, x] in path:
                    pygame.draw.rect(screen, (0, 255, 0), (x * bw, y * bh, bw, bh))
            if maze[y][x] == "#":
                pygame.draw.rect(screen, (0, 0, 0), (x * bw, y * bh, bw, bh))

            elif y == hero[0] and x == hero[1]:
                pygame.draw.rect(screen, (255, 0, 0), (x * bw, y * bh, bw, bh))

                if y == len(maze) - 2 and x == len(maze[0]) - 1:
                    screen.fill((255, 255, 255))
                    font = pygame.font.Font(None, 36)
                    text = font.render("You Win! Press 1 to continue", True, (0, 0, 0))
                    text_rect = text.get_rect()
                    text_rect.center = (windoww // 2, windowh // 2)
                    screen.blit(text, text_rect)

                    if once:
                        col += 10
                        raw += 5
                        once = False
    pygame.display.flip()
pygame.quit
# for i in maze:
#     print(i)
