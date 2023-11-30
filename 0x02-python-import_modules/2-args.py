#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argLen = len(sys.argv)
    if argLen == 1:
        print("{:d} arguments.".format(argLen - 1))
    elif argLen == 2:
        print("{:d} argument:".format(argLen - 1))
    else:
        print("{:d} arguments:".format(argLen - 1))
    for i in range(1, argLen):
        print("{}: {}".format(i, sys.argv[i]))

