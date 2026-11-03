
class Werknemer:
    def __init__(self, naam, functie):
        self.naam = naam
        self.functie = functie

    def stel_voor(self):
        print(f"Mijn naam is {self.naam} en ik werk als {self.functie}.")

    def wijzig_functie(self, nieuwe_functie):
        self.functie = nieuwe_functie
        print(f"{self.naam} heeft nu de functie: {self.functie}")


werknemers = [
    Werknemer("George", "ontwikkelaar"),
    Werknemer("Anna", "designer"),
    Werknemer("Peter", "manager")
]

print("OVERZICHT VAN DE WERKNEMERS")
print("----------------------------")

for werknemer in werknemers:
    werknemer.stel_voor()

print("\nFUNCTIE WIJZIGEN")
werknemers[0].wijzig_functie("projectleider")

print("\nNIEUWE SITUATIE")
werknemers[0].stel_voor()
