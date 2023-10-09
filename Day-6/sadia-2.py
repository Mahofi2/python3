"""
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
"""
"""
age = int(input("Enter your age"))

if age >= 0 and age <= 10:
    print("childhood")
if age >= 11 and age <= 20:
    print("kids")
if age >= 21 and age <= 40:
    print("Adult")
if age >= 41 and age <= 60:
    print("Middel")
if age >= 61 and age <= 80:
    print("old")
if age >= 81 and age <= 100 :
    print("very old")
else:
    if age > 100 :
        print("error")
"""
# loop

for i in range(1, 11):
    print("11x", i, "=", 11 * i, "  /  ""12x", i, "=", 12 * i, "  /  ""13x", i, "=", 13 * i, "  /  ""14x", i, "=",
          14 * i, "  /  "
                  "15x", i, "=", 15 * i, "  /  ""16x", i, "=", 16 * i, "  /  ", "17x", i, "=", 17 * i, "  /  ""18x", i,
          "=", 18 * i, "  /  "
                       "19x", i, "=", 19 * i, "  /  ""20x", i, "=", 20 * i, )
