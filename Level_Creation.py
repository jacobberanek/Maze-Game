import numpy as np
import pygame,sys
from pygame.locals import *
from Block import *


def createList(levelNum):
    temp=[]
    string=""
    level=[]
    with open(levelNum + '.txt') as f:
        temp.append(f.read().splitlines())

    for i in range(len(temp[0])):
        string+=temp[0][i]
        string+=","

    for i in range(len(string)):
        level.append(string[i])
        
    return level

def createLevel(levelList):

    blocks=[]
    startXPos=0
    startYPos=0

    add=False

    for i in range(len(levelList)):
            add=False
            if levelList[i]=="," and add==False:
                startYPos+=50
                startXPos=0
                add=True
            elif levelList[i]=="+":
                blocks.append(Block(startXPos,startYPos,50,50,(50,50,240)))
            elif levelList[i]=="@":
                blocks.append(Block(startXPos,startYPos,50,50,(0,0,0)))
            elif levelList[i]=="X":
                blocks.append(Finish(startXPos,startYPos,50,50))
            elif levelList[i]=="O":
                blocks.append(Obstacle(startXPos,startYPos,50,50))
            elif levelList[i]=="1":
                blocks.append(Teleporter1(startXPos,startYPos,50,50))
            elif levelList[i]=="2":
                blocks.append(Teleporter2(startXPos,startYPos,50,50))
            if add==False:
                startXPos+=50   
    return blocks
