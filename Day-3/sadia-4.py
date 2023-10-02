mark = int(input("enter your result"))

if 0 <= mark <= 32:
    print("failed")
if 33 <= mark <= 39:
    print("Grade point D ")
if 40 <= mark <= 49:
    print("Grade point C")
if 50 <= mark <= 59:
    print("Grade point B")
if 60 <= mark <= 69:
    print("Grade point A- ")
if 70 <= mark <= 79:
    print("Grade point A ")
if 80 <= mark <= 90:
    print("Grade point A+ ")
if 91 <= mark <= 100:
    print("Golden A+ ")
if mark < 100:
    print("type your single subject result")
