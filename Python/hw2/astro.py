import requests

def number_of_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')

    return r.json()["number"]
