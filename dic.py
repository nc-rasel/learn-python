# empty dict
# student = dict() .  

student = {'Name': 'Rasel', 'city': 'Dhaka'}

# Accessing Items from Dictionary
print(student['Name'])
# Adding new values
student['country'] = 'Bangladesh'
print(student)

# Updating values:
student['city'] = 'Bhola'
print(student)
if 'city' in student:
    print('Found')
else:
    print('Not found')