terminateProgram = False
while not terminateProgram:
    number1 = int(input("Enter a number"))
    number2 = int(input("Enter an another number"))

    while True:
        operation = input("please enter add / sub / mul / div and use symbol or quit to exit: ")

        if operation not in ["add", "sub", "mul", "div"]:
            print("Unknown operation !")
            continue

        if operation == "quit":
            terminateProgram = True
            break

        if operation == "add":
            print("result is :", number1 + number2)
            break

        if operation == "sub":
            print("result is :", number1 - number2)
            break

        if operation == "mul":
            print("result is :", number1 * number2)
            break

        if operation == "div":
            print("result is :", number1 / number2)
            break
