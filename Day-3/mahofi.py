mark = int(input("Enter your result  "))
if 0 <= mark <= 32:
    print("Fail")
if mark >= 33 and mark <= 39:
    print("D")
if mark >= 40 and mark <= 49:
    print("C")
if mark >= 50 and mark <= 59:
    print("B")
if mark >= 60 and mark <= 69:
    print("A-")
if mark >= 70 and mark <= 79:
    print("A")
if mark >= 80 and mark <= 100:
    print("A+")
if mark > 100:
    print("type your single subject result")
