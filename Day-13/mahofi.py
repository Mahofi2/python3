"""
 name = "Bangladesh"
 findIndex = name.find("g")
 print(findIndex)
 """
"""
 name = "hello mic test 123 123                       "
 print(name.rstrip())
 father = "         hello mic test 123 123 "
 print(father.lstrip())
 family = "      hello mic test 123 123        "
 print(family.strip())

name = input("Enter your name :")
age = input("enter your age :")
father = input("Enter your Father name :")
print(name.srip())
print(age.strip())
print(father.strip())
"""
"""
def findVowel(x):
    vowel = ['A','E','I','o','u']
    x = x.upper()
    if x in vowel:
        return True
    else:
        return False
userInput = input("Enter a later :")
result = findVowel(userInput)

if result:
    print("the later is vowel")
else:
    print("the later is consonant")
"""
"""
text = "adiyan mahofi"
print(text.upper())

text = "adiyan mahofi"
print(text.lower())
"""
