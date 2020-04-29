import sqlite3
#from flask import Flask, request, Response

def f_customers(query):
    try:
        conn = sqlite3.connect('./chinook.db')
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        conn.close()
        return results
    except Exception:
        return None
    finally:
        conn.close()


def filter_and(query_param):
    result = []
    for elem in query_param.split(';'):
        operands = elem.split(':')
        result.append(f"{operands[0].capitalize()} = '{operands[1]}'")

    return ' AND '.join(result)
    


if __name__ == '__main__':
    assert filter_and('country:USA') == "Country = 'USA'"
    assert filter_and('country:USA;city:Boston') == "Country = 'USA' AND City = 'Boston'"