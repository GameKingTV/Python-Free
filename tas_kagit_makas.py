    #Rock,pepper,scissors oyunu hazırla. tas_kagit_makas_ABDULSAMET_OZKAN
    #2 kere kazanan oyunu kazanır genel puanı +1
    #Oyun sonrası oyuncu ve bilgisayar için ikinci bir oyun isteyip istemediği sorulacak
    #Oyuncuya bir karşılama mesajı hazırla,oyunu tanıt,nasıl oynanacağı ve çıkma talimatı
    #Oyunu kodla istatistikler oynanan oyun/tur/oyuncu/total/
    #Yanlış bir komut için yeniden giriş yap.
    #bilgisayarın ikinci bir oyun tercihini random kullan.


import random

def tas_kagit_makas_ABDULSAMET_OZKAN():
    def tas_kagit_makas_kurallar():
        print("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀")
        print("Taş Kağıt Makas Oyununa Hoşgeldin!")
        print("Bu oyun iki oyuncu arasında oynanır.")
        print("Taş makası, makas kağıdı, kağıt da taşı yener.")
        print("Aynı seçim yapılırsa oyun berabere biter.")
        print("İki kez kazanan taraf oyunu kazanır.")
        print("Çıkmak için 'çıkış' yazabilirsiniz.")

    def oyuncu_secimi():
        while True:
            secim = input("Taş, Kağıt, Makas veya Çıkış ? = ").lower()
            if secim in ["taş", "kağıt", "makas", "çıkış"]:
                return secim
            print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyin.")

    def bilgisayar_secimi():
        return random.choice(["taş", "kağıt", "makas"])

    def sonuc_belirle(oyuncu_secim, bilgisayar_secim):
        if oyuncu_secim == bilgisayar_secim:
            return "Berabere!"
        elif (oyuncu_secim == "taş" and bilgisayar_secim == "makas") or \
             (oyuncu_secim == "kağıt" and bilgisayar_secim == "taş") or \
             (oyuncu_secim == "makas" and bilgisayar_secim == "kağıt"):
            return "Tebrikler Kazandınız!"
        else:
            return "Olamaz! Bu turu kaybettin."

    def bilgisayar_yeni_oyun_istek():

        return random.choice(["evet", "hayır"])


    def oyun_oyna(oyun_sayaci, ilk_oyun):

        oyuncu_puan = 0
        bilgisayar_puan = 0
        round_sayaci = 1

        while True:
            print("")
            print(f"###Oyun {oyun_sayaci}, Etap {round_sayaci} Başladı!###")
            print("")
            oyuncu_secim = oyuncu_secimi()

            if oyuncu_secim == "çıkış":
                if ilk_oyun:
                    print("Oyun sonlandırılıyor.")
                    print("Madem oynamayacaktın beni neden rahatsız ettin?")
                else:
                    print("Oyun sonlandırılıyor.")
                return False

            bilgisayar_secim = bilgisayar_secimi()

            print(f"Bilgisayar: {bilgisayar_secim}")
            sonuc = sonuc_belirle(oyuncu_secim, bilgisayar_secim)
            print(sonuc)

            if sonuc == "Tebrikler Kazandınız!":
                oyuncu_puan += 1
            elif sonuc == "Olamaz! Bu turu kaybettin.":
                bilgisayar_puan += 1

            print("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀")
            print("")
            print(f"Puan Durumu - Siz: {oyuncu_puan}, Bilgisayar: {bilgisayar_puan}")
            print("")
            print("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀")

            if oyuncu_puan == 2 or bilgisayar_puan == 2:
                break

            round_sayaci += 1

        if oyuncu_puan > bilgisayar_puan:
            print("Tebrikler! Oyunu Kazandınız!")
            return "oyuncu"
        else:
            print("Üzgünüm, Bilgisayar Kazandı!")
            return "bilgisayar"

    # Ana oyun döngüsü ve kullanıcı arayüzü
    tas_kagit_makas_kurallar()
    toplam_oyun_sayaci = 1
    oyuncu_toplam_puan = 0
    bilgisayar_toplam_puan = 0

    ilk_oyun = True

    while True:
        print("▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀")
        print("")
        print(f"🔥Genel Puan Durumu - Siz: {oyuncu_toplam_puan}, Bilgisayar: {bilgisayar_toplam_puan}🔥")
        oyun_devam = oyun_oyna(toplam_oyun_sayaci, ilk_oyun)

        if not oyun_devam:
            break

        print("\nOyun bitti!")
        kazanan = oyun_devam

        if kazanan == "oyuncu":
            oyuncu_toplam_puan += 1
        elif kazanan == "bilgisayar":
            bilgisayar_toplam_puan += 1

        while True:
            oyuncu_devam = input("Yeni bir oyun oynamak ister misiniz? (Evet/Hayır): ").lower()
            if oyuncu_devam not in ["evet", "hayır"]:
                print("Geçersiz giriş. Lütfen 'Evet' veya 'Hayır' girin.")
                continue

            bilgisayar_devam = bilgisayar_yeni_oyun_istek()
            print(f"Bilgisayar: Yeni bir oyun oynamak ister misiniz? {bilgisayar_devam.capitalize()}")

            if oyuncu_devam == "hayır" or bilgisayar_devam == "hayır":
                print(
                    "Sonra ki oyunda tekrar görüşmek üzere."

            if oyuncu_devam == "hayır" else "Şimdilik benden bu kadar. Hoşçakal!")
                print(f"🔥 Genel Puan Durumu - Siz: {oyuncu_toplam_puan}, Bilgisayar: {bilgisayar_toplam_puan} 🔥")
                return

            if oyuncu_devam == "evet" and bilgisayar_devam == "evet":
                toplam_oyun_sayaci += 1
                ilk_oyun = False
                break

# Fonksiyonu çalıştır.
tas_kagit_makas_ABDULSAMET_OZKAN()







