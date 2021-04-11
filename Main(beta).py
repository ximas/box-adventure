#module for my box adventure jump----------
import pygame
screen=pygame.display.set_mode((800,500))
#functions-------------------------------------------
#left---------------------------------------------------
def left(x,y,now_x,now_y,speed):
    down=500
    left=0
    right=800
    cyan=(0,255,255)
    red=(255,0,0)
    black=(0,0,0)
    up=-1
    run=1
    loop=1
    while run==1:
        pygame.event.pump()
        key=pygame.key.get_pressed()
        event=pygame.event.poll()
        keyu=pygame.KEYUP
        if x<=left:
            x=x+1
        if (x+100)>=right:
            x=x-1
        if x>left and (x+100)<right:
            x=x-speed
            screen.fill(cyan)
            draw()
            pygame.draw.rect(screen,red,(x,y,100,100),0)
            pygame.draw.rect(screen,black,(x,y,100,100),2)
            pygame.display.update()
        if key[pygame.K_w]:
            while loop==1:
                if (y+100)<=(now_y+100) and y>(now_y-50):
                    y=y+(up*2)
                    x=x-1
                    screen.fill(cyan)
                    draw()
                    pygame.draw.rect(screen,red,(x,y,100,100),0)
                    pygame.draw.rect(screen,black,(x,y,100,100),2)
                    pygame.display.update()
                if y<=(now_y-50) and y>(now_y-100) and up==-1:
                    x=x-1
                    y=y+up
                    screen.fill(cyan)
                    draw()
                    pygame.draw.rect(screen,red,(x,y,100,100),0)
                    pygame.draw.rect(screen,black,(x,y,100,100),2)
                    pygame.display.update()
                if y==(now_y-100):
                    up=1
                if y>=(now_y-100) and y<(now_y-50) and up==1:
                    x=x-1
                    y=y+up
                    screen.fill(cyan)
                    draw()
                    pygame.draw.rect(screen,red,(x,y,100,100),0)
                    pygame.draw.rect(screen,black,(x,y,100,100),2)
                    pygame.display.update()
                if y>=(now_y-50) and (y+99)<(now_y+100) and up==1:
                    x=x-1
                    y=y+up
                    screen.fill(cyan)
                    draw()
                    pygame.draw.rect(screen,red,(x,y,100,100),0)
                    pygame.draw.rect(screen,black,(x,y,100,100),2)
                    pygame.display.update()
                if y==(now_y+1):
                    loop=0
        if event.type==keyu:
            run=0
    return [x,y]
#right------------------------------------------------
def right(x,y,now_x,now_y,speed):
    down=500
    left=0
    right=800
    cyan=(0,255,255)
    red=(255,0,0)
    black=(0,0,0)
    up=-1
    run=1
    loop=1
    while run==1:
        pygame.event.pump()
        key=pygame.key.get_pressed()
        event=pygame.event.poll()
        keyu=pygame.KEYUP
        if x<=left:
            x=x+1
        if (x+100)>=right:
            x=x-1
        if x>left and (x+100)<right:
            x=x+speed
            screen.fill(cyan)
            draw()
            pygame.draw.rect(screen,red,(x,y,100,100),0)
            pygame.draw.rect(screen,black,(x,y,100,100),2)
            pygame.display.update()
        if key[pygame.K_w]:
            while loop==1:
                if (y+100)<=(now_y+100) and y>(now_y-50):
                    y=y+(up*2)
                    x=x+1
                    screen.fill(cyan)
                    draw()
                    pygame.draw.rect(screen,red,(x,y,100,100),0)
                    pygame.draw.rect(screen,black,(x,y,100,100),2)
                    pygame.display.update()
                if y<=(now_y-50) and y>(now_y-100) and up==-1:
                    x=x+1
                    y=y+up
                    screen.fill(cyan)
                    draw()
                    pygame.draw.rect(screen,red,(x,y,100,100),0)
                    pygame.draw.rect(screen,black,(x,y,100,100),2)
                    pygame.display.update()
                if y==(now_y-100):
                    up=1
                if y>=(now_y-100) and y<(now_y-50) and up==1:
                    x=x+1
                    y=y+up
                    screen.fill(cyan)
                    draw()
                    pygame.draw.rect(screen,red,(x,y,100,100),0)
                    pygame.draw.rect(screen,black,(x,y,100,100),2)
                    pygame.display.update()
                if y>=(now_y-50) and (y+99)<(now_y+100) and up==1:
                    x=x+1
                    y=y+up
                    screen.fill(cyan)
                    draw()
                    pygame.draw.rect(screen,red,(x,y,100,100),0)
                    pygame.draw.rect(screen,black,(x,y,100,100),2)
                    pygame.display.update()
                if y==(now_y+1):
                    loop=0
        if event.type==keyu:
            run=0
    return [x,y]
