p = '+'
l = '|'

def grid_printer(g_size):
    half_g = g_size // 2
    m = '-' * (half_g)
    s = ' ' * (half_g)

    for i in range(2):
        print(p + m + p + m + p)
        for i in range(half_g):
            print(l + s + l + s + l)
    print(p + m + p + m + p)

# grid_printer(15)

def fancy_grid_printer(rowCol, length):
    m = '-' * length
    s = ' ' * length

    for i in range(rowCol):
        for j in range(rowCol):
            print(p + m, end='')
        print(p)

        for j in range(length):
            for k in range(rowCol):
                print(l + s, end="")
            print(l)

    for j in range(rowCol):
        print(p + m, end="")
    print(p)

# fancy_grid_printer(3, 2)
fancy_grid_printer(5, 3)