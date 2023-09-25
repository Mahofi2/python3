num1=int(input("fast number"))
sign = input("enter sign")
num2=int(input("seceond number"))
if sign == "+":
    print (num1 + num2)
if sign =="-":
    print(num1 - num2)
if sign =="*":
    print(num1 * num2)
if sign =="/":
    print(num1 / num2)
if sign != "+" and  sign != "-" and  sign != "*" and sign != "/":
    print ("Invalid sign[._.]")
