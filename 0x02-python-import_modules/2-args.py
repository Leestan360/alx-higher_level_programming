#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    argv_count = len(argv)
    a = 1
    if argv_count == 0:
        print("{:d} arguments.".format(argv_count))
    elif argv_count == 1:
        print("{:d} argument:".format(argv_count))
        print("{:d}: {:s}".format(a, sys.argv[1]))
    else:
        print("{:d} arguments:".format(argv_count))
            while index <= argv_count:
                print("{:d}: {:s}".format(a, sys.argv[a]))
                a += 1
