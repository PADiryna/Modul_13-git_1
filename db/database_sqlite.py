import sqlite3
import datetime

with sqlite3.connect('db/file.db') as db:
    cursor = db.cursor()
    # query = '''CREATE TABLE IF NOT EXISTS expenses(id INTEGER, name text)'''
    # cursor.execute(query)
    query1 ="""INSERT INTO expenses(id, name) VALUES (1, 'payment for training')"""
    query2 ="""INSERT INTO expenses(id, name) VALUES (2, 'payment for school')"""
    query3 ="""INSERT INTO expenses(id, name) VALUES (3, 'payment for English courses')"""
    query4 ="""INSERT INTO expenses(id, name) VALUES (4, 'rent payment')"""
    query5 ="""INSERT INTO expenses(id, name) VALUES (5, 'payment for transport')"""
    # cursor.execute(query1)
    # cursor.execute(query2)
    # cursor.execute(query3)
    # cursor.execute(query4)
    # cursor.execute(query5)
    db.commit()

def get_timestamp(y,m,d):
    return datetime.datetime.timestamp(datetime.datetime(y,m,d))

def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()

# insert_payments = [
#     (1, 275, get_timestamp(2023, 3, 5), 1),
#     (2, 100, get_timestamp(2023, 2, 25), 2),
#     (3, 200, get_timestamp(2023, 3, 1), 3),
#     (4, 2400, get_timestamp(2023, 3, 1), 4),
#     (5, 50, get_timestamp(2023, 3, 1), 5),
#     (6, 50, get_timestamp(2023, 3, 8), 5),
#     (7, 50, get_timestamp(2023, 3, 17), 5),
#     (8, 50, get_timestamp(2023, 3, 25), 5)
# ]

with sqlite3.connect('db/file.db') as db:
    cursor = db.cursor()
    query = '''SELECT amount, payment_date, name FROM payments JOIN expenses 
               ON expenses.id = payments.expense_id WHERE expense_id = 5'''

    cursor.execute(query)
    sum = 0
    for result in cursor:
        sum += result[0]
        print(result[0], get_date(result[1]), (result[2]))
    print('TOTAL:', sum)    


    # query = """ INSERT INTO payments(id, amount, payment_date, expense_id)
    #                             VALUES(?,?,?,?);"""   
    

    # query =""" CREATE TABLE IF NOT EXISTS payments(
    #     id INTEGER,
    #     amount REAL,
    #     payment_date INTEGER,
    #     expense_id INTEGER
    # )"""


    # cursor.executemany(query, insert_payments)
    db.commit()


    
    












