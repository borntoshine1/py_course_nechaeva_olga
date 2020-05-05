import sqlite3

def first_name():
    conn = sqlite3.connect('./chinook.db')
    cur = conn.cursor()
    cur.execute('''
    SELECT DISTINCT FirstName FROM customers;
    ''')
    results = cur.fetchall()
    conn.close()
    return results