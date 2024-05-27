"""Greeter.

Usage:
  commands.py hello
  commands.py goodbye
  commands.py -h | --help

Options:
  -h --help     Show this screen.
"""
from docopt import docopt # type: ignore

if __name__ == '__main__':
    arguments = docopt(__doc__)