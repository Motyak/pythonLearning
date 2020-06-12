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
        # if substring <= pattern:
        if len(substring) <= len(pattern):
            if not pattern.startswith(substring):
                return False
        elif not substring.startswith(pattern):
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
    if(len(dec) >= 10):
        fixedDecPart, periodicDecPart = period(number)  

        if decimalForm:
            return '{0}.{1}[{2}]..'.format(ent, fixedDecPart, periodicDecPart)

        b = int(len(periodicDecPart) * '9') * 10 ** len(fixedDecPart)
        a = int(periodicDecPart) + abs(int(ent)) * b
        if fixedDecPart != '':
            a += int(fixedDecPart) * int(len(periodicDecPart) * '9')
        if str(number)[0] == '-':
            a = -a

    # else if its a decimal..
    else:
        if decimalForm:
            return str(number)

        a = int(dec) + abs(int(ent)) * 10 ** len(dec)
        b = int('1' + len(dec) * '0')
        if str(number)[0] == '-':
            a = -a

    # fraction simplification
    gcd = pgcd(a, b)
    a, b = int(a / gcd), int(b / gcd)

    # evaluate if its shorter to return the fraction or the raw number
    frac = '({0}/{1})'.format(a, b)
    if len(frac) < 8 or len(frac) < len(str(number)):
        return frac
    
    return str(number)

# print(fm(0.040419971997, True))   # example

def isfloat(val):
    try:
        float(val)
        return True
    except ValueError:
        return False

def isFraction(string):
    string = str(string)
    if re.match(r'^-?\d+/\d+$', string):
        return True
    return False

def getValue(fraction):
    fraction = str(fraction)
    search = re.search(r'^(-?\d+)/(\d+)$', fraction)
    if search:
        a = int(search.group(1))
        b = int(search.group(2))
        return a/b

def askForOperand(inputMsg):
    first = input(inputMsg)
    try:
        return getValue(first) if isFraction(first) else float(first)
    except ValueError:
        return askForOperand(inputMsg)

if __name__ == '__main__':
    map = { 'a':('+', lambda a, b: a + b), 
            's':('-', lambda a, b: a - b), 
            'm':('*', lambda a, b: a * b), 
            'd':('/', lambda a, b: a / b)   }

    inputText = \
'''
[a]ddition
[s]ubstraction
[m]ultiplication
[d]ivision
>'''

    print('__Not that simple calculator__')

    userInput = ' '
    while userInput not in 'asmd':
        userInput = input(inputText)
        userInput = userInput[0] if userInput != '' else ' '

    first = askForOperand('Enter a first operand : ')
    second = askForOperand('Enter a second operand : ')

    op = ' '.join([fm(first), map[userInput][0], fm(second)])
    res = map[userInput][1](first, second)

    print(op, '=', fm(res))
    #changer la condition pour que ça s'affiche pour 0.040419971997
    if(not res.is_integer() and fm(res) != str(res)):
        print(len(op) * ' ', '=', fm(res, True))
    # print(len(op) * ' ', '=', fm(res, True))