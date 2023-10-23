# """
# import turtle
#
#
# def drawsquare(sidelengh):
#     for i in range(4):
#         turtle.forward(sidelengh)
#         turtle.left(90)
#
#
# counter = 0
# while counter < 90:
#     drawsquare(150)
#     turtle.right(4)
#     counter += 1
# turtle.exitonclick()
# """
#
#
# def calculator():
#
#
#     num1 = int(input("Enter a number"))
#     sign = input("Enter a sign")
#     num2 = int(input("Enter an another number"))
#     if sign == "+":
#         return (num1 + num2)
#     if sign == "-":
#         return (num1 - num2)
#     if sign == "*":
#         return (num1 * num2)
#     if sign == "/":
#         return (num1 / num2)
#     if sign != "+" and sign != "-" and sign != "*" and sign != "/":
#         return ("something went wrong")
# leap year
# year = int(input("Enter a year"))
# if year % 4 == 0:
#     print("This is leap year")
# if year % 100 == 0:
#     print("This is leap year")
# if year % 400 == 0:
#     print("This is leap year")
# if year % 4 != 0 and year % 100 != 0 and year % 400 != 0:
#     print("This is not leap year")



def vowelFind(userInput):
    vowel = ["a", "e", "i", "o", "u"]
    if userInput in vowel :
        return "its vowel"
    else:
        return "consonant"


userInput = input(" type a later :")

result = vowelFind(userInput)
print(result)
