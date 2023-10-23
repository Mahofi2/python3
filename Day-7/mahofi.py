terminateprogram = False
while not terminateprogram:
    number1 = int(input("please enter a number :"))
    number2 = int(input("please enter another number :"))

    while True:
        operation = input("please enter add/sub/mul/div and use symbol or quit to exit : ")

        if operation == "quit":
            terminateprogram = True
            break

        if operation not in ["add", "+", "sub", "-", "mul", "*", "div", "/"]:
            print("unknown operation !")
            continue

        if operation == "add" or operation == "+" :
            print("Result is :", number1 + number2)
            break


        if operation == "sub" :
            print("Result is :", number1 - number2)
            break

        if operation == "-":
            print("Result is :", number1 - number2)
            break

        if operation == "mul":
            print("Result is :", number1 * number2)
            break

        if operation == "*":
            print("Result is :", number1 * number2)
            break

        if operation == "div" :
            print("Result is :", number1 / number2)
            break

        if operation == "/":
            print("Result is :", number1 / number2)
            break
