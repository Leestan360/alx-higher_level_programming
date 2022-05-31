#!/usr/bin/python3
for a in range(0, 100):
    if a == 99:
        print(a)
    else:
        if len(str(a)) == 1:
            print('{}{}'.format(0, a), end=", ")
        else:
            print('{}'.format(a), end=", ")
