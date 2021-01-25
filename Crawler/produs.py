class Produs:
    def __init__(self, nume, pret, detinut, tip):
        self.tip = tip
        self.nume = nume
        self.pret = []
        self.pret.append(pret)
        self.detinut = detinut
        self.tendinta = 0
        self.pret_initial = pret
        self.pret_max = pret


    def modif_pret(self, pret):
        if pret > self.pret[0]:
            self.creste()
        else:
            self.scade()
        if pret > self.pret_max:
            self.pret_max = pret
        self.pret.insert(0, pret)
        if len(self.pret) > 50:
            self.pret.pop()


    def cumpar(self):
        seld.detinut = True


    def vandut(self):
        self.detinut = False


    def status(self):
        return self.detinut


    def creste(self):
        self.tendinta = 1


    def scade(self):
        self.tendinta = -1


    def afisare_produs(self):
        print(f'{self.tip} - {self.nume} a avut pretul initial de {self.pret_initial} si are tendinta {self.tendinta} si are preturile : ')
        for pret1 in self.pret:
            print(pret1)
