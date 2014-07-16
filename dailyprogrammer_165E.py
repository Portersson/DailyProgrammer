########################################
# Challenge 165E: ASCII Game of Life   #
#           Date: June 13, 2014        #
########################################
# Experimental Branch
##
import random

gridsize = input(">")
grid = []

class Cell(object):
    def __init__(self,x,y,active):
        self.x = x
        self.y = y
        self.active = active
        self.neighbors =   [(x-1,y-1),(x,y-1),(x+1,y-1),
                            (x-1,y),(x+1,y),
                            (x-1,y+1),(x,y+1),(x+1,y+1)]
    def update(self, grid):
        for i in range(8):
            pass 

def initGrid(gridsize, grid):
    x = 0
    y = 0
    for i in range(int(gridsize)**2):
        if x == int(gridsize):
            x=0
            y+=1
        if y == int(gridsize):
            break
        if random.randint(0,9) == 1: state = True
        else: state = False
        
        grid.append(Cell(x,y,state))
        x+=1
def drawGrid(grid):
    y = 0
    for o in grid:
        if o.y != y:
            print("\n",end='')
            y=o.y
        if o.active: print("#",end='')
        else: print("+",end='')
        

        
initGrid(gridsize,grid)
drawGrid(grid)
input()