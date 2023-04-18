from Alistirmalar.HayvanInherit import Hayvan


class Köpek(Hayvan):
    def __int__(self, türü, ismi, yaşadığıYer, beslenmeŞekli, çıkardığıSes="Hav", kaçBacağıVar=4):
        super().__int__(türü, ismi, yaşadığıYer, beslenmeŞekli)
        self.çıkardığıSes = çıkardığıSes
        self.kaçBacağıVar = kaçBacağıVar

    def köpek_özellikleri_yazdir(self):
        print("Çıkardığı ses :{}\nKaç Bacağı Var : {}".format(self.çıkardığıSes, self.kaçBacağıVar))
