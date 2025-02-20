# Bölüm 1: Operatörler ile İşlemler
# Görev 1: Kullanıcıdan iki sayı alıp temel matematiksel işlemleri yapan program

def mathematical_operations():
    number1 = float(input("Birinci sayıyı girin: "))  # Kullanıcıdan birinci sayı alınıyor
    number2 = float(input("İkinci sayıyı girin: "))  # Kullanıcıdan ikinci sayı alınıyor
    
    print(f"Toplama: {number1} + {number2} = {number1 + number2}")  # Toplama işlemi
    print(f"Çıkarma: {number1} - {number2} = {number1 - number2 }")  # Çıkarma işlemi
    print(f"Çarpma: {number1} * {number2} = {number1 * number2}")  # Çarpma işlemi
    print(f"Bölme: {number1} / {number2} = {number1/ number2}")  # Bölme işlemi
    print(f"Mod alma: {number1} % {number2} = {number1 % number2}")  # Mod alma işlemi
    print(f"Üs alma: {number1} ** {number2} = {number1 ** number2}")  # Üs alma işlemi

if __name__ == "__main__":  # Program çalıştırıldığında ana fonksiyon çağrılır
    mathematical_operations()
