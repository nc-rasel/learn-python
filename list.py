# পাইথন প্রোগ্রামিং - লেকচার ১০ - লিস্ট
# maka a simple list
fruits = ["apple", "banana", "orange", "mango"]
print(type(fruits))
print(fruits)

# how to get 2nd item from a list.
# Note to remember in python indexing start from 0
# so getting second item from list
print(fruits[1])
print(fruits[2])
print(fruits[3])
# to get a first item
print(fruits[0])

print(len(fruits))

# to add new item in to the list
# Note to remember that when we append new item
# its added to th end of the list
fruits.append("papaya")
print(fruits)

print(len(fruits))

# how to know is there any item in the list ex: papaya
print("papaya" in fruits)  # True
print("guava" in fruits)  # False

# how to delete an item from list
# note to remember by pop, last item will be deleted
# from the list
fruits.pop()
print(fruits)

fruits.pop()
print(fruits)
fruits.pop(1)
print(fruits)
