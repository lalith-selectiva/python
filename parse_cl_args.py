import sys

args = sys.argv[1:]
for arg in args:
    arg_split = arg.split(' ')
    for arg1 in arg_split:
        print(arg1)