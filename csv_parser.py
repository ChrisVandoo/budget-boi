import csv

from transaction import Transaction

class Parser:
    """
    Parses a BMO CSV transaction file.
    Expected format:
        - initial line specifying date transactions are valid from
        - blank line
        - initial line identifying columns
        - transactions
    """

    def __init__(self, filename: str, categorizer: object) -> None:
        self._filename = filename
        self._transactions = []
        self._categorizer = categorizer

    def parse(self):
        """
        Parses the CSV file.
        """

        with open(self._filename, newline='') as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                # if index <= 2:
                #     # Skip the first three lines.
                #     continue
                # else:
                self._transactions.append(Transaction(row[1], row[2], row[4], row[5], self._categorizer))
        
        return self._transactions