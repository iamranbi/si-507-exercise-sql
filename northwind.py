import sqlite3 as sqlite
from datetime import datetime
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
print('-'*20)

# employee's first name and the number of order each employee has made (sort by the total number of orders)
print('Identify first name and number of order has made of each employee: \n')
st1='SELECT Employee.FirstName, COUNT(*) FROM Employee JOIN [Order] '
st1+='ON Employee.Id=[Order].EmployeeId GROUP BY FirstName ORDER BY COUNT(*) DESC'
cur.execute(st1)
for row in cur:
    print(row[0]+', '+str(row[1]))
print('-'*20)

# products and the corresponding supply companies in Ann Arbor
print('Identify the products and the corresponding supply companies in Ann Arbor: \n')
st2='SELECT Product.ProductName, Supplier.CompanyName FROM Product JOIN Supplier '
st2+='ON Product.SupplierId=Supplier.Id WHERE Supplier.City=="Ann Arbor"'
cur.execute(st2)
for row in cur:
    print(row[0]+', '+str(row[1]))
print('-'*20)

# number of days passed between orders for each customer(self join)
date_format = "%Y-%m-%d"
st3='SELECT x.CustomerId, y.OrderDate AS OrderDate, x.OrderDate AS PreviousOrderDate '
st3=st3+'FROM [Order] AS x JOIN [Order] AS y On x.CustomerId=y.CustomerId '
st3=st3+'WHERE y.OrderDate>x.OrderDate GROUP BY x.CustomerId, y.OrderDate'
cur.execute(st3)

print('Customer ID, Order Date, Previous Order Date, Days Passed')
for row in cur:
    da=datetime.strptime(row[1],date_format)-datetime.strptime(row[2],date_format)
    print(row[0]+', '+row[1]+', '+row[2]+', '+str(da.days))
