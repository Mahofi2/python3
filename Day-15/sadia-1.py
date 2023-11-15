digitOneMapping = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}
digitTwoMapping = {
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
}
digitThreeMapping = {
    '10': 'ten',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
}
digitFourMapping = {
    '100': 'one hundred'
}

userInput = input("Enter a number(1 to 100) :")


def digitCount(data):
    return len(data)

totalDigit =digitCount(userInput)

if totalDigit == 1:
    print(digitOneMapping.get(userInput))
elif totalDigit == 2:
    print(digitTwoMapping.get(userInput) or digitThreeMapping.get(userInput))
