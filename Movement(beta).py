#module for my box adventure jump-----------
import pygame
screen=pygame.display.set_mode((800,500))
#functions--------------------------------------------
    
#variables--------------------------------------------
main_run=1
run=1
down=500
left=0
right=800
x=100
y=400
cyan=(0,255,255)
red=(255,0,0)
black=(0,0,0)

#main-------------------------------------------------
while main_run:
    screen.fill(cyan)
    pygame.draw.rect(screen,red,(x,y,100,100),0)
    pygame.draw.rect(screen,black,(x,y,100,100),2)
    pygame.display.update()
    loop=1
#first loop that check if you are pressing keys
    while loop==1:
        pygame.event.pump()
        key=pygame.key.get_pressed()
        loop2=1
        y=400
#can be modified-----------------------------------
        speed=2
#movement keys-----------------------------------
#left---------------------------------------------------
        if key[pygame.K_d]:
            if x<=left:
                x=x+1
            if (x+100)>=right:
                x=x-1
            if x>left and (x+100)<right:
                x=x+speed
                screen.fill(cyan)
                pygame.draw.rect(screen,red,(x,y,100,100),0)
                pygame.draw.rect(screen,black,(x,y,100,100),2)
                pygame.display.update()
#right------------------------------------------------
        if key[pygame.K_a]:
            if x<=left:
                x=x+1
            if (x+100)>=right:
                x=x-1
            if x>left and (x+100)<right:
                x=x-speed
                screen.fill(cyan)
                pygame.draw.rect(screen,red,(x,y,100,100),0)
                pygame.draw.rect(screen,black,(x,y,100,100),2)
                pygame.display.update()
#controls how much the y-------------------------
#coordinate of the shape moves
        up=-1
#key you need to jump-----------------------------
        if key[pygame.K_w]:
#next loop - does the jump------------------------
            while loop2==1:
#code the shows the jump-------------------------
                if (y+100)<=down and y>350:
                    y=y+(up*2)
                    screen.fill(cyan)
                    pygame.draw.rect(screen,red,(x,y,100,100),0)
                    pygame.draw.rect(screen,black,(x,y,100,100),2)
                    pygame.display.update()
                if y<=350 and y>300 and up==-1:
                    y=y+up
                    screen.fill(cyan)
                    pygame.draw.rect(screen,red,(x,y,100,100),0)
                    pygame.draw.rect(screen,black,(x,y,100,100),2)
                    pygame.display.update()
                if y==300:
                    up=1
                if y>=300 and y<350 and up==1:
                    y=y+up
                    screen.fill(cyan)
                    pygame.draw.rect(screen,red,(x,y,100,100),0)
                    pygame.draw.rect(screen,black,(x,y,100,100),2)
                    pygame.display.update()
                if y>=350 and (y+99)<down and up==1:
                    y=y+up
                    screen.fill(cyan)
                    pygame.draw.rect(screen,red,(x,y,100,100),0)
                    pygame.draw.rect(screen,black,(x,y,100,100),2)
                    pygame.display.update()
#ends the jump loop-----------------------------
                if y==401:
                    loop2=0
#ends the key loop-------------------------------
        else:
            loop=0
