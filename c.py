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

first = float(input('Enter a first number : \n>'))
second = float(input('Enter a second number : \n>'))

if userInput == 'a':
    print(first, ' + ', second, ' = ', first + second)

elif userInput == 's':
    print(first, ' - ', second, ' = ', first - second)

elif userInput == 'm':
    print(first, ' x ', second, ' = ', first * second)

elif userInput == 'd':
    print(first, ' / ', second, ' = ', first / second)
