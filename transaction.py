import datetime

class Transaction:
    """
    This class should represent the properites of a transaction record.
    """

    def __init__(self, card_number, raw_date, amount, raw_description, schema):
        self._card_number = card_number
        self.date = self._parse_raw_date(raw_date)
        self._amount = amount
        self._description = raw_description
        self._tags = []
        self._category = ""
        self._is_categorized = False

        # Schema should be an object with references to the user's schema, used to categorize, tag etc.
        self._schema = schema
    
    @property
    def card_number(self): return self._card_number
    
    @property
    def date(self): return self._date 

    @property 
    def amount(self): return self._amount

    @property
    def description(self): return self._description

    @property 
    def tags(self): return self._tags 

    @property
    def category(self): return self._category

    @property
    def is_categorized(self): return self._is_categorized

    def _parse_raw_date(self, date):
        """
        Parses a string formatted YYYYMMDD into a datetime object.

        date: String
        @returns: Date object
        """
        if len(date) < 7:
            print("ERROR: date is not long enough...")
            return None

        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:8])

        return datetime.date(year, month, day)
    
    def _parse_raw_description(self, raw_description):
        """
        Should consult something to parse out the name of the store the 
        transaction was made at. Maybe parse other useful data out of the description.
        """

    def _tag_transaction(self):
        """
        Based off of the transaction description and perhaps also some schema
        this function should add tags to the transaction.
        """
    
    def _categorize_transaction(self):
        """
        Based off of the transaction description and perhaps also some schema
        this function should categorize the transaction.
        """

    

