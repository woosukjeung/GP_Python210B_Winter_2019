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

grid_printer(15)