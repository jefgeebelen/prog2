# Oefeningen Geebelen Jef 5IICT 2021-11-19
# ee943e4cf6e04a42

def print_enkele_lijn():
    """Oef 1: Programmeert een functie die 'Beer' op het scherm afdrukt"""
    print('Beer')


def print_meerdere_lijnen():
    """Oef 2: Programmeer een functie die twee regels afdrukt. Op de eerste regel
    komt 'schaap' te staan, op de volgende 'Vis'."""
    print('schaap')
    print('Vis')


def print_leeftijd(l):
    """Oef 3: creër een functie die 'Hi! Je bent l jaar oud' afdrukt.
    Met l de gegeven waarde."""
    l = 57
    print(f'Hi! Je bent {l} jaar oud')


def print_oppervlakte_cirkel(r):
    """Oef 4: Schrijf een functie die 'Hi! De oppervlakte is: opp' 
    afdrukt. Met opp de oppervlakte van de cirkel met opgegeven straal r. Neem
    voor pi de waarde 3.14."""
    pi = 3.14
    print(f'Hi! de oppervlakte is: {r**2*3.14}')




def print_100_hallos():
    """Oef 5: Creërt een functie die 100 keer hallo afdrukt."""
    for i in range(100):
        print('hallo')

def print_x_keer_woord(x):
    """Oef 6: schrijft een functie die x keer 'haring' afdrukt."""
    for i in range(x):
        print('haring')

def print_x_genummerde_regels(x):
    """Oef 7: schrijf een functie die x keer 'dexter' afdrukt, voorafgegaan
    door regelnummers. Dus, b.v. bij x==2:
    1 dexter
    2 dexter
    """
    for i in range(x):
        print(f'{i+1} dexter')
        
    

def print_genummerde_regels_van_tot(x, y):
    """Oef 8: Maak een functie die meermaals hoen afdrukt, voorafgegaan
    door regelnummers. De regelnummering begint bij x en eindigt met y. Dus, b.v.
    bij x==5 en y==8:
    5 hoen
    6 hoen
    7 hoen
    """
    for i in range(x, y):
        print(f'{i} hoen')


def print_numbers():
    """Oef 9: programmeer een functie die voor de getallen 2 tot en met 6,
    de machten van 2 tot en met 4 hiervan afdrukt met behulp van een dubbele
    for-loop. Dus, b.v.:
    2 tot de 2de = 8 <:-(
    2 tot de 3de = 8 <:-(
    ...
    3 tot de 2de = 9 <:-(
    3 tot de 3de = 27 <:-(
    ...
    """
    for i in range(2, 6):
        for macht in [2, 3, 4]:
           print(f"{i} tot de {macht}de = {i**macht} <:-(")

def print_tv_shows(shows):
    """Oef 10: creer een functie die voor de gegeven lijst tv-series
    iedere show op een regel afdrukt voorafgegaan door een nummering.
    Dus, b.v. gegeven de lijst: ["the last kingdom", "the 100", "The Last Kingdom"],
    krijg je:
    1. the last kingdom
    2. the 100
    3. The Last Kingdom
    """
    

# Oefeningen Geebelen Jef 5IICT 2021-11-19
# ee943e4cf6e04a42