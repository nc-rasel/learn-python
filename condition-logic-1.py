# পাইথন প্রোগ্রামিং - লেকচার ৫ - কন্ডিশনাল লজিক ১

nearly_pi = 3.141592653589793238462643383279502884197169399375105820974944
print(nearly_pi)
print(type(nearly_pi))

almost_pi = 22/7
print(almost_pi)
print(type(almost_pi))

# this is how you can get input from users
marks = input("enter your marks: ")
# we need to convert string to int
marks = int(marks)

if marks >= 40:
    print("pass")
else:
    print("fail")