import requests

endpoint ="http://localhost:8000/api" #testing local host


get_response = requests.get(endpoint, params={"abc": 123},json={"query": "Helo world"}) #http request

#print(get_response.headers) #raw data
#print(get_response.text) #raw data
#print(get_response.status_code)

#javascript Objectt Notation : 
print(get_response.json())

