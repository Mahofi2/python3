"""
def markFinding():
    mark = int(input("Enter your mark"))
    if 0 <= mark <= 32:
        return "failed"
    if 32 <= mark <= 39:
        return "D"
    if 40 <= mark <= 49:
        return "C"
    if 50 <= mark <= 59:
        return "B"
    if 60 <= mark <= 69:
        return "A-"
    if 70 <= mark <= 79:
        return "A"
    if 80 <= mark <= 90:
        return "A+"
    if 91 <= mark <= 100:
        return "Golden A+"
    else:
        return "something went wrong"


result = markFinding()
print(result)
"""


def ageFinding():
    age = int(input("Enter your age"))
    if 0 <= age <= 10:
        return "childhood"
    if 11 <= age <= 20:
        return "Teenager"
    if 21 <= age <= 40:
        return "Adulthood"
    if 41 <= age <= 60:
        return "men"
    if 61 <= age <= 80:
        return "old"
    else:
        return "Death"


ageCounting = ageFinding()
print(ageCounting)
