import pygame
screen=pygame.display.set_mode((600,500))
main_run=1
run=1
down=500
x=100
y=400
while main_run:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),(x,y,100,100),0)
    pygame.display.update()
    loop=1
    while loop==1:
        pygame.event.pump()
        key=pygame.key.get_pressed()
        loop2=1
        y=400
        if key[pygame.K_w]:
            while loop2==1:
                if y<down and y>350:
                    y=y-2
                    screen.fill((0,0,0))
                    pygame.draw.rect(screen,(255,0,0),(x,y,100,100),0)
                    pygame.display.update()
                    move=1
                if y<351 and y>300 and move==2:
                    move=1
                if y<351 and y>300 and move==1:
                    y=y-1
                    screen.fill((0,0,0))
                    pygame.draw.rect(screen,(255,0,0),(x,y,100,100),0)
                    pygame.display.update()
                    move=2
                if y==300:
                    move=3
                if y>300 and y<350 and move==3:
                    y=y+1
                    screen.fill((0,0,0))
                    pygame.draw.rect(screen,(255,0,0),(x,y,100,100),0)
                    pygame.display.update()
                    move=3
                if y>249 and y<200:
                    y=y+2
                    screen.fill((0,0,0))
                    pygame.draw.rect(screen,(255,0,0),(x,y,100,100),0)
                    pygame.display.update()
                if y<200:
                    loop2=0
                    print("END")
    
