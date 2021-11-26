# Oefeningen Geebelen Jef 5IICT 2021-11-19
# ee943e4cf6e04a42

import sys
import unittest

from herhalingt1a import *


class TestStringMethods(unittest.TestCase):
    def test_oef_1(self):
        print_enkele_lijn()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Beer")

    def test_oef_2(self):
        print_meerdere_lijnen()
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "schaap\nVis")

    def test_oef_3a(self):
        print_leeftijd(78)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Hi! Je bent 78 jaar oud")

    def test_oef_3b(self):
        print_leeftijd(57)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Hi! Je bent 57 jaar oud")

    def test_oef_4a(self):
        print_oppervlakte_cirkel(19)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Hi! de oppervlakte is: 1133.54")

    def test_oef_4b(self):
        print_oppervlakte_cirkel(38)
        output = sys.stdout.getvalue().strip()
        self.assertEqual(output, "Hi! de oppervlakte is: 4534.16")

    def test_oef_5a(self):
        print_100_hallos()
        output = sys.stdout.getvalue().strip()
        expected = "hallo\n" * 100
        self.assertEqual(output, expected.strip())

    def test_oef_6(self):
        print_x_keer_woord(15)
        output = sys.stdout.getvalue().strip()
        expected = "haring\n" * 15
        self.assertEqual(output, expected.strip())

    def test_oef_7a(self):
        print_x_genummerde_regels(3)
        output = sys.stdout.getvalue().strip()

        expected = """1 dexter
2 dexter
3 dexter
        """
        self.assertEqual(output, expected.strip())

    def test_oef_7b(self):
        print_x_genummerde_regels(5)
        output = sys.stdout.getvalue().strip()

        expected = """1 dexter
2 dexter
3 dexter
4 dexter
5 dexter
        """
        self.assertEqual(output, expected.strip())

    def test_oef_8a(self):
        print_genummerde_regels_van_tot(3, 7)
        output = sys.stdout.getvalue().strip()

        expected = """3 hoen
4 hoen
5 hoen
6 hoen
        """
        self.assertEqual(output, expected.strip())

    def test_oef_8b(self):
        print_genummerde_regels_van_tot(1021, 1023)
        output = sys.stdout.getvalue().strip()

        expected = """1021 hoen
1022 hoen
        """
        self.assertEqual(output, expected.strip())

    def test_oef_9(self):
        print_numbers()
        output = sys.stdout.getvalue().strip()

        expected = """2 tot de 2de = 4 <:-(
2 tot de 3de = 8 <:-(
2 tot de 4de = 16 <:-(
3 tot de 2de = 9 <:-(
3 tot de 3de = 27 <:-(
3 tot de 4de = 81 <:-(
4 tot de 2de = 16 <:-(
4 tot de 3de = 64 <:-(
4 tot de 4de = 256 <:-(
5 tot de 2de = 25 <:-(
5 tot de 3de = 125 <:-(
5 tot de 4de = 625 <:-(
6 tot de 2de = 36 <:-(
6 tot de 3de = 216 <:-(
6 tot de 4de = 1296 <:-(
"""
        for i, j in zip(output.split("\n"), expected.split("\n")):
            self.assertEqual(i, j)

    def test_oef_10(self):
        shows = [
            "the last kingdom",
            "the 100",
            "The Last Kingdom",
            "breaking bad",
            "X-Files",
            "x-files",
        ]
        print_tv_shows(shows)
        output = sys.stdout.getvalue().strip()

        expected = """1. the last kingdom
2. the 100
3. The Last Kingdom
4. breaking bad
5. X-Files
6. x-files
"""
        self.assertEqual(output, expected.strip())


if __name__ == "__main__":
    unittest.main(buffer=True)

# Oefeningen Geebelen Jef 5IICT 2021-11-19
# ee943e4cf6e04a42