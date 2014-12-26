import sys
import pygame
import random
from colors import Color
from cell import Cell
pygame.init() 

def resetMaze(maze, width, height):
    for x in range(0, width):
        for y in range(0, height):
            maze[x][y].visited = False

# Parameters
windowWidth = 640
windowHeight = 480
cellSize = 20
cellThickness = 3
width = (windowWidth-1)/cellSize
height = (windowHeight-1)/cellSize

# Colors
edgeColor = Color.blue

#create the screen
window = pygame.display.set_mode((windowWidth, windowHeight)) 

# Create the maze cells
maze = [[0 for x in range(height)] for x in range(width)]
stack = []
nextID = 0
for x in range(0, width):
    for y in range(0, height):
        maze[x][y] = Cell(nextID, (cellSize/2.0 + x*cellSize, cellSize/2.0 + y*cellSize), cellSize, edgeColor, cellThickness)
        nextID += 1
        stack.insert(random.randint(0,len(stack)), maze[x][y])
for x in range(0, width):
    for y in range(0, height):
        if (x != 0):
            maze[x][y].n = maze[x-1][y]
        if (y < height-1):
            maze[x][y].e = maze[x][y+1]
        if (x < width-1):
            maze[x][y].s = maze[x+1][y]
        if (y != 0):
            maze[x][y].w = maze[x][y-1]

# Construct the maze
while (len(stack) != 0):
    node = stack.pop()
    node.addEdge()
    resetMaze(maze, width, height)

# Draw the maze
for x in range(0, width):
    for y in range(0, height):
        maze[x][y].draw(window)


#draw it to the screen
pygame.display.flip() 

#input handling (somewhat boilerplate code):
while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            sys.exit(0) 
        else: 
            print event

