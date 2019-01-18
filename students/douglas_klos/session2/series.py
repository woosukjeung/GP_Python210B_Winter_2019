#!/usr/bin/python3

# Douglas Klos
# January 19th, 2019
# Python 210, Assigment 2
# series.py

# Fibonacci sequency is nautually recursive, fib(n) = fib(n-2) + fib(1)
# One of the few recursive problems I remember, so I'm using it!
def fibonacci(n):
    if (n <= 1):
        return n
    return fibonacci(n-2) + fibonacci(n-1)

# Lucas numbers are also equal to the sum of the previous two numbers in the series.
# They however start differently: When n=0, lucas = 2 and when n=1, lucas = 1.
# We can again use recursion for the solution with different initial conditions.
def lucas(n):
    if (n == 0):
        return 2
    if (n == 1):
        return 1
    return lucas(n-2) + lucas(n-1)

def sum_series(n, n0=0, n1=1):
    if (n == 0):
        return n0
    if (n == 1):
        return n1
    return sum_series(n-2,n0,n1) + sum_series(n-1,n0,n1)

if __name__ == "__main__":
#    for i in range(10):
#        print('fibonacci(' + str(i) + '): ' + str(fibonacci(i)))
#    for i in range(10):
#        print('lucas(' + str(i) + '): ' + str(lucas(i)))
#    for i in range(10):
#        print('sum_series(' + str(i) + '): ' + str(sum_series(i,0,1)))
#    for i in range(10):
#        print('sum_series(' + str(i) + '): ' + str(sum_series(i,2,1)))

    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    assert lucas(0) == 2
    assert lucas(1) == 1

    assert lucas(4) == 7

    assert sum_series(5) == fibonacci(5)

    # test if sum_series matched lucas
    assert sum_series(5, 2, 1) == lucas(5)

    print("tests passed")
