import g2048
import pygame
game=g2048.bot2048()
while game.flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.flag=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                boxes,flag=game.move(0)
                pygame.display.set_caption(('score:%s'%str(game.score)))
            elif event.key == pygame.K_RIGHT:
                boxes,flag=game.move(1)
                pygame.display.set_caption(('score:%s'%str(game.score)))
            elif event.key == pygame.K_DOWN:
                boxes,flag=game.move(2)
                pygame.display.set_caption(('score:%s'%str(game.score)))
            elif event.key == pygame.K_LEFT:
                boxes,flag=game.move(3)
                pygame.display.set_caption(('score:%s'%str(game.score)))
            else:
                pass
            # print(game.score)
            # for i in boxes:
            #     print(i)
    
pygame.quit()