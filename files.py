"""
w - write
r - read
r+ - read and write
a - append
"""
file = open("com/files/data.csv", "r+")
file.write("id,name,email\n")
file.write("1,partha,par@gmail.com\n")
file.write("2,sam,sam@gmail.com\n")
file.write("3,moh,moh@gmail.com\n")
file.write("4,ria,ria@gmail.com\n")
file.close()


"""
Now Reading File
"""

file = open("com/files/data.csv", "r")
#print(file.readlines())
#print(file.read())
for line in file:
    print(line)
file.close()
