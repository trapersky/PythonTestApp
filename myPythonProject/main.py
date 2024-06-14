#this is just a simple program to show a few basic concepts of python coding

import os

name = os.getlogin()

print(f'\nHello {name}!')

print('\nPlease enter number of times the function will be run!')
runs = int(input())

def number_of_runs():
     for i in range(runs):
        print("\nThe function is running!")

number_of_runs()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
