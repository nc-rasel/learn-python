# পাইথন প্রোগ্রামিং - লেকচার ১৩ - for লুপ
# basic list
fruits = ["apple", "mango", "banana", "orange"]

# print all the list items using for loop
for fruit in fruits:
    print(fruit)

for i in range(4):
    print(i, fruits[i])

for i in range(3, 10):
    print(i)

for i in range(3, 10, 2):
    print(i)



# Genrate a multipication table using function and loop

def generate_multipication_table(n):
    print(n, "x 1 =", n * 1)
    print(n, "x 2 =", n * 2)
    print(n, "x 3 =", n * 3)
    print(n, "x 4 =", n * 4)
    print(n, "x 5 =", n * 5)
    print(n, "x 6 =", n * 6)
    print(n, "x 7 =", n * 7)
    print(n, "x 8 =", n * 8)
    print(n, "x 9 =", n * 9)
    print(n, "x 10 =", n * 10)
    # return None

n = input("Enter numer: ")
n = int(n)

for i in range(1, n+1):
    generate_multipication_table(i)
    print("")





