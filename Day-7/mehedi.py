terminateprogram = False
while not terminateprogram:
    number1 = int(input("please enter a number :"))
    number2 = int(input("please enter another number :"))

    while True:
        operation = input("please enter add/sub/mul/div : ")

        if operation == "quit":
            terminateprogram = True
            break

        if operation not in ["add", "sub", "mul", "div"]:
           print("unknown operation !")
           continue

        if operation == "sub":
           print("Result is :", number1 - number2)
           break

        if operation == "add":
           print("Result is :", number1 + number2)
           break

        if operation == "mul":
           print("Result is :", number1 * number2)
           break

        if operation == "div":
           print("Result is :", number1 / number2)
           break
