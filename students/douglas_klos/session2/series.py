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

for i in range(20):
    print('fibonacci(' + str(i) + '): ' + str(fibonacci(i)))
for i in range(20):
    print('lucas(' + str(i) + '): ' + str(lucas(i)))

