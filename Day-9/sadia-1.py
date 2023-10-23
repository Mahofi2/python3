
# integer calculator
num1 = int(input("Enter a number"))
sign = input("Enter a sign")
num2 = int(input("Enter an another number"))


def Calculator(num1, num2, sign):
    if sign == "+":
        return num1 + num2
    elif sign == "-":
        return num1 - num2
    elif sign == "*":
        return num1 * num2
    elif sign == "/":
        return num1 / num2
    else:
        return "something went wrong"


result = Calculator(num1, num2, sign)
print(result)


# float calculator
number1 = float(input("Enter a first number"))
sign = input("Enter a sign")
number2 = float(input("Enter a second number"))


def count(number1, sign, number2):
    if sign == "add" or sign == "+":
        return number1 + number2
    if sign == "sub" or sign == "-":
        return number1 - number2
    if sign == "mul" or sign == "*":
        return number1 * number2
    if sign == "div" or sign == "/":
        return number1 / number2
    if sign != "add" or "+" and sign != "sub" or "-" and sign != "mul" or "*" and sign != "div" or "/":
        return "Incorrect Calculation"


result = count(number1, sign, number2)
print(result)


# leap year
year = int(input("Enter a year"))


def leapyear():
    if year % 4 == 0:
        return "This is leap year"
    if year % 100 == 0:
        return "This is leap year"
    if year % 400 == 0:
        return "This is leap year"
    else:
        return "This is not leap year"


cheak = leapyear()
print(cheak)


# list
user = input("Enter a district of Bangladesh")  # string data type
list = ["Dhaka", "Camilla", "Rajshahi", "Mymensigh", "Sylhet", "Barishal"]


def districtOfBangladesh():
    if districtOfBangladesh in list:
        return "in Bangladesh"
    else:
        return "Not in Bangladesh"

find = districtOfBangladesh()
print(find)


# list
capital = ["Dhaka", "Lahore", "Delhi", "Seoul", "Kualalampur"]
user = input("Enter a capital name")


def mainland():
    if user in capital:
        return "capital is in country"
    else:
        return "capital is not found"


country = mainland()
print(country)



# vowel
user = input("Enter a English letter")
vowel = ["a", "e", "i", "o", "u"]


def letter():
    if user in vowel:
        return "it's in vowel"
    else:
        return "consonant"


word = letter()
print(word)

