class Order:
    def __init__(self, customer, cart):
        self.customer = customer  
        self.cart = cart  

    def complete_order(self):
        total_amount = self.cart.get_total()

        if total_amount > 0:
            print(f"\nSipariş başarıyla oluşturuldu!")
            print(self.customer)  
            print("\nSipariş detayları:")
            self.cart.display_cart() 
            print(f"\nToplam Tutar: {total_amount} TL")
        else:
            print("\nSepet boş, sipariş oluşturulamadı!")