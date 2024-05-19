import argparse # type: ignore

print(argparse.__doc__) # # type: ignore # Prints Doc Strings Docstrings, short for documentation strings, 
# are vital in conveying the purpose and functionality of Python functions, modules, and classes.
parser = argparse.ArgumentParser(description='Power the integers at the command line')
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument( "-x", type=int, help="the base", metavar="x")
parser.add_argument("-y", type=int, help="the exponent", metavar="y")

## For Positional Arguments Enable the below 
# parser.add_argument( "x", type=int, help="the base")
# parser.add_argument( "y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")