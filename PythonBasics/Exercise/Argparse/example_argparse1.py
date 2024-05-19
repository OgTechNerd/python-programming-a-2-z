import argparse

def print_arparse_version():
    print(argparse.__version__)
parser = argparse.ArgumentParser()
parser.add_argument("arg1",  help="First Arguement")
parser.add_argument("arg2", help="Second Argument")
parser.add_argument("arg3", help="Third Argument")

args = parser.parse_args()
print (f"First argument: {args.arg1}\nSecond argument: {args.arg2}\nThird argument: {args.arg3}")
print_arparse_version