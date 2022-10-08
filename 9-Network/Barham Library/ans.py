import requests
import json


def process(book):
    nam = book["name"]
    cat = book["category"]
    if cat == 'math':
        response = requests.get('http://127.0.0.1:8000/math/').json()
        for res in response:
            for k, v in res.items():
                if v == nam:
                    return 'bad query'
        requests.post('http://127.0.0.1:8000/math/', data = book)
    if cat == 'physic':
        response = requests.get('http://127.0.0.1:8000/physic/').json()
        for res in response:
            for k, v in res.items():
                if v == nam:
                    return 'bad query'
        requests.post('http://127.0.0.1:8000/physic/', data = book)
    if cat == 'chess':
        response = requests.get('http://127.0.0.1:8000/chess/').json()
        for res in response:
            for k, v in res.items():
                if v == nam:
                    return 'bad query'
        requests.post('http://127.0.0.1:8000/chess/', data = book)