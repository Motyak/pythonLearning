import re

#Parse and print all distinct valid acronyms from a text

class Acronym:
    def __init__(self, word, standsFor):
        self.word = word.replace('.', '').upper()
        self.standsFor = standsFor

    @staticmethod
    def parseAcronyms(text):
        acronym = r'(?P<acronym>[A-Z](?:\.?[A-Z])(?:\.?[A-Z]){0,5}){1}'
        meaning = r'(?P<meaning>(?:[A-Z]{1}[a-z]+){1}(?:\ (?:(?:and|of)\ )?[A-Z]{1}[a-z]+)+)'
        pattern = r'{}\ ?\({}\)'.format(acronym, meaning)
        matches =  re.findall(pattern, text)

        acronyms = {Acronym(match[0], match[1]) for match in matches}
        return set(filter(Acronym._checkIfValid, acronyms))

    @staticmethod
    def _checkIfValid(acronym):
        return all(acronym.word[i] == Acronym._getMeaning(acronym, i)[0] 
                for i in range(0, len(acronym.word)))

    @staticmethod
    def _getMeaning(acronym, index):
        return list(filter(lambda x: x[0].isupper(), acronym.standsFor))[index]

    def __str__(self):
        return '{}, meaning {}'.format(self.word, self.standsFor)

    
text = 'Le protocole WWW (Panier Wide Web) est superbe, \
mais je préfère la N.B.A(National Basketball Association).\
Vive la NASA (National Aeronautics and Space Administration).\
Je travaille pour le FBI (Federal Bureau of Investigation).'

acronyms = Acronym.parseAcronyms(text)

for acro in acronyms:
    print(acro)
