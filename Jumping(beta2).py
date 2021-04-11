#module for my box adventure jump--------------
import pygame
screen=pygame.display.set_mode((600,500))

#variables---------------------------------------------
main_run=1
run=1
down=500
x=100
y=400

#main--------------------------------------------------
while main_run:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),(x,y,100,100),0)
    pygame.display.update()
    loop=1
#first loop that check if you are pressing jump
    while loop==1:
        pygame.event.pump()
        key=pygame.key.get_pressed()
        loop2=1
        y=400
#up controls the y coordinate of the shape----
        up=-1
        if key[pygame.K_w]:
#next loop - does the jump------------------------
            while loop2==1:
#code the shows the jump-------------------------
                if (y+100)<=down and y>350:
                    y=y+(up*2)
                    screen.fill((0,0,0))
                    pygame.draw.rect(screen,(255,0,0),(x,y,100,100),0)
                    pygame.display.update()
                if y<=350 and y>300 and up==-1:
                    y=y+up
                    screen.fill((0,0,0))
                    pygame.draw.rect(screen,(255,0,0),(x,y,100,100),0)
                    pygame.display.update()
                if y==300:
                    up=1
                if y>=300 and y<350 and up==1:
                    y=y+up
                    screen.fill((0,0,0))
                    pygame.draw.rect(screen,(255,0,0),(x,y,100,100),0)
                    pygame.display.update()
                if y>=350 and (y+99)<down and up==1:
                    y=y+up
                    screen.fill((0,0,0))
                    pygame.draw.rect(screen,(255,0,0),(x,y,100,100),0)
                    pygame.display.update()
#ends the jump loop-----------------------------
                if y==401:
                    loop2=0
#ends the key loop-------------------------------
            else:
                loop=0
                    
                    
    
