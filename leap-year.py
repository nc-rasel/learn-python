# পাইথন প্রোগ্রামিং - লেকচার ৯ - লিপ ইয়ার
# Find out which year is leap year using condition and nested if


year = input("Enter year: ")
year = int(year)

# example one with a little glitch
# if year % 4 == 0:
#     print(year, "is leap year")
# else:
#     print(year, "is not leap year")


# if any year divisible by 100 then it should also divisible by 400 too
# example 2
"""
if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print(year, "is leap year")
    elif year % 100 != 0:
        print(year, "is leap year")
    else:
        print(year, "is not leap year")
else:
    print(year, "is not leap year")
"""
# Example 3
"""
if year % 4 != 0:
    print(year, "is not leap year")
elif year % 100 != 0:
    print(year, "is leap year")
elif year % 400 != 0:
    print(year, "is not leap year")
else:
    print(year, "is leap year")
"""
# example 4
if year % 400 == 0:
    print(year, "is leap year")
elif year % 100 == 0 or year % 4 != 0:
    print(year, "is not leap year")
else:
    print(year, "is leap year")
