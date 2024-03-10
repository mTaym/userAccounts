# main.py
##########################

# username listesi oluşturun.
# password listesi oluşturun.
# sign_up() - kayit() isimli fonksiyon yazın, bu fonksiyonun 2 argumanı olsun: userName, userPassword
# sign_in() - giris() isimli fonksiyon yazın, bu fonksiyonun 2 argumanı olsun: userName, userPassword
#                     eğer kullanıcı username listesi ve password listesindeki bilgileri
#                     doğru girerse "Welcome" yazdırsın. Diğer durumda 'hatalı giriş' yazdırsın.


# döngü oluşturun, kullanıcıdan input isteyelim: (K)ayıt / (G)iriş / (Ç)ıkış
# Kayıt yapmak isterse kullanıcıdan alınan kayıt bilgilerini listelere yazdıralım
# Giriş yapmak isterse kullanıcıdan alınan username ve password'e göre sisteme giriş yapıp
# yapamayacağı yazdırılsın.
# Hatalı girişlerde döngü doğru girişe kadar devam etsin.


import time
import accounts

secim = input("(K)ayıt / (G)iriş / (Ç)ıkış\n>> ").upper()

while True:
    if secim=="K":
        username = input("Kullanıcı adınızı oluşturunuz:\n>> ")
        password = input("Parolanızı oluşturunuz:\n>> ")
        accounts.kayit(username, password)
        time.sleep(2)
        secim = input("(G)iriş / (Ç)ıkış:\n>> ").upper()
    elif secim=="G":
        username = input("Kullanıcı adınızı giriniz:\n>> ")
        password = input("Parolanızı giriniz:\n>> ")
        giris_ok = accounts.giris(username, password)
        time.sleep(2)
        if giris_ok:
            secim = input("(Ç)ıkış:\n>> ").upper()
        else:
            secim = input("(G)iriş / (Ç)ıkış\n>> ").upper()
    elif secim=="Ç":
        print("Hoşçakalın. Çıkış yapıldı.")
        break
    else:
        print("Hatalı tercih yaptınız tekrar deneyin.")
        secim = input("(K)ayıt / (G)iriş / (Ç)ıkış\n").upper()






