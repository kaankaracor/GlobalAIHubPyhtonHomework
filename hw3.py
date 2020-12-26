import random
liste1 = ["a","b","c","ç","d","e","f","g","ğ","h","i","ı","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
i = 0
kelime = []
sayı = random.randint(3,10)
while i < sayı:
    harf = random.choice(liste1)
    kelime.append(harf)
    i+=1
a = input("Başlamadan önce lütfen isminizi giriniz:")


print("""------------------------ADAM ASMACA------------------------

OYUNA HOŞGELDİN %s BOL ŞANS DİLİYORUM BUNA İHTİYACIN OLACAK!

OYUNUMUZUN KURALLARI
1)3 yanlış cevapta adam maalesef ölür.
2)Çıkmak isterseniz "1" tuşuna basın.
"""%a.upper())
print("Bulmaya çalıştığın kelime %d harf içerir"%sayı)

print(kelime)
j = 0
i = 0
doğru_tahmin = 0
yanlış_tahmin = 0
x = len(kelime)
while yanlış_tahmin < 3 :
    b = input("Tahminini buraya gir:")

    if (b == "1"):
        print("OYUNDAN ÇIKTINIZ!")
        break



    if(b in kelime):
        print("Doğru tahmin tebrikler.")
        doğru_tahmin+=1
        c = kelime.index(b)
        del kelime[c]


    else:
        print("Daha düzgün tahminler vermelisin.")
        yanlış_tahmin+=1



    if (doğru_tahmin == x):
        print("AFERİM ADAMI KURTARDIN!")
        break



if(yanlış_tahmin==3):
    print("ADAM ÖLDÜ")

    i += 1
    j += 1
