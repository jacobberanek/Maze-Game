
import numpy as np
import pygame,sys
from pygame.locals import *
from Block import *
from Level_Creation import *
pygame.init()

pygame.display.set_caption('3 Level Maze Game')

levelIndex=0
font=pygame.font.Font('freesansbold.ttf',50)
youWin=font.render("You Win!",True,(0,0,0))
youLose=font.render("You Lose!",True,(0,0,0))

easy=createList('level')
hard=createList('level2')
harder=createList('level3')
hardest=createList('level4')

level1=createLevel(easy)
level2=createLevel(hard)
level3=createLevel(harder)
level4=createLevel(hardest)
levels=[level1,level2,level3,level4]

levelCount=4
less=3

def findStartPos(level):
    var=False
    index=0
    for i in range(len(levels[levelIndex])):
        if levels[levelIndex][i].color==(0,0,0) and var==False:
            index=i
            var=True
            xpos=level1[index].x_pos
    return xpos

xpos=findStartPos(levels[levelIndex])
image=collision(xpos,0,"person")        


screen=pygame.display.set_mode((800,600))
clock = pygame.time.Clock()


    
personX=100
personY=100
collideUp=False
collideDown=False
collideRight=False
collideLeft=False
end=True
num=0
tries=0

makeBig=False

while end:
    
    screen.fill((255,255,255))
    clock.tick(360)
    pygame.key.set_repeat(50,20)
    collideLeft=False
    collideRight=False
    collideDown=False
    collideUp=False

    complete=False
    reset=False
    teleport1=False
    teleport2=False

    for i in range(len(levels[levelIndex])):
        if levels[levelIndex][i].color==(255,255,0):
            teleporter1X=levels[levelIndex][i].x_pos
            teleporter1Y=levels[levelIndex][i].y_pos
        if levels[levelIndex][i].color==(255,130,0):
            teleporter2X=levels[levelIndex][i].x_pos
            teleporter2Y=levels[levelIndex][i].y_pos
    
    #CHANGE LEVEL
    if num!=levelCount and tries!=3:
        for i in range(len(levels[levelIndex])):
            levels[levelIndex][i].draw(screen)
            if isinstance(levels[levelIndex][i], Block) and levels[levelIndex][i].color==(50,50,240) :
                if not(image.collide(levels[levelIndex][i],"K_UP")):
                   collideUp=True
                if not(image.collide(levels[levelIndex][i],"K_DOWN")):
                   collideDown=True
                if not(image.collide(levels[levelIndex][i],"K_RIGHT")):
                   collideRight=True
                if not(image.collide(levels[levelIndex][i],"K_LEFT")):
                   collideLeft=True
                   
            if isinstance(levels[levelIndex][i],Finish):
                if not(image.collide(levels[levelIndex][i],"K_UP")):
                   complete=True
                if not(image.collide(levels[levelIndex][i],"K_DOWN")):
                   complete=True
                if not(image.collide(levels[levelIndex][i],"K_RIGHT")):
                   complete=True
                if not(image.collide(levels[levelIndex][i],"K_LEFT")):
                   complete=True
            if levels[levelIndex][i].color==(255,0,255):
                if not(image.collide(levels[levelIndex][i],"K_UP")):
                    reset=True
                if not(image.collide(levels[levelIndex][i],"K_DOWN")):
                    reset=True
                if not(image.collide(levels[levelIndex][i],"K_RIGHT")):
                    reset=True
                if not(image.collide(levels[levelIndex][i],"K_LEFT")):
                    reset=True
            if levels[levelIndex][i].color==(255,255,0):
                if not(image.collide(levels[levelIndex][i],"K_UP")):
                   teleport1=True
                if not(image.collide(levels[levelIndex][i],"K_DOWN")):
                   teleport1=True
                if not(image.collide(levels[levelIndex][i],"K_RIGHT")):
                   teleport1=True
                if not(image.collide(levels[levelIndex][i],"K_LEFT")):
                   teleport1=True

            if levels[levelIndex][i].color==(255,130,0):
                if not(image.collide(levels[levelIndex][i],"K_UP")):
                   teleport2=True
                if not(image.collide(levels[levelIndex][i],"K_DOWN")):
                   teleport2=True
                if not(image.collide(levels[levelIndex][i],"K_RIGHT")):
                   teleport2=True
                if not(image.collide(levels[levelIndex][i],"K_LEFT")):
                   teleport2=True
        
        image.draw(screen)
    elif num==levelCount:
        screen.blit(youWin,(300,250))
    elif tries==3:
        screen.blit(youLose,(300,250))
    if num==levelCount-1 and makeBig==False:
        screen=pygame.display.set_mode((1000,600))
        pygame.display.update()
        makeBig=True
        
            
    
    pygame.display.update()


    for event in pygame.event.get():
        if event.type==pygame.QUIT or (event.type == KEYDOWN and event.key==K_ESCAPE):
            end=False
            pygame.quit()
        if event.type==KEYDOWN and event.key==K_RIGHT and image.x+30<800:
            if collideRight==False:
                image.x+=5
            if complete==True and levelIndex!=less:
                levelIndex+=1
                image=collision(findStartPos(levels[levelIndex]),0,"person")
            if complete==True:
                num+=1
            if reset==True:
                image=collision(findStartPos(levels[levelIndex]),0,"person")
                tries+=1
            if teleport1==True:
                image=collision(teleporter2X,teleporter2Y,"person")


        if event.type==KEYDOWN and event.key==K_LEFT and 0<image.x:
            if collideLeft==False:
                image.x-=5
            if complete==True and levelIndex!=less:
                levelIndex+=1
                image=collision(findStartPos(levels[levelIndex]),0,"person")
            if complete==True:
                num+=1
            if reset==True:
                image=collision(findStartPos(levels[levelIndex]),0,"person")
                tries+=1
            if teleport1==True:
                image=collision(teleporter2X,teleporter2Y,"person")

                

        if event.type==KEYDOWN and event.key==K_DOWN and image.y+30<600:
            if collideDown==False:
                image.y+=5
            if complete==True and levelIndex!=less:
                levelIndex+=1
                image=collision(findStartPos(levels[levelIndex]),0,"person")
            if complete==True:
                num+=1
            if num==3:
                win=True
            if reset==True:
                image=collision(findStartPos(levels[levelIndex]),0,"person")
                tries+=1
            if teleport1==True:
                image=collision(teleporter2X,teleporter2Y,"person")

        if event.type==KEYDOWN and event.key==K_UP and 0<image.y:
            if collideUp==False:
                image.y-=5
            if complete==True and levelIndex!=less:
                levelIndex+=1
                image=collision(findStartPos(levels[levelIndex]),0,"person")
            if complete==True:
                num+=1
            if reset==True:
                image=collision(findStartPos(levels[levelIndex]),0,"person")
                tries+=1
            if teleport1==True:
                image=collision(teleporter2X,teleporter2Y,"person")

        

