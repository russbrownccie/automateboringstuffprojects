#code is supposed to basically rotate the ascii art in the grid list
#code written to measure x/y axis of the art and then paste on that so a 10x7 pic or 12x12 or whatever should paste correctly

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

x_list = 0
y_list = 0

x_range = (len(grid))
y_range = (len(grid[0]))

for y_axis in range (y_list, y_range):
    for x_axis in range (x_list, x_range):
        print (grid[x_axis][y_axis], end='')
        if x_axis == 8:
            print('')
