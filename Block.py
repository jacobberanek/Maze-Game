import pygame
from pygame.locals import *

class Block():

    def __init__(self,x_pos=10, y_pos=10, width=20, height=10,
                 color=(0,0,0)):
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.width = width
        self.height=height
        self.color=color

    
    def collide(self,other,key):
        if key=="K_RIGHT":
            if self.y+30<=other.y_pos or self.y>=other.y_pos+50:
                return True
            if self.x+30<other.x_pos:
                return True
            if self.x>=other.x_pos:
                return True
            else:
                return False
        if key=="K_DOWN":
            if self.x+30<=other.x_pos or self.x>=other.x_pos+50:
                return True
            if self.y+30<other.y_pos:
                return True
            if self.y>=other.y_pos:
                return True
            else:
                return False
        if key=="K_LEFT":
            if self.y+30<=other.y_pos or self.y>=other.y_pos+50:
                return True
            if self.x>other.x_pos+50:
                return True
            if self.x<=other.x_pos:
                return True
            else:
                return False
        if key=="K_UP":
            if self.x+30<=other.x_pos or self.x>=other.x_pos+50:
                return True
            if self.y+30<other.y_pos+50:
                return True
            if self.y>other.y_pos+50:
                return True
            else:
                return False
                
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x_pos, self.y_pos,
                    self.width, self.height))
    
    

    
        
#IMAGE OBJECT
    
class collision():
    def __init__(self,x,y,pic):
        self.x=x
        self.y=y
        self.pic=pic

    def draw(self,win):
        image=pygame.image.load(self.pic+".png")
        win.blit(image,(self.x,self.y))
        
    def collide(self,other,key):
        if key=="K_RIGHT":
            if self.y+30<=other.y_pos or self.y>=other.y_pos+50:
                return True
            if self.x+30<other.x_pos:
                return True
            if self.x>=other.x_pos:
                return True
            else:
                return False
        if key=="K_DOWN":
            if self.x+30<=other.x_pos or self.x>=other.x_pos+50:
                return True
            if self.y+30<other.y_pos:
                return True
            if self.y>=other.y_pos:
                return True
            else:
                return False
        if key=="K_LEFT":
            if self.y+30<=other.y_pos or self.y>=other.y_pos+50:
                return True
            if self.x>other.x_pos+50:
                return True
            if self.x<=other.x_pos:
                return True
            else:
                return False
        if key=="K_UP":
            if self.x+30<=other.x_pos or self.x>=other.x_pos+50:
                return True
            if self.y+30<other.y_pos+50:
                return True
            if self.y>other.y_pos+50:
                return True
            else:
                return False


class Finish():

    def __init__(self,x_pos, y_pos, width, height):
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.width=width
        self.height=height
        self.color=(0,255,0)

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x_pos, self.y_pos,
                    self.width, self.height))
        
    def collide(self,other,key):
        if key=="K_RIGHT":
            if self.y+30<=other.y_pos or self.y>=other.y_pos+50:
                return True
            if self.x+30<other.x_pos:
                return True
            if self.x>=other.x_pos:
                return True
            else:
                return False
        if key=="K_DOWN":
            if self.x+30<=other.x_pos or self.x>=other.x_pos+50:
                return True
            if self.y+30<other.y_pos:
                return True
            if self.y>=other.y_pos:
                return True
            else:
                return False
        if key=="K_LEFT":
            if self.y+30<=other.y_pos or self.y>=other.y_pos+50:
                return True
            if self.x>other.x_pos+50:
                return True
            if self.x<=other.x_pos:
                return True
            else:
                return False
        if key=="K_UP":
            if self.x+30<=other.x_pos or self.x>=other.x_pos+50:
                return True
            if self.y+30<other.y_pos+50:
                return True
            if self.y>other.y_pos+50:
                return True
            else:
                return False

class Obstacle():

    def __init__(self,x_pos, y_pos, width, height):
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.width=width
        self.height=height
        self.color=(255,0,255)

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x_pos, self.y_pos,
                    self.width, self.height))
        
    def collide(self,other,key):
        if key=="K_RIGHT":
            if self.y+30<=other.y_pos or self.y>=other.y_pos+50:
                return True
            if self.x+30<other.x_pos:
                return True
            if self.x>=other.x_pos:
                return True
            else:
                return False
        if key=="K_DOWN":
            if self.x+30<=other.x_pos or self.x>=other.x_pos+50:
                return True
            if self.y+30<other.y_pos:
                return True
            if self.y>=other.y_pos:
                return True
            else:
                return False
        if key=="K_LEFT":
            if self.y+30<=other.y_pos or self.y>=other.y_pos+50:
                return True
            if self.x>other.x_pos+50:
                return True
            if self.x<=other.x_pos:
                return True
            else:
                return False
        if key=="K_UP":
            if self.x+30<=other.x_pos or self.x>=other.x_pos+50:
                return True
            if self.y+30<other.y_pos+50:
                return True
            if self.y>other.y_pos+50:
                return True
            else:
                return False

class Teleporter1():

    def __init__(self,x_pos, y_pos, width, height):
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.width=width
        self.height=height
        self.color=(255,255,0)

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x_pos, self.y_pos,
                    self.width, self.height))
        
    def collide(self,other,key):
        if key=="K_RIGHT":
            if self.y+30<=other.y_pos or self.y>=other.y_pos+50:
                return True
            if self.x+30<other.x_pos:
                return True
            if self.x>=other.x_pos:
                return True
            else:
                return False
        if key=="K_DOWN":
            if self.x+30<other.x_pos or self.x>other.x_pos+50:
                return True
            if self.y+30<other.y_pos:
                return True
            if self.y>other.y_pos:
                return True
            else:
                return False
        if key=="K_LEFT":
            if self.y+30<other.y_pos or self.y>other.y_pos+50:
                return True
            if self.x>other.x_pos+50:
                return True
            if self.x<other.x_pos:
                return True
            else:
                return False
        if key=="K_UP":
            if self.x+30<=other.x_pos or self.x>=other.x_pos+50:
                return True
            if self.y+30<other.y_pos+40:
                return True
            if self.y>other.y_pos+50:
                return True
            else:
                return False
class Teleporter2():

    def __init__(self,x_pos, y_pos, width, height):
        self.x_pos=x_pos
        self.y_pos=y_pos
        self.width=width
        self.height=height
        self.color=(255,130,0)

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x_pos, self.y_pos,
                    self.width, self.height))
        
    def collide(self,other,key):
        if key=="K_RIGHT":
            if self.y+30<=other.y_pos or self.y>=other.y_pos+50:
                return True
            if self.x+30<other.x_pos:
                return True
            if self.x>=other.x_pos:
                return True
            else:
                return False
        if key=="K_DOWN":
            if self.x+30<=other.x_pos or self.x>=other.x_pos+50:
                return True
            if self.y+30<other.y_pos:
                return True
            if self.y>=other.y_pos:
                return True
            else:
                return False
        if key=="K_LEFT":
            if self.y+30<=other.y_pos or self.y>=other.y_pos+50:
                return True
            if self.x>other.x_pos+50:
                return True
            if self.x<=other.x_pos:
                return True
            else:
                return False
        if key=="K_UP":
            if self.x+30<=other.x_pos or self.x>=other.x_pos+50:
                return True
            if self.y+30<other.y_pos+40:
                return True
            if self.y>other.y_pos+50:
                return True
            else:
                return False
            
        

                                                                            

