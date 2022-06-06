#!/usr/bin/python3
def no_c(my_string):
    for a in range(len(my_string)):
        if a == 'c' or a == 'C':
            my_string.remove(a)
            return my_string
