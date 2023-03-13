numbers = [5,5,5,1,10]
total = 0

for num in numbers:
    total += num

print(total)

#--- while loop

number = 0
while number < 10:
    print(number)
    number += 1
else:
    print("while loop ended")

#--- break and continue
print(""" on  continue statements""")
for n in [1,2,3,4,5,6,7,8,9,10]:
    if(n > 5):
        continue
    print(n)

print(""" on break  statements""")
for n in [1,2,3,4,5,6,7,8,9,10]:
    if(n == 5):
        break
    print(n)