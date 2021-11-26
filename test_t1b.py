# Oefeningen Geebelen Jef 5IICT 2021-11-26
# ee943e4cf6e04a42
import pytest
from herhalingt1b import *


def test_oef_1(capsys):
    print_meerdere_keren()
    output = capsys.readouterr().out
    assert output == "Muhammed Kathagen\n"*9

def test_oef_2(capsys):
    lijst = ["The witcher", "cavia", "meikever", "Goeienamiddag"]
    print_eerste_element_uit_lijst(lijst)
    output = capsys.readouterr().out.strip()
    assert output == "The witcher"

def test_oef_3a(capsys):
    lijst = ["Jens Bruynzeels", "Julia Roose", "Guusje Brandon"]
    print_laatste_element_uit_lijst(lijst)
    output = capsys.readouterr().out.strip()
    assert output == "Guusje Brandon"

def test_oef_3b(capsys):
    lijst = ["Bente Wigman", "Aya van Tuijl", "Bibi van Kuijc", "Lotte Rousselet"]
    print_laatste_element_uit_lijst(lijst)
    output = capsys.readouterr().out.strip()
    assert output == "Lotte Rousselet"

def test_oef_4a():
    lijst = ["Tracisteeg", "Kellydreef", "Deborahring", "Billyweg"]
    result = return_voorlaatste_element_uit_lijst(lijst)
    assert result == "Deborahring"

def test_oef_4b():
    lijst = ["Codylei", "Josephboulevard", "Thomasbaan"]
    result = return_voorlaatste_element_uit_lijst(lijst)
    assert result == "Josephboulevard"


def test_oef_5a_0():
    result = return_volume_0(4, 2)
    assert abs(result - 100.53) < 0.5

def test_oef_5b_0():
    result = return_volume_0(3, 5)
    assert abs(result - 141.37) < 0.5






def test_oef_6a():
    result = lijst_met_5_keer("Mouzaive")
    expected = ["Mouzaive"] * 5
    assert result == expected

def test_oef_6b():
    result = lijst_met_5_keer("Averbode")
    expected = ["Averbode"] * 5
    assert result == expected

def test_oef_7a():
    result = lijst_met_x_keer("Zelem", 4)
    expected = ["Zelem"] * 4
    assert result == expected

def test_oef_7b():
    result = lijst_met_x_keer("Sint-Gillis-bij-Dendermonde", 2)
    expected = ["Sint-Gillis-bij-Dendermonde"] * 2
    assert result == expected


def test_oef_8a():
    lijst = ["Korbeek-Lo", "Hamont-Achel"]
    result = lijst_voeg_woord_x_keer_toe(lijst, "Tonybaan" , 7)
    expected = ["Korbeek-Lo", "Hamont-Achel"] + ["Tonybaan"]*7
    assert result == expected

def test_oef_8b():
    lijst = ["Steenkerke", "Westvleteren", "Vremde"]
    result = lijst_voeg_woord_x_keer_toe(lijst, "Ericasingel" , 3)
    expected = ["Steenkerke", "Westvleteren", "Vremde"] + ["Ericasingel"]*3
    assert result == expected


def test_oef_9a():
    lijst = ["Gijs Duivenvoorden", "Sjoerd van Hamaland", "Gijs Duivenvoorden"]
    result = lijst_tel_aantal_woorden(lijst, "Gijs Duivenvoorden")
    assert result == 2

def test_oef_9b():
    lijst = ["Yusuf Schuylenborch", "Rosa Kwaadland-van der Spaendonc", "Rosa Kwaadland-van der Spaendonc"]
    result = lijst_tel_aantal_woorden(lijst, "Yusuf Schuylenborch")
    assert result == 1


def test_oef_10a():
    shows = [
        "x-files",
        "simpsons",
        "bojack horseman",
        "the last kingdom",
        "X-files",
        "The Witcher",
    ]
    result = lijst_nummering(shows)

    expected = [
        [1, "x-files"],
        [2, "simpsons"],
        [3, "bojack horseman"],
        [4, "the last kingdom"],
        [5, "X-files"],
        [6, "The Witcher"],
    ]
    assert result == expected

def test_oef_10b():
    shows = [
        "BoJack Horseman",
        "Lupin",
        "Ted lasso",
        "peaky blinders",
    ]
    result = lijst_nummering(shows)

    expected = [
        [1, "BoJack Horseman"],
        [2, "Lupin"],
        [3, "Ted lasso"],
        [4, "peaky blinders"],
    ]
    assert result == expected

# Oefeningen Geebelen Jef 5IICT 2021-11-26
# ee943e4cf6e04a42