class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.update_stock(quantity):  
            if product.name in self.items:
                self.items[product.name]['quantity'] += quantity
            else:
                self.items[product.name] = {'product': product, 'quantity': quantity}
        else:
            print(f"Yetersiz stok: {product.name}")

    def remove_product(self, product, quantity):
               # Sepetteki ürünü kontrol et
        if product.name in self.items:
            if self.items[product.name]['quantity'] >= quantity:
                self.items[product.name]['quantity'] -= quantity
                # Eğer ürün miktarı sıfırsa, ürünü sepetten tamamen çıkarıyoruz
                if self.items[product.name]['quantity'] == 0:
                    del self.items[product.name]
                print(f"{quantity} adet {product.name} sepetten çıkarıldı.")
            else:
                print(f"Sepette yeterli {product.name} yok.")
        else:
            print(f"{product.name} sepetinizde bulunmamaktadır.")

    def display_cart(self):
        if not self.items:
            print("Sepetiniz boş.")
            return
        print("\nSepetiniz:")
        for item in self.items.values():
            print(f"{item['product'].name} - {item['quantity']} adet - {item['product'].price * item['quantity']} TL")

    def get_total(self):
        return sum(item['product'].price * item['quantity'] for item in self.items.values())

    def view_cart(self):
        if not self.items:
            print("Sepetiniz boş.")
            return
        print("\nSepetiniz:")
        for item in self.items.values():
            print(f"{item['product'].name}: {item['quantity']} adet, {item['product'].price * item['quantity']} TL")
        print(f"Toplam fiyat: {self.get_total()} TL")
