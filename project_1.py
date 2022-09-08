"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Klara Zatloukalova
email: zatloukalova.klara@gmail.com
discord: Klára Z.#3895
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

oddelovac = '-'*40

databaze_uzivatelu = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

### Autentifikace uživatele

prihl_jmeno = input('Username: ')
if prihl_jmeno in databaze_uzivatelu:
    heslo = input('Password: ')
    if databaze_uzivatelu[prihl_jmeno] == heslo:
        print('Welcome to the app, ', prihl_jmeno.capitalize(), '.')
        prihlaseny= 1
    else:
        print('Wrong password, terminating the program...')
        prihlaseny = 0
else:
    print('Unregistered user, terminating the program...')
    prihlaseny = 0

### Uspěšná autentifikace uživatele. Nabídka textů.

if prihlaseny == 1:
    print('We have', len(TEXTS), 'texts to be analyzed.')
    print(oddelovac)
    cislo_textu = input('Enter a number btw. 1 and 3 to select: ')
    if cislo_textu == str(1) or cislo_textu == str(2) or cislo_textu == str(3):
        text = TEXTS[(int(cislo_textu) - 1)]
        print(oddelovac)

### Analýza textu.

        print('There are', len(text.split()), 'words in the selected text.')

        pocet_velkych = 0
        pocet_vsechna_velka = 0
        pocet_vsechna_mala = 0
        pocet_cisel = 0
        soucet_cisel = 0

        text = text.replace(',', '')
        text = text.replace('.', '')
        text_do_pole = text.split()

        for x in text_do_pole:
            if (x.istitle()):
                pocet_velkych += 1
            if (x.isupper()):
                pocet_vsechna_velka += 1
            if (x.islower()):
                pocet_vsechna_mala += 1
            if (x.isnumeric()):
                pocet_cisel += 1
                soucet_cisel += int(x)
        print('There are ', pocet_velkych, ' titlecase words.')
        print('There are ', pocet_vsechna_velka, ' uppercase words.')
        print('There are ', pocet_vsechna_mala, ' lowercase words.')
        print('There are ', pocet_cisel, ' numeric string.')
        print('The sum of all numbers is ', soucet_cisel)
        print (oddelovac)
        print ('LEN | OCCURENCES    | NR.')
        print (oddelovac)

### Tvorba sloupcového grafu

        pole_delek_uplne = []
        for z in text_do_pole:
            pole_delek_uplne.append(len(z))

        vysledek = []

        for t in range(0, max(pole_delek_uplne)+1):
            vysledek.append(0)
            for prvek in text_do_pole:
               if len(prvek) == t:
                    vysledek[t] += 1

        for index, q in enumerate(vysledek):
            if q != 0:
               if index < 10:
                  print(index, '  |', '*'*q, ' '*(12-q), '|', q)
               else:
                  print(index, ' |', '*' * q, ' ' * (12 - q), '|', q)

    else:
        print('Wrong input, the program terminates.')