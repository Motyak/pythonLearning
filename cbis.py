inputText = '[a]ddition\n[s]ubstraction\n[m]ultiplication\n[d]ivision\n>'
{   'a':(lambda a, b: print(a, ' + ', b, ' = ', a + b)), 
    's':(lambda a, b: print(a, ' - ', b, ' = ', a - b)), 
    'm':(lambda a, b: print(a, ' x ', b, ' = ', a * b)),    
    'd':(lambda a, b: print(a, ' / ', b, ' = ', a / b))
}[input(inputText)[0]](float(input('Enter a first operand : ')), float(input('Enter a second operand : ')))