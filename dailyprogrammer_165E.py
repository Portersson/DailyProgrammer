########################################
# Challenge 165E: ASCII Game of Life   #
#           Date: June 13, 2014        #
########################################
# Experimental Branch
##
import random, os

gridsize = int(input(">"))
grid = [[0 for x in range(gridsize)] for i in range(gridsize)]

class Cell(object):
    def __init__(self,x,y,active,gridsize):
        self.x = x
        self.y = y
        self.active = active
        self.activeNeighbors = 9#
        self.activeOnUpdate = False
        self.neighbors =   [(x-1,y-1),(x,y-1),(x+1,y-1),
                            (x-1,y),(x+1,y),
                            (x-1,y+1),(x,y+1),(x+1,y+1)]

    def iterate(self, grid):
        activeNeighbors = 0
        for i in range(7):
            if grid[self.neighbors[i][1]-1][self.neighbors[i][0]-1].active:
                activeNeighbors += 1
        if activeNeighbors < 2 or activeNeighbors > 3: self.activeOnUpdate = False
        elif activeNeighbors == 3: self.activeOnUpdate = True

    def update(self):
        self.active = self.activeOnUpdate
        
    def update2(self):
        ##
        activeNeighbors = 0
        for i in range(7):
            if grid[self.neighbors[i][1]-1][self.neighbors[i][0]-1].active:
                activeNeighbors += 1
        self.activeNeighbors = activeNeighbors #
        ##

def initGrid(gridsize, grid):
    x = 0
    y = 0
    for i in range(gridsize**2):
        if x == gridsize:
            x=0
            y+=1
        if y == gridsize:
            break
        if random.randint(0,8) == 1: state = True
        else: state = False
        
        grid[y][x]=Cell(x,y,state,gridsize) #Because console prints line by line (each line being a Y coord), Y must be first
        x+=1
def drawGrid(grid):
    os.system('cls')
    y = 0
    for j in grid: 
        for o in j:
            if o.y != y:
                print("\n",end='')
                y=o.y
            if o.active: print(o.activeNeighbors,end='')
            else: print("+",end='')
            
def updateGrid(grid):
    for j in grid: 
        for o in j:
            o.iterate(grid)
    for j in grid:
        for o in j:
            o.update()
    for j in grid:
        for o in j:
            o.update2()
        
initGrid(gridsize,grid)
while 1:
    drawGrid(grid)
    updateGrid(grid)
    input()
