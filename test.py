from Mk.regex import Acronym

text = 'Le protocole WWW (Panier Wide Web) est superbe, \
mais je préfère la N.B.A(National Basketball Association).\
Vive la NASA (National Aeronautics and Space Administration).\
Je travaille pour le FBI (Federal Bureau of Investigation).\
Je travaille pour le FBI (Federal Bureau of Investigation).'

acronyms = Acronym.parseAcronyms(text)

for acro in acronyms:
    print(acro)