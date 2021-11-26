naam = input("wat is je naam")
tickets = input("hoeveel tickets had je gewild")
prijs = input("wat is de prijs van de tickets")

prijs = int(prijs)
tickets = int(tickets)

print(f"hallo {naam} je had graag {tickets} gewild de prijs van de tickets is {prijs} ")
print(f"het totale bedrag van de tickets is {prijs*tickets}")