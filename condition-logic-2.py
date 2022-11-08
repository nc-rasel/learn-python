# পাইথন প্রোগ্রামিং - লেকচার ৬ - কন্ডিশনাল লজিক ২
# Basic and simple GPA Calculator using if elif else condition
#
#
marks = input("Enter your marks: ")
marks = int(marks)

if marks >= 80:
    print("GPA: A")
elif marks >= 70:
    print("GPA: B")
elif marks >= 60:
    print("GPA: C")
elif marks >= 50:
    print("GPA: D")
else:
    print("GPA: F")

print("Done")
