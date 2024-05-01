from data_virtualisation.example_connection import *


# Once the developers have written the connection classes, users can open a data connection using the format:
data_con = ExampleConnection()

# Users can then choose to preview the data or fetch all the data:
df = data_con.fetch()

# If the developer has implemented a validation method, users can apply it to the data:
data_con.validate(df)

# The result of the preview or fetch is a normal pandas dataframe that users can work with
print(df.head())
