import pygame
import random
import time
class bot2048():
    def randbox(self,temp):
        boxnum=0
        for y in self.boxes:
            boxnum+=y.count(0)
        if boxnum==0 and not temp:
            self.__init__()
            
            return self.boxes,False
        elif temp:
            chbox=random.randint(0,boxnum-1)
            seq=0
            for y in range(4):
                for x in range(4):
                    if self.boxes[y][x]==0:
                        if seq==chbox:
                            self.boxes[y][x]=random.choice([1,2])
                            self.draw()
                            return self.boxes,True
                            
                        else:
                            seq+=1
        else:
            return self.boxes,True
            
    def bind(self,direct): 
        self.temp=False
        #0 up 1 right 2 down 3 left   
        if direct==0:
            for x in range(4):
                for y1 in range(3):
                    for y2 in range(y1+1,4):
                        if (not self.boxes[y1][x]==self.boxes[y2][x]) and (not self.boxes[y1][x]==0) and (not self.boxes[y2][x]==0):
                            break
                        elif (self.boxes[y1][x]==self.boxes[y2][x]) and (not self.boxes[y1][x]==0) and (not self.boxes[y2][x]==0):
                            self.score+=self.value[self.boxes[y2][x]]
                            self.boxes[y1][x]+=1
                            self.boxes[y2][x]=0
                            self.temp=True
                            break
        if direct==1:
            for y in range(4):
                for x1 in range(3,-1,-1):
                    for x2 in range(x1-1,-1,-1):
                        if (not self.boxes[y][x1]==self.boxes[y][x2]) and (not self.boxes[y][x1]==0) and (not self.boxes[y][x2]==0):
                            break
                        elif (self.boxes[y][x1]==self.boxes[y][x2]) and (not self.boxes[y][x1]==0) and (not self.boxes[y][x2]==0):
                            self.score+=self.value[self.boxes[y][x2]]
                            self.boxes[y][x1]+=1
                            self.boxes[y][x2]=0
                            self.temp=True
                            break
        if direct==2:
            for x in range(4):
                for y1 in range(3,-1,-1):
                    for y2 in range(y1-1,-1,-1):
                        if (not self.boxes[y1][x]==self.boxes[y2][x]) and (not self.boxes[y1][x]==0) and (not self.boxes[y2][x]==0):
                            break
                        elif (self.boxes[y1][x]==self.boxes[y2][x]) and (not self.boxes[y1][x]==0) and (not self.boxes[y2][x]==0):
                            self.score+=self.value[self.boxes[y2][x]]
                            self.boxes[y1][x]+=1
                            self.boxes[y2][x]=0
                            self.temp=True
                            break
        if direct==3:
            for y in range(4):
                for x1 in range(3):
                    for x2 in range(x1+1,4):
                        if (not self.boxes[y][x1]==self.boxes[y][x2]) and (not self.boxes[y][x1]==0) and (not self.boxes[y][x2]==0):
                            break
                        elif (self.boxes[y][x1]==self.boxes[y][x2]) and (not self.boxes[y][x1]==0) and (not self.boxes[y][x2]==0):
                            self.score+=self.value[self.boxes[y][x2]]
                            self.boxes[y][x1]+=1
                            self.boxes[y][x2]=0
                            self.temp=True
                            break

    def move(self,direct):

        self.bind(direct)
        
        if direct==0:
            for x in range(4):
                for i in range(3):
                    for y in range(1,4):
                        if (self.boxes[y-1][x]==0) and (not self.boxes[y][x]==0):
                            self.boxes[y-1][x]=self.boxes[y][x]
                            self.boxes[y][x]=0
                            self.temp=True
        if direct==1:
            for y in range(4):
                for i in range(3):
                    for x in range(2,-1,-1):
                        if (self.boxes[y][x+1]==0) and (not self.boxes[y][x]==0):
                            self.boxes[y][x+1]=self.boxes[y][x]
                            self.boxes[y][x]=0
                            self.temp=True
        if direct==2:
            for x in range(4):
                for i in range(3):
                    for y in range(2,-1,-1):
                        if (self.boxes[y+1][x]==0) and (not self.boxes[y][x]==0):
                            self.boxes[y+1][x]=self.boxes[y][x]
                            self.boxes[y][x]=0
                            self.temp=True
        if direct==3:
            for y in range(4):
                for i in range(3):
                    for x in range(1,4):
                        if (self.boxes[y][x-1]==0) and (not self.boxes[y][x]==0):
                            self.boxes[y][x-1]=self.boxes[y][x]
                            self.boxes[y][x]=0
                            self.temp=True
                         
        return self.randbox(self.temp)
    def draw(self):
        self.screen.fill((255,255,255))
        for y in range(4):
            for x in range(4):
                if not self.boxes[y][x]==0:
                    font =pygame.font.Font(None,50)
                    text=font.render(str(self.value[self.boxes[y][x]]),True,(0,0,0))
                    x1=25+x*100
                    y1=25+y*100
                    self.screen.blit(text,(x1,y1))
        pygame.display.flip()

    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode([400,400])
        self.screen.fill('white')
        self.score=0
        self.value=[2**n for n in range(12)]
        self.boxes=[[0,0,0,0] for i in range(4)]
        boxes,self.flag=self.randbox(True)
        # while flag:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             flag=False
        #     print(self.score)
        #     for i in boxes:
        #         print(i)
        #     direct=int(input(':'))
        #     boxes,flag=self.move(direct)
        # pygame.quit()
#game=bot2048()