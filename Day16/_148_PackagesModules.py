# Importing and using python modules/packages.
from preetytable import PreetyTable

table = PreetyTable()  # class
table.add_column("Veg_name", ["Squash", "Tomato", "Zuchini", "Beans"])  # call methods
print(table)
table.add_column("Eaten", ["Cooked", "Uncooked"])

# changing objects attributes
table.align = "l" # left align