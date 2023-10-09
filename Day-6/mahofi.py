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

        if operation == "add" and operation == "+":
            print("Result is :", number1 + number2)
            break

        if operation == "sub" and operation == "-":
            print("Result is :", number1 - number2)
            break
        if operation == "mul" and operation == "*":
            print("Result is :", number1 * number2)
            break
        if operation == "div" and operation == "/":
            print("Result is :", number1 / number2)
            break
