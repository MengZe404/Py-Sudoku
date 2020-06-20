import numpy as np
from numpy import array

# grid = np.empty(shape = [9, 9], dtype = object)

grid = array([
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [5, 4, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
])

GRIDSIZE = 9

fullset = {0,1,2,3,4,5,6,7,8,9}

def possible():
    for row in range(0, GRIDSIZE):
        for col in range(0, GRIDSIZE):
            if grid[row][col] == 0:
                possible_row = fullset - set(grid[row])
                possible_col = possible_row - set(grid[col])
                square_row_index = (row // 3) * 3
                square_col_index = (col // 3) * 3 
                square_occupied = set(grid[square_row_index][square_col_index])   
                print(square_occupied)
                

possible()
