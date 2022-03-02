import json
import requests

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    js = json.dumps(data) 
    r = requests.get(url=URL, data=js)
    data = r.json()
    print(data)

# get_data(1)

# create data
def post_data():
    data = {
        'name': 'Andy',
        'roll': 1,
        'city': 'Mumbai'
    }
    js = json.dumps(data) 
    r = requests.post(url=URL, data=js)
    data = r.json()
    print(data)
# post_data()


# data update
def update_data():
    data = {
        'id': 3,
        'name': 'Andy',
        'roll': 1,
        'city': 'Mumbai'
    }
    js = json.dumps(data) 
    r = requests.put(url=URL, data=js)
    data = r.json()
    print(data)

# update_data()


# data delete
def delete_data():
    data = {
        'id': 3,
    }
    js = json.dumps(data) 
    r = requests.delete(url=URL, data=js)
    data = r.json()

delete_data()