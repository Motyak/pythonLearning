def pgcd(a, b):
    # a, b = int(a), int(b)   #check if a and b are integers

    while b != 0:
        r = a % b
        a, b = b, r
    return int(a)

def fm(number):
    dec = string(number)
    dec = dec[dec.find('.') + 1:]
    a = 0
    b = 1

    #if its a decimal number
    if number.isnumeric():
        number = float(number)
        #if its a whole number, get rid of the decimal part
        if number.is_integer():
            return str(int(number))
        else:
            a = int(dec)
            b = int('1' + len(dec) * '0')

    #if its a non-decimal number
    elif dec[-2:] == '..':
        a = int(dec[:-2])
        b = int(len(dec) * '9')
        
    #simplification de la fraction
    gcd = pgcd(a, b)
    a, b = a / gcd, b / gcd
    return '(' + str(a) + '/' + str(b) + ')'

inputText = '''\

[a]ddition
[s]oustraction
[m]ultiplication
[d]ivision
>'''

print('__Calculatrice simple__')
userInput=''

while userInput not in ['a', 's', 'm', 'd']:
    userInput = input(inputText)[0]

first = input('Enter a first number : ')
second = input('Enter a second number : ')

if userInput == 'a':
    print(fm(first) + ' + ' + fm(second) + ' = ' + fm(first + second))

elif userInput == 's':
    print(fm(first) + ' - ' + fm(second) + ' = ' + fm(first - second))

elif userInput == 'm':
    print(fm(first) + ' x ' + fm(second) + ' = ' + fm(first * second))

elif userInput == 'd':
    print(fm(first) + ' / ' + fm(second) + ' = ' + fm(first / second))
