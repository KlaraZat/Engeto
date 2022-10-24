"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Klara Zatloukalova
email: zatloukalova.klara@gmail.com
discord: Klára Z.#3895
"""

import requests
from bs4 import BeautifulSoup
import sys
import csv

pole_jmena_mest = []
pole_kody_mest = []
pole_adres = []
seznam_stran = []
volebni_vysledky_pole = []

# Nacteni volebnich stran. Volano ve funkci nacti_volebni_vysledky.
def nacti_jmena_stran(polevka):
    jmeno_stran_vse = polevka.find_all(class_="overflow_name")
    for jmeno_strany in jmeno_stran_vse:
        seznam_stran.append(jmeno_strany.getText())

# Nacteni detailnich dat z hypertextoveho odkazu stranky. Voláno ve funkci nacti_data_ze_stranky.
def nacti_volebni_vysledky(vysledky_url):
    pole_souhrn = []
    pole_pocet_hlasu = []

    stranka = requests.get(vysledky_url)
    polevka = BeautifulSoup(stranka.content, 'html.parser')

    volici_v_seznamu = polevka.find(class_="cislo", headers="sa2").getText().replace('\xa0', '')
    vydane_obalky = polevka.find(class_="cislo", headers="sa3").getText().replace('\xa0', '')
    platne_hlasy = polevka.find(class_="cislo", headers="sa6").getText().replace('\xa0', '')

    pole_souhrn = [volici_v_seznamu, vydane_obalky, platne_hlasy]

    # Volání fce načtení seznamu stran za účelem vytvoření hlavičky souboru. Pokud již bylo načteno, přeskočí se.
    if not seznam_stran: nacti_jmena_stran(polevka)

    pocet_hlasu_vse = polevka.find_all(class_="cislo", headers="t1sa2 t1sb3")
    pocet_hlasu_vse += polevka.find_all(class_="cislo", headers="t2sa2 t2sb3")

    for pocet_hlasu in pocet_hlasu_vse:
        pole_pocet_hlasu.append(pocet_hlasu.getText().replace('\xa0', ''))

    return pole_souhrn + pole_pocet_hlasu

# Nacteni zakladnich dat ze stranky.
def nacti_data_ze_stranky(okres_url):
    URL = okres_url

    adresa_html_zaklad = "https://volby.cz/pls/ps2017nss/"

    stranka = requests.get(URL)

    polevka = BeautifulSoup(stranka.content, 'html.parser')

    kod_mesta_vse = polevka.find_all(class_="cislo")
    jmeno_mesta_vse = polevka.find_all(class_="overflow_name")

    for jmeno_mesta in jmeno_mesta_vse:
        pole_jmena_mest.append(jmeno_mesta.getText())

    for kod_mesta in kod_mesta_vse:
        pole_kody_mest.append(kod_mesta.getText())
        volebni_vysledky_pole.append(nacti_volebni_vysledky(adresa_html_zaklad + (kod_mesta.find('a').get('href'))))

# Vytvoreni souboru.
def vytvor_csv(soubor):
    header = ['kod', 'lokace', 'volici', 'vydane obalky', 'platne hlasy'] + seznam_stran

    with open(soubor, 'w', newline = '', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for i in range(0, len(pole_kody_mest)):
            tmp_radek = []
            tmp_radek.append(pole_kody_mest[i])
            tmp_radek.append(pole_jmena_mest[i])
            for j in range(0, len(volebni_vysledky_pole[i])):
                tmp_radek.append(volebni_vysledky_pole[i][j])

            writer.writerow(tmp_radek)

# Kontrola vstupních parametrů.
def kontrola():
    parametry = sys.argv
    if len(parametry) != 3:
        print("Špatný počet parametrů. Program se ukončí.")
        quit()
    elif "https://volby.cz/pls/ps2017nss/" not in parametry[1]:
        print("URL adresa není správná. Program se ukončí.")
        quit()
    elif '.csv' not in parametry[2]:
        print("Výstup může být uložen pouze do .csv souboru. Program se ukončí.")
        quit()
    else:
        return parametry[1], parametry[2]

# Spouštění.
def main():
    url, soubor = kontrola()
    nacti_data_ze_stranky(url)
    vytvor_csv(soubor)

if __name__ == "__main__":
    main()