#jump------------------------------------------------
def jump(x,y,now_x,now_y):
    down=500
    left=0
    right=800
    cyan=(0,255,255)
    red=(255,0,0)
    black=(0,0,0)
    up=-1
    run=1
    loop=1
    pygame.event.pump()
    key=pygame.key.get_pressed()
    key_f=pygame.key.get_focused()
    while run==1:
        while loop==1:
            if (y+100)<=(now_y+100) and y>(now_y-50):
                y=y+(up*2)
                screen.fill(cyan)
                draw()
                pygame.draw.rect(screen,red,(x,y,100,100),0)
                pygame.draw.rect(screen,black,(x,y,100,100),2)
                pygame.display.update()
            if y<=(now_y-50) and y>(now_y-100) and up==-1:
                y=y+up
                screen.fill(cyan)
                draw()
                pygame.draw.rect(screen,red,(x,y,100,100),0)
                pygame.draw.rect(screen,black,(x,y,100,100),2)
                pygame.display.update()
            if y==(now_y-100):
                up=1
            if y>=(now_y-100) and y<(now_y-50) and up==1:
                y=y+up
                screen.fill(cyan)
                draw()
                pygame.draw.rect(screen,red,(x,y,100,100),0)
                pygame.draw.rect(screen,black,(x,y,100,100),2)
                pygame.display.update()
            if y>=(now_y-50) and (y+99)<(now_y+100) and up==1:
                y=y+up
                screen.fill(cyan)
                draw()
                pygame.draw.rect(screen,red,(x,y,100,100),0)
                pygame.draw.rect(screen,black,(x,y,100,100),2)
                pygame.display.update()
            if y==(now_y+1):
                loop=0
        run=0
#draws obstacles-------------------------------
def draw():
    pygame.draw.rect(screen,(0,255,0),
                     (Draws[0],Draws[1],Draws[2],Draws[3]),0)
    pygame.display.update()
#adds the values to the obstacle list----------
def limits(obscle):
    [x,y,l,h]=obscle.limits()
    Limits.append(x)
    Limits.append(y)
    Limits.append(l)
    Limits.append(h)
#adds the values to the obstacle draw list-----
def draws(obscle):
    [x,y,l,h]=obscle.draws()
    Draws.append(x)
    Draws.append(y)
    Draws.append(l)
    Draws.append(h)
#creats the obstacle limits you specify--------
class obstacle():
    def __init__(self,x,l,h):
        self.x=x
        self.l=l
        self.h=h
    def limits(self):
        limit_x=self.x
        limit_y=500
        limit_l=self.x+self.l
        limit_h=limit_y-self.h
        return[limit_x,limit_y,limit_l,limit_h]
    def draws(self):
        draw_x=self.x
        draw_y=500
        draw_l=self.l
        draw_h=-self.h
        return[draw_x,draw_y,draw_l,draw_h]

#variables-------------------------------------------
main_run=1
Down=500
Left=0
Right=800
x=100
y=400
speed=1
cyan=(0,255,255)
red=(255,0,0)
black=(0,0,0)
Limits=[]
Draws=[]
#y coordinate for the obstacle doesn't need to be specified
#because the obstacle will always start from the ground
land=obstacle(200,600,50)
limits(land)
draws(land)
draw()
print(Limits,Draws)
pygame.display.update()
#main-------------------------------------------------
while main_run:
    screen.fill(cyan)
    pygame.draw.rect(screen,red,(x,y,100,100),0)
    pygame.draw.rect(screen,black,(x,y,100,100),2)
    draw()
    pygame.display.update()
    event=pygame.event.poll()
    key=pygame.KEYDOWN
    if event.type==key:
        pygame.event.pump()
        key=pygame.key.get_pressed()
        nx=x
        ny=y
        if key[pygame.K_w]:
            jump(x,y,nx,ny)
        if key[pygame.K_a]:
            [x,y]=left(x,y,nx,ny,speed)            
        if key[pygame.K_d]:
            [x,y]=right(x,y,nx,ny,speed)
        


