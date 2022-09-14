"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Klára Zatloukalová
email: zatloukalova.klara@gmail.com
discord: Klára Z.#3895
"""

import random

### Generování random čísla.
def generovani():
    cislo_gen = set()
    while len(cislo_gen) < 4:
        cislo_gen.add(random.randint(0,9))
    return cislo_gen

cislo = list(generovani())
while cislo[0] == 0:
    cislo = list(generovani())

### Úvod do hry.
print('Hi there!')
print('-'*40)
print('''I've generated a random 4 digit number for you.''')
print('''Let's play a bulls and cows game.''')
print('-'*40)

### Funkce pro kontrolu vstupů.
def kontrola_vstupu(vstup):
    existuje_duplicita = 0
    if vstup.isnumeric():
        if len(vstup_cislo) > 4:
            print('Číslo je příliš dlouhé.')
            return False
        elif len(vstup_cislo) < 4:
            print('Číslo je příliš krátké.')
            return False
        elif len(vstup_cislo) == 4:
            for i in range(0, 4):
                for y in range(i + 1, 4):
                    if (vstup_cislo[i] == vstup_cislo[y]):
                        existuje_duplicita += 1
            if existuje_duplicita > 0:
                print('Duplicita ve vstupu.')
                return False
            if vstup_cislo[0] == '0':
                print('První číslo nesmí být nula.')
                return False
    else:
        print('Vstup není číslo.')
        return False
    return True

### Zadání vstupu uživatele a volání kontroly.
byci = 0
pocet_kol = 0
while byci != 4:

    vstup = (input('Enter a number: '))
    vstup_cislo = list(vstup)

    byci = 0
    kravy = 0

    if kontrola_vstupu(vstup):
        vstup_cislo_prevedeno = list(map(int, vstup_cislo))
        pocet_kol += 1

### Vyhodnocování výsledku.
        for x, t in zip(cislo, vstup_cislo_prevedeno):
            if t in cislo:
                kravy += 1
                if x == t:
                    byci += 1
                    kravy -= 1
        if byci == 1 and kravy == 1:
            print(byci, 'bull', kravy, 'cow')
            print('-' * 40)
        elif byci != 1 and kravy != 1:
            print(byci, 'bulls', kravy, 'cows')
            print('-' * 40)
        elif byci == 1 and kravy != 1:
            print(byci, 'bull', kravy, 'cows')
            print('-' * 40)
        elif byci != 1 and kravy == 1:
            print(byci, 'bulls', kravy, 'cow')
            print('-' * 40)
else:
    print('''Correct, you've guessed the right number in''', pocet_kol, '''guesses''')
    print('-' * 40)
    if pocet_kol == 1 and pocet_kol <= 2:
        print('''That's amazing.''')
    elif pocet_kol >= 3 and pocet_kol <= 6:
        print('''That's avarage.''')
    elif pocet_kol >= 7:
        print('''That's not so good.''')
    exit()





