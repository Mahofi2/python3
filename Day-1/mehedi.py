
num1 = float (input("fast number"))
sign = input("sign")
num2 = float (input("second number "))
if sign == "+":
    print (num1 + num2)
if sign == "-":
    print (num1 - num2)
if sign == "*":
    print (num1 * num2)
if sign == "/":
    print (num1 / num2)
if sign != "+" and sign != "-" and sign != "*" and sign != "/":
    print ("invalid sign")

