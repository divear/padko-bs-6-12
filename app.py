from datetime import datetime

class Test:
    def __init__(self):
        self.vse = "Všobecné znalosti"
        self.datum = datetime.now().strftime("%Y-%m-%d")
        self.odpovedi = [
            "Lisabon",
            "30 let",
            "144",
            "8 bitů",
            "Isaac Asimov"
        ]
        self.pointy = 0


    def typ_testu(self):
        moznost = input("Ktery typ testu chcete (T: Test P: Přijímačky)? ").upper()
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
    def kontrola(self, odpoved, index):
            if odpoved == self.odpovedi[index]:
                self.pointy+=1
    def otazky(self):
        self.otazky = [
            "Hlavní město Portugalska?",
            "Jak dlouho trvala 30 letá válka?",
            "12 x 12 = ?",
            "1 Byte = ? bitů?",
            "Autor díla Já, robot?"
        ]
        for (i,e) in enumerate(self.otazky):
            odpoved = input(f"\n{e} ")
            self.kontrola(odpoved, i)
        print(self.pointy)




d = Test()
d.otazky()


# Co chybi:
# b) tohle mozna mam ale idk radsi double check
# f) idk co really chce
# g) hodnoceni
# h) destruktor
# cela dvojka a trojka xd
