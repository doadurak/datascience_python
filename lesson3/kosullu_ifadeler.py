
sayi = float(input("Bir sayı girin: "))

if sayi < 0:
    print("Negatif sayı girdiniz!")
else:
   
    if sayi % 2 == 0:
        print(f"{sayi} sayısı çifttir.")
    else:
        print(f"{sayi} sayısı tektir.")