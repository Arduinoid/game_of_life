# importing random.py
import random

# This function creates a row out of an array
def row(width):
    row = []
    for i in range(width):
        row.append(random.randint(0,1))
    return row

# print row(8)

# This funciton will call the row() funciton and create a grid from it
def grid(rows, columns):
    grid_array = []
    for i in range(rows):
        grid_array.append(row(columns))
    return grid_array

# print grid(4,8)

# This funciton helps to know what the size of the grid is
def gridSize(grid):
    num_of_cols = len(grid)
    num_of_rows = len(grid[0])
    grid_dimensions = [num_of_cols, num_of_rows]
    return grid_dimensions

# print gridSize(grid(4,8))

# <<<<<< IN PROGRESS >>>>> #
def cellCheck(grid, position):
    '''
    This function takes two arguments
    grid = would be a two dimensional array
    position = would be a list of two items [x,y]
    It would then output a 1 or a 0 depending on the sum value surrounding
    the cell position. This value is obtained from calling the function
    cellSurroundSum()

    reference grid for indexing
        0 1 2 3 4 5 6 7
        | | | | | | | |
    0 - 0 0 0 0 X 0 0 0
    1 - 0 X X X 0 X 0 0
    2 - X X 0 0 X 0 0 0
    3 - 0 X 0 0 0 0 0 0

    cellCheck(grid, [2,2])
    >> 0
    cellCheck(grid, [5,1])
    >> 1
    cellCheck(grid, [1,2])
    >> 0
    cellCheck(grid, [3,2])
    >> 1
    '''

    column = [position[0]]
    row = [position[1]]
    cell = grid[row][column]

    cell_surround_total = cellSurroundSum(grid, column, row)

    if cell == 1:
        # check how many neighnors to perform certain logic

    else:
        # Perform logic for dead cell 

# Building a function to obtain the surrounding cell values
# then output the sum of those values
def cellSurroundSum(grid, column, row):
    cell_value = grid[column][row]
    shift = [-1, 0, 1]
    cell_sum = 0
    for i in range(3):
        section = grid[row + shift[i]]
        for i in range(3):
            cell_sum += section[column + shift[i]]

    return cell_sum - cell_value


# Passing the grid() function to this function will render the grid in characters
def gridRender(grid, dead=None, alive=None):
    cell = [dead, alive]
    if cell[0] == None or cell[1] == None:
        for line in grid:
            print line
    else:
        row = ""
        for line in grid:
            for item in line:
                row += cell[item]
            print row
            row = ""

# This funciton will take a grid input and will swap the bits from 0 to 1 or 1 to 0
# depending on the current value of each bit
def cellShift(grid):
    row = []
    new_grid = []
    for line in grid:
        for item in line:
            row.append(0 if item else 1)

        new_grid.append(row)
        row = []
    return new_grid

#<<<<< TESTING >>>>>>#

# capture the grid state in a variable
life_grid = grid(4,8)
# for i in life_grid:
#     print i
# throw this print here for spacing between the two outputs
# print
# This is testing the cellShift funciton
# shifted = cellShift(life_grid)
# for i in shifted:
#     print i

# grid render that defaults to raw grid
gridRender(life_grid)
print cellSurroundSum(life_grid, 2, 2)
# grid render using character replacment arguments
# gridRender(life_grid, "x", "o")
