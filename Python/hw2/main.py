from flask import Flask, request
from requirements import requirements
from users import users_addres
from imb import mean
from astro import number_of_astronauts

app = Flask(__name__)


@app.route('/reguirements/')
def read_txt():

    return requirements()


@app.route('/generate-users/')
def generate_users():
    length = int(request.args['length'])
    return users_addres(length)


@app.route('/mean/')
def height_weight():

    return mean()


@app.route('/space/')
def astronauts():

    return str(number_of_astronauts())

if __name__ == '__main__':
    app.run(port=5050)