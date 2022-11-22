# this is list example
courses = ['History', 'Math', 'Science', 'Commerce', 'Arts', 'Language']
print(courses)
# ['History', 'Math', 'Science', 'Commerce']
print(courses[0])
# print first one from the list
# History
print(courses[:2])
# print first two
# ['History', 'Math']

print(courses[2:])
# print start after first two
# ['Science', 'Commerce', 'Arts', 'Language']

print(courses[-2])
# print the 2nd one from the last
# Arts

print(courses[-2:])
# print the last two from the list
# ['Arts', 'Language']

print(courses[0:-2:])
# print all except last two from the list
# ['History', 'Math', 'Science', 'Commerce']

for i in courses[:-2]:
    print(i)
# print all except last two from the list
# History
# Math
# Science
# Commerce

print(courses[1:-2:])
# print all except first one and last two
# ['Math', 'Science', 'Commerce']


# Quick notes 
# List = mutable 
# Remove,pop,insert,append,extend,join,split,max,min,sum,sorted,sort 
# Tuple= immutable 
# Sets= used as membership checker 
# Doesn't allow duplicate data 
# Union, difference, intersection