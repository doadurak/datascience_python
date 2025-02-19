# Görev 2: Kullanıcıdan bir sayı alarak 1’den o sayıya kadar olan sayıların toplamını hesaplayan program

def calculate_sum():
    number = int(input("Bir sayı girin: "))  # Kullanıcıdan bir sayı alınır
    total = 0  # Toplam değişkeni başlatılır

    # For döngüsü kullanarak toplam hesaplama
    for i in range(1, number + 1):
        total += i  # Her sayıyı toplama ekler

    print(f"1'den {number}'e kadar olan sayıların toplamı: {total}")  # Sonucu ekrana yazdırır

# Programı çalıştırma
if __name__ == "__main__":
    calculate_sum()