
def bowelFind(later):
    bowel = ["a", "e", "i", "o", "u"]

    if later in bowel :
        return "its bowel"
    else:
        return "its not bowel"


later = input("type later :")


result = bowelFind(later)
print(result)
