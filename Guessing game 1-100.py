#1-) Rastgele 1-100 arasında sayılar seçtir.
#2-) Seçilen sayıyı tahmin için input al.
#3-) Yüksek, düşük olarak tahmine geri bildirim sağla ve döngüyü devam ettir.
#4-) Sonucu bulunca döngüyü bitir.
#5-) Tahmin sayılarını tut.


import random

rastgele_sayi = random.randint(1,100)

tahminler = []


while True:

    tahmin = int(input("1-100 arasında tahminde bulun:"))

    tahminler.append(tahmin)

    if tahmin == rastgele_sayi:
        print("Tebrikler! Doğru tahmin. " +str(len(tahminler))+". tahmininde bildin." )
        break

    elif tahmin > rastgele_sayi :
        print("Tahminin yüksek ⏫, Tekrar dene! " +str(len(tahminler))+". tahmine ulaştın.")

    else:
        print("Tahminin düşük ⏬, Tekrar dene! " +str(len(tahminler))+". tahmine ulaştın.")



        #KENDİME NOTLAR:
        # Tahmin inputunu döngü dışında bıraktım ve dakikalarca tekrar eden tahminin düşük sonucunu aldım kodu çalıştırırken :D
        # Tahminleri tutmak için liste oluşturdum ve len komutu ile listede ki tahmin sayısını aldım. len'i direkt kullandığımda sayıyı integer olarak aldığı için hata aldım
        # bu yüzden stringe çevirdim.






