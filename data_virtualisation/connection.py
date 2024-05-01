"""
NAME
    connection - defines a basic Connection class for developers to build more data connections

PACKAGE CONTENTS
    Connection: the basic Connection class
"""
import pandas as pd
import logging.config
import logging.handlers
import json
from typing import Dict
import pickle
import os


def setup_logging():
    config_file = os.path.join(os.path.dirname(__file__), "logging_config/config.json")
    with open(config_file) as file:
        config = json.load(file)
    logging.config.dictConfig(config)


class Connection:
    """
    This is the Connection parent class that you will use to define your data connections.
    To create a new data connection class, use the format:

    class MyDataConnection(Connection):
        '''
        Choose an appropriate name for your data connection and explain it in the docstring.
        '''
        def __init__(self, purpose):
            super.__init__(purpose, force_purpose = False, persist_cache = False)

        def preview(self):
            # define your code here to return the top 10 rows of data

        def fetch(self):
            # define your code here to return all data

        def validate(self):
            # if you choose to implement data validation for your returned data, add the validation
            # checks and processes in here

    Attributes
    ----------
    purpose: str
        A short description of the reason that the user is opening the connection and reading the data.
    logger: logging.Loger
        The logging object for the connection is managed at the admin level.
        You can display log messages in your code by using
        self.logger.debug('This is a debug message that will not show to users.')
        self.logger.info('This is an information message that will show to users.')
        self.logger.warning('This is a warning message that will show to users.')
        self.logger.error('This is an error message that will show to users.')
        self.logger.critical('This is a critical message that will show to users.')
    persist_cache: bool
        True if the cache is to be persisted as a pickle file, otherwise False.
    pickle_file: str
        If the cache is persisted, this string holds the name of the cache file.
    cached_values: pd.DataFrame
        If the cache is not persisted, this variable holds the return dataframe.

    Methods
    -------
    preview()
        Return the first 10 rows of data from the connection.
    fetch()
        Return all the rows of data from the connection.
    cache()
        Store a copy of the data locally and use it for future preview and fetch methods.
    validate()
        Apply data validation checks and rules to the data.
    """

    def __init__(self, purpose: str = None, *, force_purpose: bool = False, persist_cache: bool = False):
        """
        This is the initialiser method for your data connection.
        It sets the attributes of the connection object.
        To override this method in your data connection class, use the format:

        def __init__(self, purpose: str = None):
            super.__init__(
                purpose,
                force_purpose = False,
                persist_cache = False
            )

        :param purpose: A short description of the reason that the user is opening the connection and reading the data.
        :param force_purpose: To force the user to enter a purpose,
            set force_purpose = True in your super.__init__() call.
        :param persist_cache: To set the cache to persist in a pickle file,
            set persist_cache = True in your super.__init__() call.
        """

        # purpose: check that the purpose is set and raise a value error if necessary.
        if purpose is None and force_purpose:
            raise ValueError('Please provide a purpose for this connection.')
        self.purpose: str = purpose

        # logger: set up the logger to log errors with the connection.
        self.logger = logging.getLogger("data_connections")
        setup_logging()

        # cache: set up the cache either as a file or a variable.
        self.persist_cache: bool = persist_cache
        if self.persist_cache:
            self.pickle_file: str = 'cached_values.pkl'
        else:
            self.cached_values: pd.DataFrame | None = None

    def preview(self) -> pd.DataFrame:
        """
        This method returns the top 10 rows of data from the data connection.
        To override this method in your data connection class, use the format:

        def preview(self):
            # define your code here to return the top 10 rows of data
        ---

        :return: pd.DataFrame
            preview of the top 10 rows of data from the connection
        """
        self.logger.error(f'Sorry, the preview method has not been implemented on {type(self).__name__}.')
        return pd.DataFrame({})

    def fetch(self) -> pd.DataFrame:
        """
        This method returns all data from the data connection.
        To override this method in your data connection class, use the format:

        def fetch(self):
            # define your code here to return all data
        ---

        :return: pd.DataFrame
            all data from the connection
        """
        self.logger.error(f'Sorry, the fetch method has not been implemented on {type(self).__name__}.')
        return pd.DataFrame({})

    def cache(self, full_df: pd.DataFrame = None) -> bool:
        """
        This method manages the cached values for the data connection.
        If the cache is empty, it returns False.
        If the cache is loaded, it returns True.
        The default cached_values are stored as a pandas dataframe on the connection object.
        To persist the cache as a pickle file, set persist_cache = True in your __init__ override:

        class MyDataConnection(Connection):
            def __init__(self, purpose: str = None):
                super.__init__(purpose, persist_cache = True)
        ---

        :param full_df: The fetched data to cache.
        :return: bool
            True if the cache is loaded, otherwise False
        """
        if self.persist_cache:
            if full_df is None:
                return os.path.exists(self.pickle_file)
            with open(self.pickle_file, 'wb') as file:
                pickle.dump(full_df, file)
                return True
        else:
            if full_df is None:
                print(self.cached_values is not None)
                return self.cached_values is not None
            self.cached_values = full_df
            return True

    def load_cached_data(self) -> pd.DataFrame:
        """
        This method returns the data from the cache.
        To use this in your .fetch() method, use the code:

        if self.cache():
            return self.load_cached_data()
        ...
        self.cache(data)
        ---

        :return: pd.DataFrame
            cached dataframe
        """
        if self.persist_cache:
            with open(self.pickle_file, 'rb') as file:
                return pickle.load(file)
        else:
            return self.cached_values

    def validate(self, data: pd.DataFrame) -> Dict[str, pd.DataFrame]:
        """
        This method validates the data from the connection and applies data quality auditing steps.
        This method uses self.logger.info('Info message') to log data quality issues.
        To override this method in your data connection class, use the format:

        def validate(self):
            # define your code here to validate the data
        ---

        :return: Dict['valid': pd.DataFrame, 'invalid': pd.DataFrame]
            a dictionary showing the valid and invalid rows of data
        """
        self.logger.error(f'Sorry, the validate method has not been implemented on {type(self).__name__}.')
        return {'valid': pd.DataFrame({}), 'invalid': pd.DataFrame({})}

    def __repr__(self):
        return f'''{type(self).__name__}(purpose: str = "{self.purpose}") has methods:
            .fetch() -> pd.DataFrame: 
                returns all data from the connection
            .preview() -> pd.DataFrame: 
                returns the top 10 rows from the connection
            .validate() -> Dict['valid': pd.DataFrame, 'invalid': pd.DataFrame]: 
                returns the valid data and invalid data as two dictionary entries
            
            For more information on the Connection class or on one of these methods, use the help() function.
            e.g. help(Connection)
            '''

    def __str__(self):
        return f'Data connection to {type(self).__name__} returns a pandas dataframe.'


def main():
    help(Connection)
    setup_logging()


if __name__ == '__main__':
    main()
