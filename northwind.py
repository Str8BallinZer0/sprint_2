import sqlite3

connection = sqlite3.connect('northwind_small.sqlite3')
curs = connection.cursor()

# get all the column names
# print(curs.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;").fetchall())

# print(curs.execute('SELECT sql FROM sqlite_master WHERE name="Customer";').fetchall())

# ten most exp items per unit
expensive_items = [x for x in curs.execute('SELECT * FROM Product ORDER BY UnitPrice DESC LIMIT 10')]
print(expensive_items)

# make a list of ages then sum and divide by length
# would normally import datetime but didn't know if that was allowed so I grabbed the year as an int and approximated
age_list = [int(x[6].split('-')[0]) - int(x[5].split('-')[0]) for x in curs.execute('SELECT * FROM Employee')]
avg_hire_age = sum(age_list)/len(age_list)
print(avg_hire_age)

# ten most expensive items and their suppliers... returning all columns...
ten_most_expensive = [x for x in curs.execute('SELECT * FROM Product INNER JOIN Supplier ON Supplier.ID = Product.SupplierID ORDER BY UnitPrice DESC LIMIT 10')]
print(ten_most_expensive)

# largest category by number of unique products
list_cat = [x[0] for x in curs.execute('SELECT CategoryName FROM Category INNER JOIN Product ON Product.CategoryID = Category.ID')]
# after making a list that joins categoryid on individual product id's just have to find the mode
largest_category = max(set(list_cat), key=list_cat.count)
print(largest_category)

connection.close()