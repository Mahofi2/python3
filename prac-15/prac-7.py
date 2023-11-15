"""
print("Hello World")
print("Tasfia Tanjim Sadia")
# int calculator
num1 = int(input("Enter a number"))
sign = input("Enter a sign")
num2 = int(input("Enter an another number"))
if sign == "+":
    print(num1 + num2)
elif sign == "-":
    print(num1 - num2)
elif sign == "*":
    print(num1 * num2)
elif sign == "/":
    print(num1 / num2)
else:
    print("incorrect")
"""
"""
# float calculator
number1 = float(input("Enter a number"))
sign = input("Enter aa sign")
number2 = float(input("Enter a second number"))
if sign == "+":
    print(number1 + number2)
if sign == "-":
    print(number1 - number2)
if sign == "*":
    print(number1 * number2)
if sign == "/":
    print(number1 / number2)
if sign != "+" and sign != "-" and sign != "*" and sign != "/":
    print("something went wrong")
"""
# country = "Bangladesh"
# president = "Sheikh Hasina"
# currency = "Taka"
# print(country)
# print(president)
# print(currency)
"""
# find age problem
age = int(input("Enter your age"))
if age >= 0 or age <= 18:
    print("childhood")
elif age >= 19 or age <= 40:
    print("middel age")
elif age >= 41 or age <= 80:
    print("Man")
elif age >= 81 or age <= 100:
    print("old man")
else:
    print("Error")
"""
# number1 = 10
# number2 = 10
# result = (number1 * number2)
# print(result)
# list
# cousins = ['rima', 'sadia', 'mehedi', 'mahofi', 'diva', 'riyan', 'rifat', 'jamee', 'arafat', 'anita', 'ashfi']
# print(cousins[4])
"""
# find saaarc
saarc = ['Bangladesh', 'India', 'Pakistan', 'Afghanistan', 'Bhutan', 'Maldives', 'Nepal', 'Sri-Lanka']
name = input("Enter your country name :")
if name in saarc:
    print("Your country is in saaarc")
else:
    print("Not founded")
"""

# find result problem
result = int(input("Enter your mark :"))
if 0 <= result <= 32:
    print("Failed")
if 33 <= result <= 39:
    print("D")
if 40 <= result <= 49:
    print("C")
if 50 <= result <= 59:
    print("B")
if 60 <= result <= 69:
    print("A-")
if 70 <= result <= 79:
    print("A")
if 80 <= result <= 90:
    print("A+")
if 91 <= result <= 100:
    print("Golden A+")
if result > 100:
    print("something went wrong")


