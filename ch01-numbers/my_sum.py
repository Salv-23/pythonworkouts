#!/usr/bin/env python3
"""A custom sum function that takes multiple values from a CLI"""

import argparse


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Custom version of a sum function",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "numbers",
        metavar="numbers",
        help="A list of numbers to iterate over e.g python my_sum.py 1 2 3",
        type=int,
        nargs="+",
    )

    return parser.parse_args()


def my_sum(*numbers):
    """Custom sum function

    Takes any quantity of numeric arguments and returns the sum of them.
    """
    total = 0
    for number in numbers:
        total += number
    print(total)


def main():
    """Make a sum of arguments

    Use a list of arguments provided by the user,
    then invoke the custom sum function-
    -unpacking all the gathered arguments.
    """
    arguments = get_arguments()
    my_sum(*arguments.numbers)


if __name__ == "__main__":
    main()
