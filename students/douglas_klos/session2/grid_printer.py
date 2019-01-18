#!/usr/bin/python3

# Douglas Klos
# January 19th, 2019
# Python 210, Assignment 2
# grid_printer.py

# Simply prints the static 2 x 2 grid shown at the start of the assignment.
def print_grid0():
    str1 = '+ ' + '- ' * 4 + '+ ' + '- ' * 4 + '+ ' + '\n'
    str2 = '| ' + '  ' * 4 + '| ' + '  ' * 4 + '| ' + '\n'

    print(str1 + str2 * 4 + str1 + str2 * 4 + str1)

# Value passed to function is the total width and height of the grid sans edges.
# Since grid has static two rows and two columns, odd numbers are floored during division.
# Problem was underspecified, this seemed reasonable, output matches examples given.
def print_grid1(x):
    if x < 0:
        print('Enter a number 0 or larger for cell size')
        return
    size = x // 2

    str1 = ('+ ' + '- ' * size + '+ ' + '- ' * size + '+' + '\n')
    str2 = ('| ' + '  ' * size + '| ' + '  ' * size + '|' + '\n')
    print(str1 + str2 * size + str1 + str2 * size + str1)

# X is the number of rows & columns.
# Y is the number of units in each grid cell.
def print_grid2(x,y):
    if x <= 0 or y < 0:
        print('Enter Row & Column count > 0, and cell size >= 0')
        return
    for a in range(x):
        print((('+ ' + '- ' * y) * x) + '+')
        for b in range(y):
            print((('| ' + '  ' * y) * x) + '|')
    print((('+ ' + '- ' * y) * x) + '+\n')


print_grid0()
print_grid1(3)
print_grid1(11)
print_grid1(15)
print_grid2(3,4)
print_grid2(5,3)

