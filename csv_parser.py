import csv

from transaction import Transaction

class Parser:
    """
    Parses a BMO CSV transaction file.
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
            for _, row in enumerate(reader):
                if len(row) < 6:
                    continue
                t = Transaction(row[1], row[2], row[4], row[5], self._categorizer)
                # If we fail to parse the date, assume the row contains invalid data and skip it.
                if t.date:
                    self._transactions.append(t)
        
        return self._transactions