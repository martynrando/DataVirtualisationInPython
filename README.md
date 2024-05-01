This project demonstrates how to use Python for data virtualisation by creating data connection objects. 
Data virtualisation creates an abstraction layer over disparate data sources to ensure that analysts are connecting to the appropriate data sources and applying the correct preparation steps. 

The main.py file shows how users can interact with the data_virtualisation package to open a connection and fetch the data. 
The returned data comes in as a standard pandas dataframe, which the user can work with as normal.

Within the data_virtualisation package, connection.py defines the basic Connection class, which is complete with logging, appropriate warnings, standard methods, and caching functionality. 
Data connection owners can create children from this class for each data connection they want to define. They can then override the preview and fetch methods as required.
They should create these in grouped modules to help keep track of what connections already exist, following the format of example_connection.py.
