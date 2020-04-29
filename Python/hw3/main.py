import sqlite3
from flask import Flask, request, Response
from firstname import first_name
from number_of_tracks import tracks
from tracks_sec import tracks_sec
from filter_customers import filter_and, f_customers

app = Flask(__name__)

@app.route('/names/')
def customers():
    return str(first_name())


@app.route('/tracks/')
def number_of_tracks():
    return str(tracks())


@app.route('/tracks_sec/')
def tracks_seconds():
    return str(tracks_sec())


@app.route('/customers/')
def customers_filter():
    query = ''' 
        SELECT * FROM customers;
    '''

    country = request.args.get('country')
    if country:
        query = f'''
            SELECT * FROM customers WHERE Country = '{country}';
        '''

    param = request.args.get('filter')
    if param:
        query = f'''
        SELECT * FROM customers WHERE {filter_and(param)};
        '''

    return str(f_customers(query))
    

if __name__ == '__main__':
    app.run(port=5050, debug=True)
