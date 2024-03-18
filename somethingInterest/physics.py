import pygame
import math
import time
import random
pygame.init()
screenW=1600
screenH=1000
screen=pygame.display.set_mode([screenW,screenH])
flag=True

tick=0.01
g=[0,9.8]##m/s^2
# F_list=[]
##1m=1px
cd=0.47#0.47
rouAir=10#1.2

##1tick=0.01s
##x:m  y:m  v:m/s  a:m/s^2  m:kg  volume:m^3  Rou:kg/m^3 r:m
# m_info=[{'x':500,'y':100,'v':[0,0],'a':[0,0],'m':0,'volume':0,'rou':1000,'r':10}]
# m_info[0]['volume']= (4/3) * math.pi * (m_info[0]['r']**3)
# m_info[0]['m']= m_info[0]['rou'] * m_info[0]['volume']
class Ball():
    def __init__(self,x,y,v,a,rou,r):
        self.x=x
        self.y=y
        self.v=v
        self.a=a
        self.rou=rou
        self.r=r
        self.s=math.pi * self.r**2
        self.volume=(4/3) * math.pi * (self.r**3)
        self.m=self.rou*self.volume
        self.F_list=[]
        self.Fnet=[0,0]
        self.collideWith=[]
        red=random.randint(0,255)
        green=random.randint(0,255)
        blue=random.randint(0,255)
        self.color=(red,green,blue)
        print(self.color)
    def addGravity(self,g=g):

        self.F_list.append([self.m*g[0],self.m*g[1]])

    def addAirFriction(self,cd=cd,rouAir=rouAir):
        self.F_list.append([-0.5 * rouAir * self.s * cd * (self.v[0]**2) * (self.v[0]/(abs(self.v[0])+0.0001))\
                            , -0.5 * rouAir * self.s * cd * self.v[1]**2 * (self.v[1]/(abs(self.v[1]+0.0001)))])


    def floorBounce(self):
        
        self.a=[0,-2*self.v[1]/tick]
        self.v=[self.v[0],-self.v[1]]

    def wallBounce(self):
        
        self.a=[-2*self.v[0]/tick,0]
        self.v=[-self.v[0],self.v[1]]


    def collide(self, other_ball):
        # 计算碰撞前的动量
        self_momentum = self.m * math.sqrt(self.v[0]**2 + self.v[1]**2)
        other_momentum = other_ball.m * math.sqrt(other_ball.v[0]**2 + other_ball.v[1]**2)

        # 计算碰撞后的速度
        self_vx_after = ((self.m - other_ball.m) * self.v[0] + 2 * other_ball.m * other_ball.v[0]) / (self.m + other_ball.m)
        self_vy_after = ((self.m - other_ball.m) * self.v[1] + 2 * other_ball.m * other_ball.v[1]) / (self.m + other_ball.m)
        other_vx_after = ((other_ball.m - self.m) * other_ball.v[0] + 2 * self.m * self.v[0]) / (self.m + other_ball.m)
        other_vy_after = ((other_ball.m - self.m) * other_ball.v[1] + 2 * self.m * self.v[1]) / (self.m + other_ball.m)

        # 更新速度
        self.v[0] = self_vx_after
        self.v[1] = self_vy_after
        other_ball.v[0] = other_vx_after
        other_ball.v[1] = other_vy_after

        



    def calNetF(self):
        for Force in self.F_list:
                self.Fnet[0]+=Force[0]
                self.Fnet[1]+=Force[1]

    def calPos(self,balls):
        if self.y+self.r>screenH:
            self.y=screenH-self.r
            self.floorBounce()
            tempv=self.v
        elif self.y-self.r<0:
            self.y=self.r
            self.floorBounce()
            tempv=self.v
        elif self.x-self.r<0:
            self.x=self.r
            self.wallBounce()
            tempv=self.v
        elif self.x+self.r>screenW:
            self.x=screenW-self.r
            self.wallBounce()
            tempv=self.v
        else:
            isCollide=False
            for ball in balls:
                if ball != self and (ball not in self.collideWith):
                    
                    distance = math.sqrt((self.x - ball.x)**2 + (self.y - ball.y)**2)
                    if distance <= (self.r + ball.r):
                        # print('collide')
                        self.collideWith.append(ball)
                        ball.collideWith.append(self)
                        self.collide(ball)
                        
                        isCollide=True
                        tempv=self.v
            if isCollide:
                self.x+=tempv[0]*tick+self.a[0]*0.5*(tick**2)
                self.y+=tempv[1]*tick+self.a[1]*0.5*(tick**2)
                self.F_list=[]
                self.Fnet=[0,0]
                self.collideWith=[]
                return
                
            self.calNetF()
            self.a=[self.Fnet[0]/self.m,self.Fnet[1]/self.m]
            
            
            tempv=self.v
            self.v[0]+=self.a[0]*tick
            self.v[1]+=self.a[1]*tick
        self.x+=tempv[0]*tick+self.a[0]*0.5*(tick**2)
        self.y+=tempv[1]*tick+self.a[1]*0.5*(tick**2)

        self.F_list=[]
        self.Fnet=[0,0]
        

balls=[]
# balls.append(Ball(500,200,[10,0],[0,0],1000,20))
for i in range(20):
    x=random.random()*screenW
    y=random.random()*screenH
    vx=random.random()*200
    vy=random.random()*200
    rou=random.random()*1500+500
    r=random.random()*40+10
    balls.append(Ball(x,y,[vx,vy],[0,0],rou,r))
# balls.append(Ball(200,400,[100,0],[0,0],1000,20))
# balls.append(Ball(400,400,[20,0],[0,0],1000,20))


while flag:
    screen.fill('white')
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            flag=False

    for ball in balls:
        # ball.addGravity()
        # ball.addAirFriction()

        ball.calPos(balls)
        pygame.draw.circle(screen,ball.color,(ball.x,ball.y),ball.r)
    # for m in m_info:
    #     Fnet=[0,0]
    #     F_list=[]
    #     F_list.append(['G',[m_info[0]['m']*g[0],m_info[0]['m']*g[1]]])
    #     if m['y']+m['r']>800:
    #         print(m['v'])
    #         m['y']=800-m['r']
    #         m['a'][1]=0-2*m['v'][1]/tick
    #         m['v'][1]=0-m['v'][1]
    #         print(m['v'])
    #     else:   
    #         # print(m['v'])
    #         for Force in F_list:
    #             Fnet[0]+=Force[1][0]
    #             Fnet[1]+=Force[1][1]
            
    #         m['a'][0]=Fnet[0]/m['m']
    #         m['a'][1]=Fnet[1]/m['m']
    #         tempv=m['v']
    #         m['v'][0]+=m['a'][0]*tick
    #         m['v'][1]+=m['a'][1]*tick
    #     m['x']+=tempv[0]*tick+m['a'][0]*0.5*(tick**2)
    #     m['y']+=tempv[1]*tick+m['a'][1]*0.5*(tick**2)
        

        # pygame.draw.circle(screen,'black',(m['x'],m['y']),m['r'])

    pygame.display.flip()
    time.sleep(0.001)
pygame.quit()