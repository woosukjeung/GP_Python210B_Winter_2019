#!/usr/bin/env python3

# Douglas Klos
# January 20th, 2019
# Python 210
# list_lab.py


def display_list(seq):
    print(seq)


def append_fruit(fruit_list):
    response = input("Please enter the na me of fruit to be added: ")
    fruit_list.append(response)

if __name__ == "__main__":

    fruit = ("Apples", "Pears", "Oranges", "Peaches")

    display_list(fruit)
    append_fruit(fruit)
