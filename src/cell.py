import pygame
from colors import Color
import random

class Cell:
    n = None
    e = None
    s = None
    w = None
    north = True
    east = True
    south = True
    west = True

    ID = -1
    pos = (0,0)
    size = 20
    color = Color.yellow
    thickness = 1

    fill = False

    visited = False

    def __init__(self, ID, pos, size, color, thickness):
        self.ID = ID
        self.pos = pos
        self.size = size
        self.color = color
        self.thickness = thickness

    def addEdge(self):
        self.visited = True 
        edgeOrder = self.getRandomEdgeOrder()
        numConnections = 0
        done = False
        for i in edgeOrder:
            (neighborNotConnected, neighbor) = self.getNeighbor(i)
            if (neighborNotConnected == False):
                numConnections += 1
            if (neighborNotConnected):
                if numConnections == 3:
                    return False
                else:
                    if (neighbor == None):
                        continue
                    if not self.isConnected(neighbor):
                        neighbor.connect(self.ID)
                        self.connect(neighbor.ID)
                        return True
            else:
                if neighbor.visited != True: 
                    done = neighbor.addEdge()
            if done:
                return True
        return False

    def isConnected(self, target, parent=None):
        if (self.ID == target.ID):
            return True
        
        for i in range(0, 4):
            (neighborNotConnected, neighbor) = self.getNeighbor(i)
            if (parent != None and neighbor != None and parent.ID == neighbor.ID):
                continue
            else:
                if neighbor != None:
                    if (neighborNotConnected == False and neighbor.isConnected(target, self)):
                        return True
        return False

                
            
    def connect(self, connectToID):
        if (self.n != None and self.n.ID == connectToID):
            self.north = False
        if (self.e != None and self.e.ID == connectToID):
            self.east = False
        if (self.s != None and self.s.ID == connectToID):
            self.south = False
        if (self.w != None and self.w.ID == connectToID):
            self.west = False

    def getNeighbor(self, i):
        if i == 0:
            return (self.north, self.n)
        elif i == 1:
            return (self.east, self.e)
        elif i == 2:
            return (self.south, self.s)
        else:
            return (self.west, self.w)

    def getRandomEdgeOrder(self):
        x = []
        for i in range(0,4):
            x.insert(random.randint(0,len(x)), i)
        return x
        
    def draw(self, window):
        if (self.north == True):
            pygame.draw.line(window, self.color, (self.pos[0]-self.size/2.0,self.pos[1]-self.size/2.0), (self.pos[0]+self.size/2.0, self.pos[1]-self.size/2.0), self.thickness) 
        if (self.east == True):
            pygame.draw.line(window, self.color, (self.pos[0]+self.size/2.0,self.pos[1]-self.size/2.0), (self.pos[0]+self.size/2.0, self.pos[1]+self.size/2.0), self.thickness) 
        if (self.south == True):
            pygame.draw.line(window, self.color, (self.pos[0]-self.size/2.0,self.pos[1]+self.size/2.0), (self.pos[0]+self.size/2.0, self.pos[1]+self.size/2.0), self.thickness) 
        if (self.west == True):
            pygame.draw.line(window, self.color, (self.pos[0]-self.size/2.0,self.pos[1]-self.size/2.0), (self.pos[0]-self.size/2.0, self.pos[1]+self.size/2.0), self.thickness) 

        if (self.fill):
            pygame.draw.rect(window, Color.cyan, pygame.Rect(self.pos[0]-self.size/2.0 + round(self.thickness/2.0), self.pos[1]-self.size/2.0 + round(self.thickness/2.0), self.size- self.thickness/2.0, self.size-self.thickness/2.0))


