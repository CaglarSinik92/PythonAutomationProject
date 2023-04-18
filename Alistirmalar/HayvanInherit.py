class Hayvan:
    """
    class özellikleri
    ***********************
    Todo Türü
    Todo İsmi
    Todo Yaşadığı Yer
    Todo Beslenme Şekli
    ***********************
    """

    def __int__(self, türü, ismi, yaşadığıYer, beslenmeŞekli):
        self.türü = türü
        self.ismi = ismi
        self.yaşadığıYer = yaşadığıYer
        self.beslenmeŞekli = beslenmeŞekli

    def özellikleriYaz(self):
        print("Türü : {}\nİsmi : {}\nYaşadığı Yer : {}\nBeslenme Şekli : {}".format(self.türü,self.ismi,self.yaşadığıYer,self.beslenmeŞekli))