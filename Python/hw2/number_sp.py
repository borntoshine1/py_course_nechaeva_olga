import requests
def number_of_astronauts():
    r = requests.get('http://api.open-notify.org/astros.json')
    d = r.json()
    return d["number"]

print(number_of_astronauts())