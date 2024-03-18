import pygame
import random
import time
import json
import sys
import os


if __name__=='__main__':
    tem=True
    while True:
        
        pygame.init()
        screen=pygame.display.set_mode([1000,800])
        balls=[]
        for i in range(5):
            balls.append([random.randint(0,1000),0,random.uniform(0.1,0.3)])
        print(balls)
        mark=0

        #初始化
        dpath=os.path.dirname(__file__)
        hero=pygame.image.load(os.path.join(dpath,"hero.png"))
        ballimage=pygame.image.load(os.path.join(dpath,'en.jpg'))
        storep=os.path.join(dpath,'record.json')

        colorkey=hero.get_at((0,0))
        hero.set_colorkey(colorkey)
        hx=500-35
        hy=800-38
        flag=True
        movr=False
        movl=False
        movu=True
        gamu=True
        lop=200
        movup=0
        upt=2
        speed=0.1
        global temple


        while flag:
            
            
            #侦测键盘控制
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag=False
                #可持续移动
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        movr=True
                    if event.key == pygame.K_LEFT:
                        movl=True
                    if event.key == pygame.K_UP and movu:
                        movup=200
                        upt-=1
                    if upt==0:
                        movu=False
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        movr=False
                    if event.key == pygame.K_LEFT:
                        movl=False
                        
            #不跑出屏幕外
            if movr and hx<1000-35:
                hx+=0.5
            if movl and hx>0:
                hx-=0.5

            #二段跳
            if movup>0:
                hy-=1
                movup-=1
            if hy==800-38:
                movu=True
                upt=2
            
            #模拟重力
            if hy<800-38:
                hy+=0.25
            
            
            screen.fill((255,255,255))
            for i in balls:
                screen.blit(ballimage,(i[0],i[1]))
                i[0]+=(i[2]+speed)
                i[1]+=(i[2]+speed)
                if i[0]>1000:
                    i[0]-=1000
                if i[1]>800:
                    i[1]-=800

            pygame.display.set_caption(("score:"+str(round(mark))))
            screen.blit(hero,(hx,hy))
            
            for i in balls:
                if i[0]<hx<i[0]+32 and i[1]<hy<i[1]+32:
                    gamu=False
                if i[0]<hx+35<i[0]+32 and i[1]<hy<i[1]+32:
                    gamu=False
                if i[0]<hx<i[0]+32 and i[1]<hy+38<i[1]+32:
                    gamu=False
                if i[0]<hx+35<i[0]+32 and i[1]<hy+38<i[1]+32:
                    gamu=False
            
            if lop>0:
                lop-=0.01
            else:
                lop=200
                speed+=0.1

                
            if gamu:
                pygame.display.update()
                mark+=0.01
            else:
                with open(storep,"r") as fp:
                    record=json.load(fp)
                if mark>record:
                    record=mark
                    with open(storep,"w") as fp:
                        json.dump(record,fp)
                    print("恭喜您打破了纪录")
                time.sleep(3)
                flag=False
        pygame.quit()
        print("得分：%d\n最高纪录：%d"%(mark,record))
        print("回车以继续开始下局游戏")
        a=input('')
        if a=="":
            continue
        else:
            tem=False
            sys.exit()




    