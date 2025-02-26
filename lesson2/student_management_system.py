import json

class StudentManagement:
    def __init__(self):
        self.students = {}
        self.file_name = "students.json"
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                self.students = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.students = {}

    def save_data(self):
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(self.students, file, ensure_ascii=False, indent=4)

    def add_student(self):
        try:
            student_id = int(input("Öğrenci Numarası: "))
        except ValueError:
            print("Hata: Öğrenci numarası sadece rakamlardan oluşmalıdır!")
            return
        
        if str(student_id) in self.students:
            print("Bu numaraya sahip öğrenci zaten mevcut!")
            return
        
        first_name = input("Ad: ").strip()
        if not all(x.isalpha() or x.isspace() for x in first_name):
            print("Hata: Ad yalnızca harflerden ve boşluklardan oluşmalıdır!")
            return
        
        last_name = input("Soyad: ").strip()
        if not all(x.isalpha() or x.isspace() for x in last_name):
            print("Hata: Soyad yalnızca harflerden ve boşluklardan oluşmalıdır!")
            return
        
        department = input("Bölüm: ")
        
        try:
            gpa = float(input("Not Ortalaması: "))
        except ValueError:
            print("Hata: Not ortalaması yalnızca sayısal bir değer olmalıdır!")
            return
        
        self.students[str(student_id)] = {"Ad": first_name, "Soyad": last_name, "Bölüm": department, "Not Ortalaması": gpa}
        self.save_data()
        print("Öğrenci başarıyla eklendi!")

    def list_students(self):
        if not self.students:
            print("Sistemde kayıtlı öğrenci bulunmamaktadır.")
        else:
            for student_id, info in self.students.items():
                print(f"Numara: {student_id}, Ad: {info['Ad']}, Soyad: {info['Soyad']}, Bölüm: {info['Bölüm']}, Not Ortalaması: {info['Not Ortalaması']}")

    def view_student(self):
        student_id = input("Görüntülemek istediğiniz öğrencinin numarasını girin: ")
        if student_id in self.students:
            info = self.students[student_id]
            print(f"Ad: {info['Ad']}, Soyad: {info['Soyad']}, Bölüm: {info['Bölüm']}, Not Ortalaması: {info['Not Ortalaması']}")
        else:
            print("Bu numaraya sahip öğrenci bulunamadı!")

    def update_student(self):
        student_id = input("Güncellemek istediğiniz öğrencinin numarasını girin: ")
        if student_id in self.students:
            print("Mevcut bilgiler: ")
            self.view_student()
            
            first_name = input("Yeni Ad: ").strip()
            if first_name and not all(x.isalpha() or x.isspace() for x in first_name):
                print("Hata: Ad yalnızca harflerden ve boşluklardan oluşmalıdır!")
                return
            
            last_name = input("Yeni Soyad: ").strip()
            if last_name and not all(x.isalpha() or x.isspace() for x in last_name):
                print("Hata: Soyad yalnızca harflerden ve boşluklardan oluşmalıdır!")
                return
            
            department = input("Yeni Bölüm: ") or self.students[student_id]["Bölüm"]
            
            try:
                gpa = float(input("Yeni Not Ortalaması: ")) if input("Yeni Not Ortalaması girilecek mi? (E/H): ").lower() == 'e' else self.students[student_id]["Not Ortalaması"]
            except ValueError:
                print("Hata: Not ortalaması yalnızca sayısal bir değer olmalıdır!")
                return
            
            self.students[student_id] = {"Ad": first_name or self.students[student_id]["Ad"], "Soyad": last_name or self.students[student_id]["Soyad"], "Bölüm": department, "Not Ortalaması": gpa}
            self.save_data()
            print("Öğrenci bilgileri güncellendi!")
        else:
            print("Bu numaraya sahip öğrenci bulunamadı!")

    def menu(self):
        while True:
            print("\nÖĞRENCİ YÖNETİM SİSTEMİ")
            print("1. Öğrenci Ekle")
            print("2. Öğrencileri Listele")
            print("3. Öğrenci Görüntüle")
            print("4. Öğrenci Güncelle")
            print("5. Çıkış")
            choice = input("Seçiminizi yapın: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.list_students()
            elif choice == "3":
                self.view_student()
            elif choice == "4":
                self.update_student()
            elif choice == "5":
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz seçim, tekrar deneyin!")

if __name__ == "__main__":
    system = StudentManagement()
    system.menu()