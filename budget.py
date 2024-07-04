from schema import Schema

class Budget:
    """
    Parses an array of Transactions to determine how they match up to the specified budget.
    """
    def __init__(self, transactions, schema_path) -> None:
        self._categories = Schema(schema_path).get_categories()
        self._transactions = transactions
        self._budget = {}
        self._curr_timeframe = ""
    
    def budget(self, month="", year=""):
        """
        Compares the transactions with the budget defined by category in the schema
        to see how we are doing for our budget.
        """
        results = {category: 0 for category in self._categories.keys()}
        if month and year:
            self._curr_timeframe = f"{month} {year}"

        for transaction in self._transactions:
            # Only show budget for given time period
            if month and year:
                if transaction.month != month or transaction.year != year:
                    continue

            amount = float(transaction.amount)
            curr_total = float(results[transaction.category])
            new_total = amount + curr_total
            results[transaction.category] = new_total

        self._budget = results
    
    def results(self):
        """
        Print out results of budget.
        """
        total = 0
        budget_total = 0

        print("\n\n================== BUDGET ==================")
        if self._curr_timeframe:
            print(self._curr_timeframe)
        print("--------------------------------------------")
        print("Category | Actual | Budgeted")
        print("--------------------------------------------")
        for category, amount in self._budget.items():
            if category != 'Transfer' and category != 'Other':
                total = float(total) + float(amount)
                budget_total = float(budget_total) + float(self._categories[category].get('amount'))
            print("{}: ${:.2f} / ${:.2f}".format(category, amount, self._categories[category].get('amount')))
        print("--------------------------------------------")
        print("Total: ${:.2f} / ${:.2f}".format(total, budget_total))
        print("============================================\n\n")

    def print_csv(self, month="", year=""):
        """
        Prints transactions for the month, tagged by category.
        CSV: date, amount, description, category
        """
        out = []
        for t in self._transactions:
            # Only show budget for given time period
            if month and year:
                if t.month != month or t.year != year:
                    continue
            
            out.append(f"{t.date},{t.amount},{t.description},{t.category}\n")
        
        with open(f"{month}-{year}-parsed-transactions.csv", "w") as f:
            f.writelines(out)

