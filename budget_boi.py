import argparse
import csv

from transaction import Transaction
from schema import Categorizer

def budget():
    parser = argparse.ArgumentParser(
        prog="BudgetBoi",
        description="Do various budget related activities."
    )

    parser.add_argument(
        'filename',
        help="Path to csv file containing record of recent transactions."
    )

    parser.add_argument(
        'schema',
        help="Path to JSON file containing a mapping of transaction descriptions -> categories"
    )

    args = parser.parse_args()

    transactions = []

    categorizer = Categorizer(args.schema)

    # open and parse CSV
    with open(args.filename, newline='') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            # print(row)
            if i != 0:
                transactions.append(Transaction(row[1], row[2], row[4], row[5], categorizer))

    categorizer.save()
    
    print("Parsed all transactions!")

if __name__ == "__main__":
    budget()