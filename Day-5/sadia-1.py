"""
math = (200 + 300) * 12
print(math)
a = 500 * 12
print(a)
b = (200 + 300 - 250) * 12
print(b)
print(5 + 30 + 20)
print(5 + 30 - 20)
print(5 + 30 * 20)
print((5 + 30) * 20)
print(((5 + 30) * 20 / 10))
print(5 + 30 * 20 / 10)
"""
"""
# intezer calculator

num1 = int(input("enter a number"))
sign = (input("enter a sign"))
num2 = int(input("enter an another number"))

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
# floting calculator

num1 = float(input("enter first number"))
sign = (input("enter a sign"))
num2 = float(input("enter second number"))

if sign == "+" :
    print (num1 + num2)
if sign == "-" :
     print (num1 - num2)
if sign == "*" :
     print (num1 * num2)
if sign == "/" :
    print (num1 / num2)
if sign != "+" and sign != "-" and sign != "*" and sign != "/" :
    print ("incorrect")
    """
# age challenge
year = int(input("enter a age"))

if year >= 0 and year <= 18:
    print("childhood")
elif year >= 19 and year <= 30:
    print("Adult")
elif year >= 31 and year <= 60:
    print("Mid age")
elif year >= 61 and year <= 100:
    print("old")
else:
    if year > 100 :
        print("error")
