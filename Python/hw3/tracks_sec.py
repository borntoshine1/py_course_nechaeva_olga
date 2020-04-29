import sqlite3

def tracks_sec():
    conn = sqlite3.connect('./chinook.db')
    cur = conn.cursor()
    cur.execute('''
    SELECT Name, Milliseconds * 0.001 FROM tracks;
    ''')
    results = cur.fetchall()
    conn.close()
    return results