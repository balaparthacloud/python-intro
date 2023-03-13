import calculator

def greet(name):
    print(f"hello : {name}")


greet("Partha")
greet("Sarathy")


def reveal_gender(gender="unknown"):
    if (gender.upper() == "M"):
        return "Male"
    elif (gender.upper() == "F"):
        return "Female"
    else:
        return gender.upper()


print(reveal_gender("m"))
print(reveal_gender("f"))

print("""
---
Cal functions executed, intro to functions
""")

print(calculator.add(1,1))