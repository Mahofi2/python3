import random

number = random.randint(1, 100)
attempts = 0
while True:
    userGuess = int(input('Guess the number (between 1 and 100):'))
    attempts += 1
    if userGuess == number:
        print('Yes, your guess is correct!')
        break
    if userGuess > number:
        print('Incorrect! please try to guess a smaller number.')
    else:
        print('Incorrect! please try to guess a larger number.')


print("Tou tried", attempts, "times to find the correct number.")


print("let's play lv.2")

number = random.randint(1, 1000)

attempts = 0

while True:
    userGuess = int(input('Guess the number (between 1 and 1000):'))
    attempts += 1
    if userGuess == number:
        print('Yes, your guess is correct!')
        break
    if userGuess > number:
        print('Incorrect! please try to guess a smaller number.')
    else:
        print('Incorrect! please try to guess a larger number.')


print("Tou tried", attempts, "times to find the correct number.")

print("***your great***")
