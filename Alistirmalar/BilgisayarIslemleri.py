import time


class Bilgisayar:
    """"
    Done-Bilgisyarı açma
    Done-Bilgisayaro kapatmak
    Done-Bilgisayar yeniden başlatmak

    Done-Bilgisayar Sesini Kısmak
    Done-Bilgisayar Sessini Arttırmak

    Done-bilgisayar_ses_seviye_göster
    Done-bilgisayar_statu_goster
    Done-yuklu_programları_göster
    Done- Bilgisayar belleği gösterme

    Done-Bilgisayara program yükleme
        Done- Her program eklendiğinde bellekten düş
    Done- Bilgisayardan program silme
        Done- her program silindiğinde belleğe ekle

    todo - Bilgisayara Menü Hazırlama
    """

    def __int__(self, bilgisayarStatu="Kapalı", bilgisayarSes=0, yüklüProgramlar=["notepad"], bilgisayarBelleği=4096):
        self.bilgisayarStatu = bilgisayarStatu
        self.bilgisayarSes = bilgisayarSes
        self.yüklüProgramlar = yüklüProgramlar
        self.bilgisayarBelleği = bilgisayarBelleği

    def bilgisayar_açma(self):
        self.bilgisayarStatu = "Açık"
        return self.bilgisayar_statu

    def bilgisayar_kapama(self):
        self.bilgisayarStatu = "Kapalı"
        return self.bilgisayar_statu

    def bilgisayar_yeniden_baslatma(self):
        print("Bilgisayarınız yeniden başlatılıyor lütfen bekleyin...")
        time.sleep(2)
        print("Bilgisayarınız yeniden başlatıldı...")
        return self.bilgisayarStatu

    def bilgisayar_ses_acma(self):
        if self.bilgisayarSes != 40:
            self.bilgisayarSes += 1
            print("Bilgisayarınızın yeni ses seviyesi :{}".format(self.bilgisayarSes))

    def bilgisayar_ses_kısmak(self):
        if self.bilgisayarSes != 0:
            self.bilgisayarSes -= 1
            print("Yeni bilgisayar sesi {}".format(self.bilgisayarSes))

    def bilgisayar_ses_seviye_göster(self):
        return self.bilgisayarSes

    def bilgisayar_statu_goster(self):
        return self.bilgisayarStatu

    def yuklu_programları_göster(self):
        return self.yüklüProgramlar

    def bilgisayar_kalan_belleği(self):
        return self.bilgisayarBelleği

    def bilgisayara_program_yukleme(self, program, programBoyutu):
        self.yüklüProgramlar.append(program)
        self.bilgisayarBelleği -= programBoyutu
        return self.yüklüProgramlar

    def bilgisayardan_program_silme(self, program, programBoyutu):
        self.yüklüProgramlar.remove(program)
        self.bilgisayarBelleği += programBoyutu
        return self.yüklüProgramlar
