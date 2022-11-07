# Autohr
#  S M Rasel Mahamud

# def get_taxes(earnings):
#     if earnings < 12000:
#         tax_owed = .25 * earnings
#     else:
#         tax_owed = .35 * earnings
#     return tax_owed

# ana_taxes = get_taxes(9000)
# bob_taxes = get_taxes(15000)

# print(ana_taxes)
# print(bob_taxes)


marks = input("Enter your marks: ")
marks = int(marks)

if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 50:
    grade = "B"
else:
    grade = "F"

print("Your grade is ", grade)