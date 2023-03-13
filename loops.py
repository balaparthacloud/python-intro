names = ["Par","Moh","Sameer","Pramod"]


print(names)
print(names[0])

print("---1")

for name in names:
    print(name)

"""
Loop Dictionaries
"""

person = {
    "age": 25,
    "name": "Partha",
    "work": "home"
}

for key in person:
    print(f"key: {key} value: {person[key]}")

print("---2")
print(person.items())
print(person.keys())
print(person.values())
print("---3")
for key,value in person.items():
    print(f"key: {key} value: {person[key]}")