def problem1():
    x = 1
    toplam = 0
    sayi = int(input("Lütfen bir sayı giriniz:"))
    while (x < sayi):
        if (sayi % x == 0):
            toplam += x
            print("Bölenleri :", x)
        x += 1
    if (toplam == sayi):
        print("Mükemmel bir sayı seçtiniz")
    else:
        print(" :( çok kötü bir sayı")


def problem2():
    sayı = input("Sayı:")
    basamak_sayisi = len(sayı)
    sayı = int(sayı)
    basamak = 0
    toplam = 0

    gecici_sayı = sayı

    while (gecici_sayı > 0):
        basamak = gecici_sayı % 10

        toplam += basamak ** basamak_sayisi

        gecici_sayı //= 10

    if (toplam == sayı):
        print(sayı, "bir armstrong sayısıdır.")
    else:
        print(sayı, "bir armstrong sayısı değildir.")


def problem3():
    for i in range(1, 11):
        print("*************************************************")
        for j in range(1, 11):
            print("{} x {} = {}".format(i, j, i * j))


def problem4():
    toplam = 0
    while (True):
        sayi = input("Bir sayı giriniz:")
        temp_input = str(sayi)
        if (temp_input == "q"):
            break
        else:
            toplam += int(sayi)
    print("Toplam = ", toplam)


def problem5():
    for i in range(1, 101):
        if (i % 3 != 0):
            continue
        print(i)


def problem6():
    liste = [i for i in range(1, 101) if i % 2 == 0]
    print(liste)


def asalsayiBulma(sayi):
    # sayi = input("Bir sayı giriniz:")
    while True:
        if sayi == "q":
            break
        else:
            sayi = int(sayi)
            if asalsayiBulma(sayi):
                print("Sayı asal sayıdır")
                break
            else:
                print("Asal bir sayı değildir.")
                break
    if (sayi == 1):
        return False
    elif sayi == 2:
        return True
    else:
        for i in range(2, sayi):
            if (sayi % i == 0):
                return False
        return True


def toplama(a, b):
    return a + b


def çıkarma(a, b):
    return a - b


def bölme(a, b):
    return a / b


def çarpma(a, b):
    return a * b


def faktoriyel(a):
    toplam = 1
    while (a > 1):
        toplam *= a
        a -= 1
    return toplam


def hesap_makinesi():
    """
    Toplama
    Çıkarma
    Bölme
    Çarpma
    """
    print("""
    *****************************************
    ***** Hesap Makinesine Hoş geldiniz *****
    Topama Yapmak için 1 giriniz
    Çıkarma için 2 giriniz
    Bölme için 3 giriniz
    Çarpma için 4 giriniz
    Çıkmak için 5 giriniz
    """)
    while True:
        secim = int(input("Bir seçim yapınız :"))
        if secim == 1:
            a = int(input("Toplanacak 1. sayıyı giriniz :"))
            b = int(input("Toplanacak 2. sayıyı giriniz :"))
            print("Sonucunuz :", toplama(a, b))
        elif secim == 2:
            a = int(input("Çıkartma yapılacak sayıyı giriniz :"))
            b = int(input("Çıkartılacak sayıyı giriniz :"))
            print("Sonucunuz :", çıkarma(a, b))
        elif secim == 3:
            a = int(input("Çarpılacak 1. sayıyı giriniz :"))
            b = int(input("Çarpılacak 2. sayıyı giriniz :"))
            print("Sonucunuz :", çarpma(a, b))
        elif secim == 4:
            a = int(input("Bölünen sayıyı giriniz :"))
            b = int(input("Bölen sayıyı giriniz :"))
            print("Sonucunuz :", bölme(a, b))
        elif secim == 5:
            break
