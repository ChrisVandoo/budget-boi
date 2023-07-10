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

    def get(self, transaction_desc):
        """ 
        Returns the schema for the specified transaction description.
        """
        return self._schema.get(transaction_desc)
    
    def update(self, transaction_desc, schema_body):
        """
        Should update the specified part of the schema with new stuff.
        """
        self._schema[transaction_desc] = schema_body

    def save(self):
        """
        Should write the updated schema back to the original file.
        """
        with open(self._schema_path, "w") as f:
            json.dump(self._schema, f)