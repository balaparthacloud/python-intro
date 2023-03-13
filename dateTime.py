import datetime


print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.datetime.now().time())
print(datetime.datetime.now().date())
print(datetime.datetime.now().year)
print(datetime.datetime.now().day)

print(datetime.datetime.now().strftime("%d-%m-%Y"))
print(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
print(datetime.datetime.now().strftime("%d-%B-%Y %H:%M:%S"))
print(datetime.datetime.now().strftime("%d-%b-%Y %H:%M:%S"))