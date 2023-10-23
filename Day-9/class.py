
num = float(input("Enter a number"))
sign = input("Enter a sign")
num2 = float(input("Enter an another number"))

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


def calculator(num, num2, sign):
    if sign == "+":
        return add(num, num2)
    elif sign == "-":
        return sub(num, num2)
    elif sign == "*":
        return mul(num, num2)
    elif sign == "/":
        return div(num, num2)
    else:
        return "Error"



result = calculator(num, num2, sign)
print(result)
