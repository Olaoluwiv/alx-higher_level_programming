#!/usr/bin/python3
# Prints the number of and the list of its arguments

if __name__ == "__main__":
    from sys import argv

    # Using sys.argv to get the command-line arguments
    argv = sys.argv
    size = len(argv) - 1

    if size < 1:
        print("{} arguments:".format(size))
        for i in range(size):
            print("{}: {}".format(i + 1, arguments[i + 1]))

    elif size == 1:
        print("{} argument.".format(size))

    else:
        print("{} arguments.".format(size))
