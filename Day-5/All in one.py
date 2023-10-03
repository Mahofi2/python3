# variables
a = 20
b = 30
print(a + b)

# data type
#  int
# float
# list
# string "['_']"

# condition
age = int (input("how old are you"))


if (age >= 18):
    print("adult")
else:
    print("Minor")
# scan
input ()

# calculator
num1 = float(input("fast number")) # use int
sign = input("enter sign")
num2 = float(input("sec number")) # use int
if sign == "+":
    print(num1 + num2)
if sign == "-":
    print(num1 - num2)
if sign == "*":
    print(num1 * num2)
if sign == "/":
    print(num1 / num2)
if sign != "+" and sign != "-" and sign != "*" and sign != "/":
    print("Invalid sign[._.]")
# comment
"""
multiline comment
"""
# list
work = ["hello","hi","whats up","good bye"]
print(work[1])
# grade find
mark = int(input("enter your result"))

if 0 <= mark <= 32:
    print("failed")
if 33 <= mark <= 39:
    print("Grade point D ")
if 40 <= mark <= 49:
    print("Grade point C")
if 50 <= mark <= 59:
    print("Grade point B")
if 60 <= mark <= 69:
    print("Grade point A- ")
if 70 <= mark <= 79:
    print("Grade point A ")
if 80 <= mark <= 90:
    print("Grade point A+ ")
if 91 <= mark <= 100:
    print("Golden A+ ")
if mark < 100:
    print("type your single subject result")

# leap finding

year = int(input("finding leap year type here :"))
if year % 4 == 0:
    print("yes its leap year")
elif year % 100 == 0:
    print("yes its leap year")
elif year % 400 == 0:
    print("yes its leap year")
else:
    print(" no is not leap year ")

# leap year different

year = int(input("finding leap year type here :"))

if year % 4 == 0:
    print("yes its leap year ")

else:
    if year % 100 == 0:
        if year % 400 == 0:
            print("yes its leap year")
        else:
            print(" no is not leap year ")
    else:
        print(" no is not leap year ")
# make 1 to 10 namta H.W
# use turtle make some think H.W




