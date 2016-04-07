from cell import Cell
from collections import deque
import random
from colors import Color

iteration = 0
f = open('/Users/zfleischman/repos/mazes/logs/mazeLog.txt', 'w+')

def printQ(Q):
    x = []
    for y in Q:
        x.append(y.ID)
    return x

def process(cell, Q):
    global iteration,f
    f.write(repr((iteration, cell.ID, printQ(Q))))
    f.write("----\n")
    iteration += 1
    # Mark cell as visited
    cell.visited = True

    # Add to Q
    Q.append(cell)

    (retValue, neighbor) = cell.connectToRandomUnvisitedNeighbor()
    return (retValue, neighbor, Q)

def generateMaze(maze):
    startX = random.randint(0,len(maze))
    startY = random.randint(0,len(maze[0]))

    cell = maze[startX][startY]

    firstTime = True
    Q = deque()
    while firstTime or Q:
        firstTime = False
        (retValue, neighbor, Q) = process(cell, Q)
        # If we successfully appended neighbor, process the neighbor
        if (retValue == 0):
            cell = neighbor
        # If we have no unvisited neighbors, remove from Q
        elif (retValue == 1):
            Q.pop()

        if Q and retValue != 0:
            cell = Q.popleft()

def getRandomMaze(w,h):
    newMaze = [[0 for x in range(h)] for x in range(w)]
    cellID = 1
    for x in range(w):
        for y in range(h):
            newMaze[x][y] = Cell(cellID, (x,y))
            cellID += 1
    for x in range(w):
        for y in range(h):
            if (y > 0):
                newMaze[x][y].n = newMaze[x][y-1]
            if (y < h-1):
                newMaze[x][y].s = newMaze[x][y+1]
            if (x > 0):
                newMaze[x][y].w = newMaze[x-1][y]
            if (x < w-1):
                newMaze[x][y].e = newMaze[x+1][y]

    generateMaze(newMaze)

    return newMaze

