# Oefeningen Geebelen Jef 5IICT 2021-11-26
# ee943e4cf6e04a42

def print_meerdere_keren():
    """Oef 1: Creër een functie die 9 keer 'Muhammed Kathagen' op het scherm afdrukt"""
    for i in range(9):
        print("Muhammed Kathagen")

def print_eerste_element_uit_lijst(lijst):
    """Oef 2: Maak een functie die het eerste element uit lijst afdrukt."""
    print(lijst[0])


def print_laatste_element_uit_lijst(lijst):
    """Oef 3: schrijf een functie die het laatste element uit een lijst afdrukt."""
    print(lijst[-1])


def return_voorlaatste_element_uit_lijst(lijst):
    """Oef 4: maak een functie die het voorlaatste element van lijst teruggeeft."""
    return(lijst[-2])

def return_volume_0(straal, hoogte):
    """Oef 5: programmeer een functie die het volume van cilinder teruggeeft."""
    pi = 3.14
    return(pi*straal**2*hoogte)






def lijst_met_5_keer(woord):
    """Oef 6: Schrijf een functie die een lijst met 5 element 'woord' teruggeeft.
    Dus, lijst_met_5_keer("Linkebeek") geeft ["Linkebeek", "Linkebeek", "Linkebeek", "Linkebeek", "Linkebeek"].
    """
    lijst = []
    for i in range(5):
         lijst.append(woord)
    return(lijst)

def lijst_met_x_keer(woord, aantal):
    """Oef 7: schrijft een functie die een lijst met 'aantal' keer het woord 'woord' teruggeeft.
    Dus, lijst_met_x_keer("Estinnes", 2) zou ["Estinnes", "Estinnes"] geven.
    """
    lijst = []
    for i in range(aantal):
         lijst.append(woord)
    return(lijst)

def lijst_voeg_woord_x_keer_toe(lijst, woord, aantal):
    """Oef 8: maakt een functie die het woord 'aantal' keren achteraan de lijst toevoegd
    en deze lijst teruggeeft.
    lijst = ["konijn"]
    Dus, lijst_voeg_woord_x_keer_toe(lijst, "haas", 2) geeft:
    lijst == ["konijn", "haas", "haas"]
    """
    
    for i in range(aantal):
         lijst.append(woord)
    return(lijst)
    return(aantal)


def lijst_tel_aantal_woorden(lijst, woord):
    """Oef 9: Schrijft een functie die het aantal keer dat een woord voorkomt in een lijst teruggeeft.
    Dus, lijst_tel_aantal_woorden(["a", "b", "a"], "a") geeft 2 terug.
    """
    return lijst.count(woord)



def lijst_nummering(lijst):
    """Oef 10: creer een functie die voor de gegeven lijst een nieuwe
    geneste lijst maakt, met telkens het volgnummer en het element.
    .
    Dus, b.v. gegeven de lijst: ["x-files", "simpsons", "bojack horseman"],
    geef je een nieuwe lijst terug:
    [
        [1, "x-files"],
        [2, "simpsons"],
        [3, "bojack horseman"],
    ]
    """
    lijst1 = []
    nummer = 1
    for i in lijst:
        lijst2 = []
        lijst2.append(nummer)
        nummer = nummer+1
        lijst2.append(i)
        lijst1.append(lijst2)
    return(lijst1)

# Oefeningen Geebelen Jef 5IICT 2021-11-26
# ee943e4cf6e04a42