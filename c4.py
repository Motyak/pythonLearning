import math #ceil for nb of iterations in isRepeating(..)
import re   #fractions in input

def pgcd(a, b):
    a, b = int(a), int(b)   #check if a and b are integers

    while b != 0:
        r = a % b
        a, b = b, r
    return int(a)

# check if a pattern is periodic within a string (startswith instead of equality)
def isRepeating(pattern, string):
    nbOfIterations = math.ceil(len(string) / len(pattern))
    if nbOfIterations == 1:
        return False
    for i in range(1, nbOfIterations + 1):
        substring = string[len(pattern) * (i - 1):len(pattern) * i]
        # print(string, pattern, substring)   #debug
        if substring <= pattern:
            if pattern.startswith(substring) == False:
                return False
        elif substring.startswith(pattern) == False:
            return False
    return True

# return a tuple with the fixed decimal part and the periodic decimal part
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
            if isRepeating(actualPattern, dec[i:-1]):
                return (dec[:dec.find(actualPattern)], actualPattern)
    return (dec, '0')

# Format a number to print it the correct way
def fm(number, decimalForm=False):
    number = float(number)  #check if its a number

    #if its a whole number, get rid of the decimal part
    if number.is_integer():
        return str(int(number))

    #get integral and decimal part
    ent = dec = str(number)
    ent = ent[:ent.find('.')]
    dec = dec[dec.find('.') + 1:]

    # we consider its a non-decimal if it has at least 10 digits
    if(len(str(dec)) >= 10):
        decParts = period(number)  #0 -> fixed, 1 -> periodic part

        if decimalForm:
            return ent + '.' + decParts[0] + '[' + decParts[1] + ']..'

        a = int(decParts[1])
        b = int(len(decParts[1]) * '9') * 10 ** len(decParts[0])
        if decParts[0] != '':
            a += int(decParts[0]) * int(len(decParts[1]) * '9')
        a += abs(int(ent)) * b   #la partie entiere
        if str(number)[0] == '-':
            a = -a

    # else if its a decimal..
    else:
        if decimalForm:
            return ent + '.' + dec

        a = int(dec) + abs(int(ent)) * 10 ** len(dec)
        b = int('1' + len(dec) * '0')
        if str(number)[0] == '-':
            a = -a

    # fraction simplification
    gcd = pgcd(a, b)
    a, b = int(a / gcd), int(b / gcd)

    # evaluate if its better to return the fraction or the raw number
    frac = '(' + str(a) + '/' + str(b) + ')'
    if len(frac) < 8 or len(frac) < len(str(number)):
        return frac
    # return frac #debug
    
    return str(number)

def genSpaces(string):
    string = str(string)

    if string.isnumeric():
        return int(string) * ' '
    
    return len(string) * ' '

def isFraction(string):
    string = str(string)
    if re.match(r'^\d+/\d+$', string):
        return True
    return False

def getValue(fraction):
    fraction = str(fraction)
    search = re.search(r'^(\d+)/(\d+)$', fraction)
    if search:
        a = int(search.group(1))
        b = int(search.group(2))
        return a/b
    
# print(fm(0.0419971997199))

inputText = \
'''
[a]ddition
[s]ubstraction
[m]ultiplication
[d]ivision
>'''

print('__Simple calculator__')
userInput=''

while userInput not in ['a', 's', 'm', 'd']:
    userInput = input(inputText)[0]

first = input('Enter a first operand : ')
second = input('Enter a second operand : ')
first = getValue(first) if isFraction(first) else float(first)
second = getValue(second) if isFraction(second) else float(second)

if userInput == 'a':
    op = fm(first) + ' + ' + fm(second)
    res = first + second

elif userInput == 's':
    op = fm(first) + ' - ' + fm(second)
    res = first - second

elif userInput == 'm':
    op = fm(first) + ' x ' + fm(second)
    res = first * second

elif userInput == 'd':
    op = fm(first) + ' / ' + fm(second)
    res = first / second

print(op, '=', fm(res))
if(not res.is_integer() and fm(res) != str(res)):
    print(genSpaces(op), '=', fm(res, True))