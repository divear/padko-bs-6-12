from datetime import datetime

class Test:
    def __init__(self):
        self.vse = "Všobecné znalosti"
        self.datum = datetime.now().strftime("%Y-%m-%d")
        self.odpovedi = []

    def typ_testu(self):
        moznost = input("Ktery typ testu chcete (T: Test P: Přijímačky)? ")
        if moznost == "T":
            print("test")
        elif moznost == "P":
            print("prijimacky")
        # tady jeste chce "vstup pro zvolenou možnost výběru"
    def zapis(self):
        self.jmeno = input("Vase jmeno a prijimeni: ")
        self.trida = input("Vase trida: ")
        self.predmet =  "matika idk"
        return f"Pocatecni informace: \n predmet: {self.predmet} \n datum: {self.datum}\nJmeno a prijimeni: {self.jmeno}\ntrida: {self.trida}"
    def otazky(self):
        self.otazky = [
            "Hlavní město Portugalska?",
            "Jak dlouho trvala 30 letá válka?",
            "12 x 12 = ?",
            "1 Byte = ? bitů?",
            "Autor díla Já, robot?"
        ]


d = Test()
d.typ_testu()
