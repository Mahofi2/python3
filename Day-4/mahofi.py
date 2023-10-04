year = int(input("finding leap year type here :"))
if year % 4 == 0:
    print("yes its leap year")
elif year % 100 == 0:
    print("yes its leap year")
elif year % 400 == 0:
    print("yes its leap year")
else:
    print(" no is not leap year ")
