print("leapyear")
def leapYear():
    if year % 4 == 0:
        return "yes"
    elif year % 100 == 0:
        return "yes"
    elif year % 400 == 0:
        return "yes"
    else:
        return "no"


year = int(input("year type here :"))

result = (leapYear())
print(result)
