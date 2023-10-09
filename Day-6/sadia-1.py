# 1 = 1 + 1

terminateprogram = False
while not terminateprogram:
    number1 = int(input("please enter a number :"))
    number2 = int(input("please enter another number :"))

    while True:
        operation = input("please enter add/sub or quit to exit : ")

    if operation == \
            quit:
        terminateprogram = True
        break

    if operation not in ["add", "sub"]:
        print("unknown operation !")
        continue

    if operation == "add":
        print("Result is :", number1 + number2)
        break

    if operation == "sub":
        print("Result is :", number1 - number2)
        break
