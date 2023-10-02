num1 = int(input("enter a number"))
sign = input("enter a sign")
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
