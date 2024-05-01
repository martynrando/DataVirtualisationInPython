"""
NAME
    data_virtualisation - A package for data virtualisation in Python

PACKAGE CONTENTS
    connection: defines a basic Connection class for developers to build more data connections
    customer: the data connections owned by the customer analytics team

NOTES
    since this package is internal and not for distribution
    and connections are to be build out iteratively in an Agile fashion,
    the package is left as a shared folder
"""
import os


print('Welcome to the data virtualisation package! Here are some of the connection groups to explore:')

developer_files = [
    '__init__', '__pycache__', 'logging_config', 'logs', 'ftse_250.csv', 'connection'
]

for file in os.listdir(os.path.dirname(__file__)):
    file = file.strip('.py')
    if file in developer_files:
        continue
    print('\t' + file)

print('\nTo access the connections in a group, import data_virtualisation.group.')
print('e.g. import data_virtualisation.customer\n\n')
