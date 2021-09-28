import sqlite3

# connect to database
connection = sqlite3.connect('demo_data.sqlite3')

# make a cursor
cursor = connection.cursor()

# count the rows and apply to a variable
row_count = 0
table = cursor.execute('SELECT * FROM demo')

for row in table:
    row_count += 1

print(row_count)

# check where x AND y are greater than or equal to 5
xy_at_least_5 = 0
table2 = cursor.execute('SELECT * FROM demo WHERE x >= 5 AND y >= 5')

for row in table2:
    xy_at_least_5 += 1

print(xy_at_least_5)

# find unique y values
table3 = cursor.execute('SELECT * FROM demo')
unique_y = len(set([x[2] for x in table3]))

print(unique_y)

# close connection
connection.close()
