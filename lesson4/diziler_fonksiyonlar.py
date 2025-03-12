def en_buyuk_ve_en_kucuk(sayilar):

    en_buyuk = max(sayilar)
    en_kucuk = min(sayilar)
    return en_buyuk, en_kucuk
sayilar = []
for i in range(5):
    sayi = int(input(f"{i+1}. sayıyı girin: "))
    sayilar.append(sayi)
en_buyuk, en_kucuk = en_buyuk_ve_en_kucuk(sayilar)
print(f"Girdiğiniz sayılar: {sayilar}")
print(f"En büyük sayı: {en_buyuk}")
print(f"En küçük sayı: {en_kucuk}")