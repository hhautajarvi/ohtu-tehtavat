KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self.kapasiteetti_tarkistus(kapasiteetti, True)
        self.kasvatuskoko = self.kapasiteetti_tarkistus(kasvatuskoko, False)
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kapasiteetti_tarkistus(self, kapasiteetti, kapasiteetti_true):
        if kapasiteetti is None:
            if kapasiteetti_true:
                return KAPASITEETTI
            else:
                return OLETUSKASVATUS
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti") 
        else:
            return kapasiteetti

    def kuuluu(self, alkio):
        return alkio in self.ljono

    def lisaa(self, alkio):
        if not self.kuuluu(alkio):
            self.ljono[self.alkioiden_lkm] = alkio
            self.alkioiden_lkm += 1
            if self.alkioiden_lkm >= len(self.ljono):
                self.ljono.extend([0]*self.kasvatuskoko)
            return True
        return False

    def poista(self, alkio):
        if self.kuuluu(alkio):
            self.ljono.remove(alkio)
            self.alkioiden_lkm -= 1
            return True
        return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a_intjoukko, b_intjoukko):
        for luku in b_intjoukko.to_int_list():
            a_intjoukko.lisaa(luku)
        return a_intjoukko

    @staticmethod
    def leikkaus(a_intjoukko, b_intjoukko):
        for luku in b_intjoukko.to_int_list():
            if not a_intjoukko.kuuluu(luku):
                a_intjoukko.poista(luku)
        for luku in a_intjoukko.to_int_list():
            if luku not in b_intjoukko.to_int_list():
                a_intjoukko.poista(luku)
        return a_intjoukko

    @staticmethod
    def erotus(a_intjoukko, b_intjoukko):
        for luku in b_intjoukko.to_int_list():
            a_intjoukko.poista(luku)
        return a_intjoukko

    def __str__(self):
        lista = ', '.join([str(luku) for luku in self.to_int_list()])
        return "{" + lista + "}"

