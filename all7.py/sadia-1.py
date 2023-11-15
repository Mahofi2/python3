print("Hello world !")
"""
# variable
name = "Tasfia tanjim sadia"
age = 21
birthYear = ("27 / 02 / 2002")
fatherName = "Mokbul Hossain"
motherName = "Nargis Begum"
print(name, age, birthYear, fatherName, motherName)
"""
"""
# integer calculator
num1 = int(input("Enter a number"))
sign = input("Enter a sign")
num2 = int(input("Enter an another number"))
if sign == "+":
    print(num1 + num2)
if sign == "-":
    print(num1 - num2)
if sign == "*":
    print(num1 * num2)
if sign == "/":
    print(num1 / num2)
if sign != "+" and sign != "-" and sign != "*" and sign != "/":
    print("something went wrong")
"""
"""
# float calculator.py
number1 = float(input("Enter a first number"))
sign = input("Enter a sign")
number2 = float(input("Enter a second number"))
if sign == "add":
    print(number1 + number2)
elif sign == "sub":
    print(number1 - number2)
elif sign == "mul":
    print(number1 * number2)
elif sign == "div":
    print(number1 / number2)
else:
    print("invalid code")
"""

# leap year
year = int(input("Enter a year"))
if year % 4 == 0:
    print("This is leap year")
if year % 100 == 0:
    print("This is leap year")
if year % 400 == 0:
    print("This is leap year")
if year != 4 % 0 and year != 100 % 0 and year != 400 % 0: # qsn
    print("This is not leap year")

"""
# leap year 2
year = int(input("Enter a year"))
if year % 4 == 0:
    print("yes, leap year")
elif year % 100 == 0:
    print("Yes, leap year")
elif year % 400 == 0:
    print("Yes, leap year")
else:
    print("No, not leap year")
"""
"""
# loop
for i in range(0, 4):
    print("Bangladesh is a river side country")
for i in range(1, 11):
    print("21x", i, "=", 21 * i, "  /  " "22x", i, "=", 22 * i, "  /   " "23x", i, "=", 23 * i, "   /   " "24x", i, "=",
          24 * i, "  /  ""25x", i, "=", 25 * i,
          "  /  " "26x", i, "=", 26 * i, "  /  " "27x", i, "=", 27 * i, "  /  " "28x", i, "=", 28 * i, "  /  " "29x", i,
          "=", 29 * i, "  /  " "30x", i, "=", 30 * i)
"""
"""
# list
greetings = ["Hello","Hi","Hey","Assalamu Alaikum","Welcome","Adab","Anneyo haseyo","Namashkar"]
print(greetings[6])
"""
"""
# grade finding
mark = int(input("Enter your mark "))
if 0 <= mark <= 32:
    print("failed")
if 33 <= mark <= 49:
    print("C")
if 50 <= mark <= 59:
    print("B")
if 60 <= mark <= 69:
    print("A-")
if 70 <= mark <= 79:
    print("A")
if 80 <= mark <= 100:
    print("A+")
if mark > 100:
    print("Error")
"""
"""
# list
saarc = ["Bangladesh", "India", "Pakistan", "Maldive", "Bhutan", "Malaysia"]
print(saarc[2])
countryName = (input("Enter your country name :"))
if countryName in saarc :
    print("Your country is in saarc")
else :
    print("not founded")
"""
"""
# turtle
import turtle
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.exitonclick()
"""

