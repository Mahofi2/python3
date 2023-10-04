year = int(input("finding leap year type here :"))

if year % 4 == 0:
    print("yes its leap year ")

else:
    if year % 100 == 0:
        if year % 400 == 0:
            print("yes its leap year")
        else:
            print(" no is not leap year ")
    else:
        print(" no is not leap year ")

