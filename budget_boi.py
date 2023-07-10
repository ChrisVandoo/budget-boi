import argparse
import csv

from transaction import Transaction

def budget():
    parser = argparse.ArgumentParser(
        prog="BudgetBoi",
        description="Do various budget related activities."
    )

    parser.add_argument(
        'filename',
        help="Path to csv file containing record of recent transactions."
    )

    args = parser.parse_args()

    transactions = []

    # open and parse CSV
    with open(args.filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            transactions.append(Transaction(row[1], row[2], row[4], row[5]))


if __name__ == "__main__":
    budget()