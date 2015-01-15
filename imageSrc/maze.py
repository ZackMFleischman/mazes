


import numpy
from numpy.random import random_integers as rand
import matplotlib.pyplot as pyplot
import MazeGenerator
from colors import Color
from MazeGenerator import printQ
import sys

sys.setrecursionlimit(10000)

# Parameters
borderSize = 5
edgeSize = 1
cellSize = 5

cellsX=160
cellsY=130

f = open('/Users/zfleischman/scripts/mazes/mazeLog2.txt', 'w')

def solveHelper(S, goal):
    global f
    if not S:
        return (False, [])
    f.write(repr(printQ(S)))
    f.write("----\n")
    
    cell = S.pop()
    cell.visited = True
    if (cell.ID == goal.ID):
        f.write("FOUND GOAL\n")
        S.append(cell)
        return (True, S)

    solved = False
    if not solved and cell.s != None and not cell.s.visited and not cell.southWall:
        f.write("Go South\n")
        S.append(cell.s)
        (solved, S) = solveHelper(S, goal)
    if not solved and cell.w != None and not cell.w.visited and not cell.westWall:
        f.write("Go West\n")
        S.append(cell.w)
        (solved, S) = solveHelper(S, goal)
    if not solved and cell.e != None and not cell.e.visited and not cell.eastWall:
        f.write("Go East\n")
        S.append(cell.e)
        (solved, S) = solveHelper(S, goal)
    if not solved and cell.n != None and not cell.n.visited and not cell.northWall:
        f.write("Go North\n")
        S.append(cell.n)
        (solved, S) = solveHelper(S, goal)
    
    if solved:
        f.write("Solved!\n")
        S.insert(0, cell)
        return (True, S)
    else:
        f.write("Backing up\n")
        return solveHelper(S, goal)



def solve(start, end):
    global f
    stack = [start] 
    (retValue, finalStack) = solveHelper(stack, end)
    if retValue:
        f.write(repr(printQ(finalStack)))
        f.write("----\n")
        for cell in finalStack:
            cell.fillColor = Color.yellow

def maze(width=80, height=50):

    # White out maze
    Z = numpy.ones((height+borderSize,width+borderSize,3), dtype=float)

    # Generate Maze
    maze = MazeGenerator.getRandomMaze((cellsX, cellsY));

    # Reset
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            maze[x][y].visited = False


    # Solve Maze
    cellStart = maze[0][0]
    cellEnd = maze[len(maze)-1][len(maze[0])-1]
    solve(cellStart, cellEnd)

    # Draw Maze
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if (x == len(maze)-1) and (y == len(maze[0])-1):
                maze[x][y].draw(Z, borderSize, cellSize, edgeSize, True)       
            else:
                maze[x][y].draw(Z, borderSize, cellSize, edgeSize)       
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if (maze[x][y].fillColor == None):
                if (x == len(maze)-1) and (y == len(maze[0])-1):
                    maze[x][y].draw(Z, borderSize, cellSize, edgeSize, True)       
                else:
                    maze[x][y].draw(Z, borderSize, cellSize, edgeSize)       
    return Z



pyplot.figure(figsize=(18, 14))
sizeX = borderSize*2 + edgeSize + (edgeSize+cellSize)*cellsX
sizeY = borderSize*2 + edgeSize + (edgeSize+cellSize)*cellsY
pyplot.imshow(maze(sizeX, sizeY), cmap=pyplot.cm.binary, interpolation='nearest')
pyplot.xticks([]), pyplot.yticks([])
pyplot.show()
pyplot.savefig("maze.png")


