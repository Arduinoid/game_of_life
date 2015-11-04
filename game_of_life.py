import random

def row(width):
    row = []
    for i in range(width):
        row.append(random.randint(0,1))
    return row

# print row(8)

def grid(rows, columns):
    grid_array = []
    for i in range(rows):
        grid_array.append(row(columns))
    return grid_array

# print grid(4,8)

def gridRender(grid):
    cell = [".", "*"]
    row = ""
    for line in grid:
        for item in line:
            row += cell[item]
        print row
        row = ""

def cellShift(grid):
    row = []
    new_grid = []
    for line in grid:
        for item in line:
            # email: erik.bernoth@gmail.com
            # row.append(0 if item else 1)
            if item == 1:
               row.append(0)
            else:
               row.append(1)
        new_grid.append(row)
        row = []
    return new_grid

life_grid = grid(4,8)
shifted = cellShift(life_grid)

for i in shifted:
    print i

print

for i in life_grid:
    print i

# gridRender(life_grid)
