"""
# borgo
list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
listNumber = []
for i in list:
    listNumber.append(i * i)

print(listNumber)
"""
"""
# tuple
numbers = (2, 3, 4, 5,)
n1, n2, n3, n4 = numbers
print(n3)
"""
# set
a = {1, 2, 3, 9, 5}
b = {6, 2, 3, 9, 10}
# interSection = a ^ b
interSection = a & b
print(interSection)
# union = a | b
