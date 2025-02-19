# Görev 3: 1 ile 100 arasındaki çift sayıları ekrana yazdıran program

def print_even_numbers():
    # 1 ile 100 arasındaki çift sayıları yazdır
    for number in range(2, 101, 2):  # 2'den başlayıp 2'şer artırarak 100'e kadar gider
        print(number, end=" ")  # Sayıları yan yana yazdır

# Programı çalıştırma
if __name__ == "__main__":
    print_even_numbers()