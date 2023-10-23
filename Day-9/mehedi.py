num1 = float(input(" inter fast number"))
sign = input("inter sign")
num2 = float(input(" inter 2d number"))


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mal(x, y):
    return x * y


def div(x, y):
    return x / y


def calculator(num1, sign, num2):
    if sign == "+":
        return add(num1, num2)
    elif sign == "-":
        return sub(num1, num2)
    elif sign == "*":
        return mal(num1, num2)
    elif sign == "/":
        return div(num1, num2)
    else:
        "error"


result = calculator(num1, sign, num2)
print(result)
