num1 = float(input("fast number"))
sign = input("enter sign")
num2 = float(input("sec number"))
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
