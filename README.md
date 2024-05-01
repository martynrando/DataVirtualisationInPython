This project demonstrates how you can use Python for data virtualisation by creating data connection objects. 

The main.py file shows how a user can interact with the data_virtualisation package to open a connection and fetch the data. 
The returned data comes in as a standard pandas dataframe, which the user can work with as normal.

Within the data_virtualisation package, connection.py defines the basic Connection class, complete with logging, appropriate warnings and standard methods. 
Data connection owners can create children from this class for each data connection that they want to define. They can then override the preview and fetch methods.
They should create these in grouped modules to help keep track of what connections already exist.
