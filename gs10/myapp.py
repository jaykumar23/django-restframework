import json
import requests

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    headers = {
        'content-Type': 'application/json'
    }
    if id is not None:
        data = {'id': id}
    js = json.dumps(data) 
    r = requests.get(url=URL,headers=headers, data=js)
    data = r.json()
    print(data)

# get_data()

# create data
def post_data():
    data = {
        'name': 'Andy',
        'roll': 1,
        'city': 'Mumbai'
    }
    headers = {
        'content-Type': 'application/json'
    }
    js = json.dumps(data) 
    r = requests.post(url=URL,headers=headers, data=js)
    data = r.json()
    print(data)
# post_data()


# data update
def update_data():
    data = {
        'id': 3,
        'name': 'Aandy',
        'roll': 1,
        'city': 'Mumbai'
    }
    headers = {
        'content-Type': 'application/json'
    }
    js = json.dumps(data) 
    r = requests.put(url=URL,headers=headers, data=js)
    data = r.json()
    print(data)

# update_data()


# data delete
def delete_data():
    data = {
        'id': 3,
    }
    headers = {
        'content-Type': 'application/json'
    }
    js = json.dumps(data) 
    r = requests.delete(url=URL,headers=headers, data=js)
    data = r.json()
    print(data)

delete_data()