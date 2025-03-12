sayi = int(input("Bir sayı girin: "))
toplam_for = 0
for i in range(1, sayi + 1):
    toplam_for += i
toplam_while = 0
i = 1
while i <= sayi:
    toplam_while += i
    i += 1
print(f"For döngüsü ile toplam: {toplam_for}")
print(f"While döngüsü ile toplam: {toplam_while}")