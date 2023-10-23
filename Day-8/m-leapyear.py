year = int(input("type year"))
def leapYear():
    if year % 4 == 0:
        print("is that a leap year")
    elif year % 100 == 0:
        print("it is leap year")
    elif year % 400 == 0:
        print("it is leap year")
    else:
        print("sorry")

year()

