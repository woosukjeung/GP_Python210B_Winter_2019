def fibonacci(n):
    count = 0
    a,b = 0,1
    while count < n:
        #begin fibonacci sequence: a now = 1, b now = 0+1
        a, b = b, a+b
        #increment count by 1 with each iteration
        count +=1
    if count == n:
        #return result when nth fibonnci is calculated.
        return a

def lucas(n):
    count = 0
    a,b = 2,1
    while count < n:
        #begin fibonacci sequence: a now = 1, b now = 0+1
        a, b = b, a+b
        #increment count by 1 with each iteration
        count +=1
    if count == n:
        #return result when nth fibonnci is calculated.
        return a


def sum_series(n, *args):
    if args:
        a,b = args
    if a == 2 and b ==1:
        return lucas(n)
    else:
        return fibonacci(n)
