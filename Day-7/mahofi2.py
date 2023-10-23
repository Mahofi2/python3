def add():
    num1 = int(input("enter a num"))
    num2 = int(input("enter a num"))
    return num1 + num2


def sub():
    num1 = int(input("enter a num"))
    num2 = int(input("enter a num"))
    return num1 - num2


def mul():
    num1 = int(input("enter a num"))
    num2 = int(input("enter a num"))
    return num1 * num2


def div():
    num1 = int(input("enter a num"))
    num2 = int(input("enter a num"))
    return num1 / num2


print("+ for 1/ - for 2 / * for 3/ / for 4")

i = int(input("sign"))
if i == 1:
    print(add())
elif i == 2:
    print(sub())
elif i == 3:
    print(mul())
elif i == 4:
    print(div())
else:
    print("wrong sign")
