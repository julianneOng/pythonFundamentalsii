#functions
# - consists of function name, parameters.
# - starts "def" keyword.
# - Optimizes and make a block of code reusable.

# void function
def averageOfTwoThreeNumbers( num1,num2,num3):
    #codes ...
    average = (num1 + num2 + num3) /3
    print("Average: ", average)


averageOfTwoThreeNumbers(89, 76, 81)
averageOfTwoThreeNumbers(89, 76, 81)
averageOfTwoThreeNumbers(89, 76, 81)

# return function
title = "ang alamat ni loudie"
title2 = ": Bagsakan Era"

def stringToTitle(title):
    return title.title()

def stringToUppercase(message):
    return message.upper()

def stringToLowercase(message):
    return message.lower()

def joinSting(message, message2):
    return message.join(message2)

def countLetters(message):
    return len(message)


print(stringToTitle(title))
print(stringToUppercase(title))
print(stringToLowercase(title))
#print(joinSting(title, title2))
print(countLetters(title))
