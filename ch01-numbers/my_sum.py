import argparse


def my_sum(*numbers):
    """Custom sum function

    Takes any number of numeric arguments and returns the sum of them.
    """
    total = 0
    for number in numbers:
        total += number
    print(total)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="Custom version of a sum function"
            )
    parser.add_argument(
        "numbers",
        type=int,
        nargs="+",
        help="A list of numbers to iterate over e.g., python my_sum.py 1 2 3",
    )
    # Retrieve values from parser: [('numbers', [1, 2, 3])]
    numbers = parser.parse_args()._get_kwargs()[0][1]
    # Unpacking values from list
    my_sum(*numbers)
