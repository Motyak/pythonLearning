import math

def pgcd(a, b):
    a, b = int(a), int(b)   #check if a and b are integers

    while b != 0:
        r = a % b
        a, b = b, r
    return int(a)

def isRepeating(pattern, string):
    nbOfIterations = math.ceil(len(string) / len(pattern))
    print(nbOfIterations)   #debug
    for i in range(1, nbOfIterations + 1):
        substring = string[len(pattern) * (i - 1):len(pattern) * i]
        print(string, pattern, substring)   #debug
        if substring <= pattern:
            if pattern.startswith(substring) == False:
                return False
        elif substring.startswith(pattern) == False:
            return False
    return True

def period(rational):
    rational = float(rational)  #check if its a number

    ent = dec = str(rational)
    ent = ent[:ent.find('.')]
    dec = dec[dec.find('.') + 1:]

    for i in range(len(dec) - 2):
        actualPattern = ''
        for j in range(i, len(dec) - 1):
            actualPattern += str(dec[j])
            # check if pattern is repeating until the end excluding last digit
            if isRepeating(actualPattern, dec[:-1]):
                return actualPattern
            # print(actualPattern)
        

print(period(1/13))
# print(isRepeating('142857', '1428571428571428'))    #True
# print(isRepeating('14285', '1428571428571428'))     #False


# def fm(number):
#     number = float(number)  #check if its a number

#     #if its a whole number, get rid of the decimal part
#     if number.is_integer():
#         return str(int(number))

#     #construct the fraction
#     ent = dec = str(number)
#     ent = ent[:ent.find('.')]
#     dec = dec[dec.find('.') + 1:]
#     a = int(dec) + int(ent) * 10 * len(dec)
#     b = int('1' + len(dec) * '0')

#     #simplification de la fraction
#     gcd = pgcd(a, b)
#     a, b = int(a / gcd), int(b / gcd)

#     frac = '(' + str(a) + '/' + str(b) + ')'
#     if len(frac) < 8 or len(frac) < len(str(number)):
#         return frac
    
#     return str(number)

# def genSpaces(string):
#     string = str(string)

#     if string.isnumeric():
#         return int(string) * ' '
    
#     return len(string) * ' '


# inputText = \
# '''
# [a]ddition
# [s]ubstraction
# [m]ultiplication
# [d]ivision
# >'''

# print('__Simple calculator__')
# userInput=''

# while userInput not in ['a', 's', 'm', 'd']:
#     userInput = input(inputText)[0]

# first = float(input('Enter a first operand : '))
# second = float(input('Enter a second operand : '))

# if userInput == 'a':
#     op = fm(first) + ' + ' + fm(second)
#     res = first + second

# elif userInput == 's':
#     op = fm(first) + ' - ' + fm(second)
#     res = first - second

# elif userInput == 'm':
#     op = fm(first) + ' x ' + fm(second)
#     res = first * second

# elif userInput == 'd':
#     op = fm(first) + ' / ' + fm(second)
#     res = first / second

# print(op, '=', fm(res))
# if(not res.is_integer() and fm(res) != str(res)):
#     print(genSpaces(op), '=', res)