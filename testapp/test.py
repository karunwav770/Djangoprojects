import requests

# def f1(id):
#     BASE_URL='http://127.0.0.1:8000/'
#     END_URL='cbv3/'
#     resp=requests.get(BASE_URL+END_URL+str(id))
#     print(resp.status_code)
#     print(resp.json())
import json


def f2():
    BASE_URL='http://127.0.0.1:8000/'
    END_URL='cbv3/'
    emp_data={
        'name':'kaaja',
        'role':'BA',
        'project':'claims',
        'email':'kaaja@gmail.com',
        'location':'BNGL'
    }
    resp=requests.post(BASE_URL+END_URL,data=json.dumps(emp_data))
    print(resp.status_code)
    print(resp.json())
   
def f3(id=None):
    BASE_URL='http://127.0.0.1:8000/'
    END_URL='apiview/'
    emp_data={
    "id":23,
    "name": "rodam",
    "role": "BA",
    "project": "claims",
    "email": "rodam@gmail.com",
    "location": "Us"
    }
    resp=requests.put(BASE_URL+END_URL,data=json.dumps(emp_data))
    print(resp.status_code)
    print(resp.json())
f3()