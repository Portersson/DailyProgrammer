########################################
# Challenge 165E: ASCII Game of Life   #
#           Date: June 13, 2014        #
########################################
import random, os,time

gridsize = int(input(">"))
grid = [[0 for x in range(gridsize)] for i in range(gridsize)]

class Cell(object):
    def __init__(self,x,y,active,gridsize):
        self.x = x
        self.y = y
        self.active = active
        self.activeNeighbors = 9#
        self.activeOnUpdate = active
        self.neighbors =   [[x-1,y-1],[x,y-1],[x+1,y-1],
                            [x-1,y],[x+1,y],
                            [x-1,y+1],[x,y+1],[x+1,y+1]]
        for i in range(8):
            for i2 in range(2):
                if self.neighbors[i][i2] == gridsize:
                    self.neighbors[i][i2] = 0

    def iterate(self, grid):
        activeNeighbors = 0
        for i in range(8):
            if grid[self.neighbors[i][1]][self.neighbors[i][0]].active:
                activeNeighbors += 1
                
        self.activeNeighbors = activeNeighbors #
        if activeNeighbors < 2 or activeNeighbors > 3: self.activeOnUpdate = False
        elif activeNeighbors == 3: self.activeOnUpdate = True

    def update(self):
        self.active = self.activeOnUpdate
        

def initGrid(gridsize, grid):
    x = 0
    y = 0
    for i in range(gridsize**2):
        if x == gridsize:
            x=0
            y+=1
        if y == gridsize:
            break
        if random.randint(0,6) ==1: state = True
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
            if o.active: print('#',end='')
            else: print(",",end='')
    print('')
            
def updateGrid(grid):
    for j in grid: 
        for o in j:
            o.iterate(grid)
    for j in grid:
        for o in j:
            o.update()
        
initGrid(gridsize,grid)
while 1:
    drawGrid(grid)
    updateGrid(grid)
    time.sleep(.08)
