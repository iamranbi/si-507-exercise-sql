import sqlite3 as sqlite
conn=sqlite.connect('Northwind_small.sqlite')
cur=conn.cursor()

print('\n Searched for')
ask_user1=input('1) ShipCity starts with: ')
ask_user2=input('2) The number of characters in employee first name: ')

try:
    order_start=ask_user1.upper()
    name_num=int(ask_user2)
    if isinstance(order_start,str) and len(ask_user1)==1 and 3<name_num<9:
        st='SELECT x.ShipCity, y.FirstName FROM [Order] AS x JOIN Employee AS y '
        st=st+'On x.EmployeeId=y.Id WHERE x.ShipCity LIKE "'+order_start+'%" AND '
        st=st+'LENGTH(y.FirstName)=='+str(name_num)
        cur.execute(st)
        num_order=len(cur.fetchall())
    else:
        num_order=0
except ValueError:
    num_order=0

print('The number of orders: '+str(num_order)+'\n')
conn.close()
