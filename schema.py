import json

"""
{
    "TRANSACTION_DESC": {
        "NAME": "",
        "CATEGORY": ""
    }
}
"""

class Schema:
    """
    Class that wraps the schema used to normalize transaction records.
    """

    def __init__(self, schema_path):
        self._schema_path = schema_path
        self._schema = {}

        with open(schema_path, "r") as f:
            self._schema = json.load(f)

    def get_transaction(self, transaction_desc):
        """ 
        Returns the schema for the specified transaction description.
        """
        return self._schema['schema'].get(transaction_desc)
    
    def update_transaction(self, transaction_desc, category):
        """
        Should update the specified part of the schema with new stuff.
        """
        self._schema['schema'][transaction_desc] = {"category": category}
    
    def get_categories(self):
        """
        Returns the map of category:{}
        """
        return self._schema.get('categories')

    def save(self):
        """
        Should write the updated schema back to the original file.
        """
        with open(self._schema_path, "w") as f:
            json.dump(self._schema, f)

class Categorizer:
    """
    This class is the UI/engine used to classify transactions and manipulate the schema.
    """

    def __init__(self, schema_path) -> None:
        self._schema = Schema(schema_path)
        self._categories_by_index = []
        self._prompt = self._generate_prompt()
    
    def run(self, transaction_description):
        """
        Tries to automatically find the category for the transaction and return it. 
        If the transaction description doesn't match anything in the schema, the user
        is prompted to categorize the transaction manually.
        """
        if not transaction_description:
            print("No transaction description provided.")
            return None
        
        # If this is not None, we've managed to automatically assign the category.
        _category = None
        transaction_schema = self._schema.get_transaction(transaction_description)
        if transaction_schema:
            _category = transaction_schema['category']

        if not _category:
            print("What should this be categorized as?")
            # Prompt the user to manually assign the category
            # TODO this will break if user enters invalid input
            choice = input(self._prompt)
            _category =  self._categories_by_index[int(choice) - 1]
            self._schema.update_transaction(transaction_description, _category)
               
        return _category

    def save(self):
        self._schema.save()

    
    def _generate_prompt(self):
        """
        Returns a nice prompt with all the categories and things.
        """
        prompt = "Please enter the number of one of the following categories: \n"
        index = 1
        categories = self._schema.get_categories()

        for category, stuff in categories.items():
            prompt += f"[{index}] {category}: {stuff.get('description')} \n"
            self._categories_by_index.append(category)
            index+=1

        prompt += ">"
        return prompt