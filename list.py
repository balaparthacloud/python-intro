"""
This is doc on python list
"""

numbers = [1,2,3,4,5]
numbers.append(1000)
print(len(numbers))
print (2 in numbers)
print (1001 in numbers)
print(numbers[0])
print(numbers.remove(1))
print(numbers.pop())
print(numbers.pop())
print(numbers)
del numbers[0:7]
print(numbers)

#----Example 2

numbers = [1,2,3,4,5,6,7,8,9]
numberList = [1,2]
numberSet = {1,1}
print(numberList)
print(numberSet)