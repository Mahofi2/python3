"""
# guessing game
import random
numbers = random.randint(1, 500)
attempts = 0
while True:
    userInput = int(input("please, guess the numbers between 1 to 500 :"))
    attempts += 1
    if userInput == numbers:
        print('Congratulations ! Your guess is correct')
        break
    if userInput > numbers :
        print('Incorrect ! please try to guess a smaller number')
    if userInput < numbers :
        print('wrong ! please try to guess a larger numbers')


print("You tried,", attempts, "times to guess the corrct number")
"""
"""
# guessing colours
import random
colours = ['red', 'Green', 'Black', 'White', 'Blue']
colours = random.randint(colours)
attempts = 0
while True:
    userInput = input('please, guess the colours :')
    attempts += 1
    if userInput == colours:
        print("Congratulation ! Your guess is correct")
        break
    else:
        print("Incorrect")

print("You tired,", attempts, "times to guess the colours")
"""
userInput = int(input("Enter a number"))
primeNumbers = []

for i in range(userInput):
    if i % 2 != 0:
        primeNumbers.append(i)


print(primeNumbers)
