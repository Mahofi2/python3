"""
# int calculator
def intzerCalculator():
    number1 = int(input("Enter a number :"))
    sign = input("Enter a sign :")
    number2 = int(input("Enter an another number : "))
    if sign == "+":
        return number1 + number2
    if sign == "-":
        return number1 - number2
    if sign == "*":
        return number1 * number2
    if sign == "/":
        return number1 / number2
    else :
        return "something went wrong"


result = intzerCalculator()
print(result)
"""

"""
# loop
def serial():
    for i in (1, 11):
        return "2x" + str(i) + "=" + str(2 * i)


result = serial()
print(result)
"""


# loop
def serial():
    for i in (1, 11):
        return ("2x", i, "=", 2 * i)


result = serial()
print(result)
