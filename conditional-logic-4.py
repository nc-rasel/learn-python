# পাইথন প্রোগ্রামিং - লেকচার ৮ - কন্ডিশনাল লজিক ৪
# Find Odd and Even number using conditional logic
# Find positive and negative number
# using nested if else
# Need to check truth table for A and B , A or B, Not A

n = input("Enter number: ")
n = int(n)

if n >= 0 and n % 2 == 0:
    print(n, "is positive and even number")
elif n >= 0 and n % 2 == 1:
    print(n, "is positve and odd number")
elif n < 0 and n % 2 == 0:
    print(n, "is negative and even number")
else:
    print(n, "is negative and odd number")


""""
if n >= 0:
    if n % 2 == 0:
        print(n, "positive and even number")
    else:
        print(n, "is positive and odd number")
else:
    if n % 2 == 0:
        print(n, "is negative and even number")
    else:
        print(n, "is negative and odd number")
"""

"""
if n % 2 == 0:
    print(n, "Even number")
else:
    print(n, "Odd number")
"""
