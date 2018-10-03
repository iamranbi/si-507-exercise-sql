import sqlite3 as sqlite
conn=sqlite.connect('Northwind_small.sqlite')
cur=conn.cursor()

# all rows from the Region table
print('Show all rows from the Region table: \n')
cur.execute('SELECT * FROM Region')
for row in cur:
    print(row[0],row[1])
print('-'*20)

# customers
print('How many customers are there? \n')
cur.execute('SELECT * FROM Customer')
print(len(cur.fetchall()))
print('-'*20)

# orders
print('How many orders have been made? \n')
cur.execute('SELECT * FROM [Order]')
print(len(cur.fetchall()))
print('-'*20)

# first five rows from the Product table
print('Show the first five rows from the Product table: \n')
cur.execute('SELECT * FROM Product LIMIT 5')
for row in cur:
    print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
print('-'*20)

# all available categories
print('Show all available categories: \n')
cur.execute('SELECT * FROM Category')
for row in cur:
    print(row[1])
print('-'*20)

# five cheapest products
print('Show the five cheapest products: \n')
cur.execute('SELECT ProductName FROM Product ORDER BY UnitPrice LIMIT 5')
for row in cur:
    print(row[0])
print('-'*20)

# products having more than 100 units in stock
print('Show all products that have more than 100 units in stock: \n')
cur.execute('SELECT ProductName FROM Product WHERE UnitsInStock>100')
for row in cur:
    print(row[0])
print('-'*20)

# columns in the Order table
print('Show all columns in the Order table: \n')
cur.execute('SELECT * FROM [Order]')
for i in cur.description:
    print(i[0])
## column info: for x in cursor.description: print(x)
print('-'*20)
