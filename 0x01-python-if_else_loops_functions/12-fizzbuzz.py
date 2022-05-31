#!/usr/bin/python3
def fiizbuzz():
    for a in range(1, 101):
        if a % 3 == 0:
            print("Fizz ")
        elif a % 5 == 0:
            print("Buzz ")
        elif a % 15 == 0:
            print("FizzBuzz ")
        else:
            print(a, end=" ")
