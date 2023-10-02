print ("Leap year")

year = int (input("Enter a year"))

if year % 4 == 0 :
    print ("This is leap year")
if year % 100 == 0 :
    print ("This is leap year")
if year % 400 == 0 :
    print ("This is leap year")
else :
    print ("Normal year")

