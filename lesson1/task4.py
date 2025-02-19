# Görev 4: Kullanıcıdan alınan bir metni döngü kullanarak ters çeviren program

def reverse_text():
    text = input("Bir metin girin: ")  # Kullanıcıdan metin alınır
    reversed_text = ""  # Boş bir ters metin değişkeni oluşturulur

    # Döngü ile metni tersten ekleme
    for char in text:
        reversed_text = char + reversed_text  # Karakteri en başa ekle

    print(f"Ters çevrilmiş metin: {reversed_text}")  # Sonucu ekrana yazdır

# Programı çalıştırma
if __name__ == "__main__":
    reverse_text()
