import sqlite3

def tracks():
    conn = sqlite3.connect('./chinook.db')
    cur = conn.cursor()
    cur.execute('''
    SELECT COUNT(*) FROM tracks;
    ''')
    results = cur.fetchall()
    conn.close()
    return str(results[0][0])