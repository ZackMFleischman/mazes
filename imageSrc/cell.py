from colors import Color
import random

class Cell:
    n = None
    e = None
    s = None
    w = None
    northWall = True
    eastWall = True
    southWall = True
    westWall = True

    ID = -1
    pos = (0,0)
    size = 20
    color = Color.yellow
    thickness = 1

    fill = False
    fillColor = None

    visited = False

    def __init__(self, ID, pos):
        self.ID = ID
        self.pos = pos

    def getNeighbor(self, i):
        if i == 0:
            return (self.northWall, self.n)
        elif i == 1:
            return (self.eastWall, self.e)
        elif i == 2:
            return (self.southWall, self.s)
        else:
            return (self.westWall, self.w)

    def getRandomEdgeOrder(self):
        x = []
        for i in range(0,4):
            x.insert(random.randint(0,len(x)), i)
        return x

    def allNeighborsHaveBeenVisited(self):
        if (self.n != None and not self.n.visited):
            return False
        if (self.w != None and not self.w.visited):
            return False
        if (self.e != None and not self.e.visited):
            return False
        if (self.s != None and not self.s.visited):
            return False
        return True

    def connectToRandomUnvisitedNeighbor(self):
        if (self.allNeighborsHaveBeenVisited()):
            return (1, None)
        # Randomly fail to connect
        #if (random.randint(0,100) < 25):
        #    return(2, None)
        
        edgeOrder = self.getRandomEdgeOrder()
        for x in range(len(edgeOrder)):
            (wall, neighbor) = self.getNeighbor(edgeOrder[x])
            if (wall and neighbor != None and not neighbor.visited):
                neighbor.visted = True
                neighbor.connectTo(self)
                self.connectTo(neighbor)
                return (0, neighbor)
        return (1, None)

    def connectTo(self, neighbor):
        if (self.n != None and self.n.ID == neighbor.ID):
            self.northWall = False
        if (self.s != None and self.s.ID == neighbor.ID):
            self.southWall = False
        if (self.e != None and self.e.ID == neighbor.ID):
            self.eastWall = False
        if (self.w != None and self.w.ID == neighbor.ID):
            self.westWall = False

    def draw(self, Z, borderSize, cellSize, edgeSize, lastCell=False):
        drawXBegin = borderSize + ((cellSize + edgeSize)*self.pos[1])
        drawYBegin = borderSize + ((cellSize + edgeSize)*self.pos[0])

        backgroundColor = Color.violet
        overrideFillColor = backgroundColor
        if self.fillColor != None:
            overrideFillColor = self.fillColor

        # Draw Border
        for x in range(0,edgeSize):
            if (self.westWall):
                Z[drawXBegin:drawXBegin+cellSize+edgeSize+edgeSize, drawYBegin+x] = Color.black
            else:
                Z[drawXBegin+edgeSize:drawXBegin+cellSize+edgeSize, drawYBegin+x] = overrideFillColor
                
            if (self.eastWall):
                Z[drawXBegin:drawXBegin+cellSize+edgeSize+edgeSize, drawYBegin+edgeSize+cellSize+x] = Color.black
            else:
                Z[drawXBegin+edgeSize:drawXBegin+cellSize+edgeSize, drawYBegin+edgeSize+cellSize+x] = overrideFillColor

            if (self.northWall and self.pos != (0,0)):
                Z[drawXBegin+x, drawYBegin:drawYBegin+cellSize+edgeSize+edgeSize] = Color.black 
            else:
                Z[drawXBegin+x, drawYBegin+edgeSize:drawYBegin+cellSize+edgeSize] = overrideFillColor 

            if (self.southWall and not lastCell):
                Z[drawXBegin+edgeSize+cellSize+x, drawYBegin:drawYBegin+cellSize+edgeSize+edgeSize] = Color.black
            else:
                Z[drawXBegin+edgeSize+cellSize+x, drawYBegin+edgeSize:drawYBegin+cellSize+edgeSize] = overrideFillColor

        if self.fill or True:
            Z[drawXBegin+edgeSize:drawXBegin+edgeSize+cellSize, drawYBegin+edgeSize:drawYBegin+edgeSize+cellSize] = overrideFillColor 


        

        


