#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) >= ord('A') and ord(a) <= ord('Z'):
            character = chr(ord(a) - 32)
        else:
            character = a
        print('{:s}'.format(character), end="")
    print("")
