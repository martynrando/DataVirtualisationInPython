"""
NAME
    customer - the data connections owned by the customer analytics team

PACKAGE CONTENTS
    ExampleConnection: the data connection class for the customer purchases data
        This data contains all the customer information from the customer table and
        any associated purchases through the POS system.
"""
from data_virtualisation.connection import Connection
import time
import pandas as pd


# To establish a new data connection, the developer can create a new class using the Connection class.
# They can use the Connection class .__init__() method to provide specifications for their connection.
# They can override the .preview() and .fetch() methods to pull data from a database, Excel file or anywhere else
# and run any joins or preparation steps.
# They can also create a .validate() method to check the data quality of the result.
class ExampleConnection(Connection):
    """
    This is an example data connection, created by Name and owned by Team.
    """
    def __init__(self, purpose: str = None):
        super().__init__(purpose, persist_cache=True)

    def preview(self):
        return pd.read_csv('ftse_250.csv', nrows=10)

    def fetch(self):
        if self.cache():
            return self.load_cached_data()
        time.sleep(2)
        data = pd.read_csv('ftse_250.csv')
        self.cache(data)
        return data  # self.validate(data)['valid']


# This section is used for testing the example connection.
def main():
    start = time.time()
    data_conn = ExampleConnection(
        purpose="Creating a segmentation model."
    )
    print(data_conn.preview())
    print(data_conn.fetch())


if __name__ == '__main__':
    main()
