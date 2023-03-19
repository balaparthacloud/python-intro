from urllib import request
import requests
import json
import pyttsx3

r = request.urlopen("http://www.google.com")
print(r.getcode())
print(r.read())

"""
Doc : get request
"""
print("--- next request \n\n ")

r = requests.get("http://official-joke-api.appspot.com/jokes/ten")
data = r.text
print(r.status_code)
print(data)
json_load = json.loads(data)
print(json_load)

print(f" total jokes {len(json_load)} \n\n")
for sdata in json_load:
    print(f" setup : {sdata['setup']}")
    print(f" punchline : {sdata['punchline']} \n")
    pyttsx3.speak(sdata['setup'])
    pyttsx3.speak(sdata['punchline'])




