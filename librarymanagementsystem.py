#test1
class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        if not books:
            print("No books available." if language == "1" else "Mevcut kitap yok.")
        else:
            for book in books:
                book_info = book.split(",")
                print(f"Title: {book_info[0]}, Author: {book_info[1]}, Year: {book_info[2]}, Pages: {book_info[3]}" if language == "1" else f"Başlık: {book_info[0]}, Yazar: {book_info[1]}, Yıl: {book_info[2]}, Sayfalar: {book_info[3]}")

    def add_book(self):
        title = input("Enter book title: " if language == "1" else "Kitap başlığını girin: ").title()
        author = input("Enter book author: " if language == "1" else "Kitap yazarını girin: ").title()
        release_year = input("Enter release year: " if language == "1" else "Yayın yılını girin: ")

        if len(release_year) != 4:
            print("Please enter a 4-digit number." if language == "1" else "Lütfen 4 haneli bir sayı girin.")
            return

        try:
            released_year = int(release_year)
        except ValueError:
            print("Invalid input! Use an integer for the release year." if language == "1" else "Geçersiz giriş! Yayın yılı için bir tamsayı kullanın.")
            return

        pages = input("Enter page count: " if language == "1" else "Sayfa sayısını girin: ")
        book_info = f"{title},{author},{release_year},{pages}\n"
        print("Please wait..." if language == "1" else "Lütfen bekleyin.")
        self.file.write(book_info)
        print("Book added successfully." if language == "1" else "Kitap başarıyla eklendi.")

    def remove_book(self):
        title = input("Enter the title of the book you want to remove: " if language == "1" else "Kaldırmak istediğiniz kitabın başlığını girin: ").title()
        self.file.seek(0)
        books = self.file.read().splitlines()
        updated_books = [book for book in books if title not in book]
        self.file.seek(0)
        self.file.truncate()
        for i in updated_books:
            self.file.write(i + '\n')
        if title not in books:
            print("Book not found. Please check the title and try again." if language == "1" else "Kitap bulunamadı. Lütfen başlığı kontrol edin ve tekrar deneyin.")
        else:
            print("Book removed successfully." if language == "1" else "Kitap başarıyla kaldırıldı.")

    def all_remove_book(self):
        correct_password = 1234
        entered_password = int(input("If you want to delete all books, please enter the password: " if language == "1" else "Tüm kitapları silmek istiyorsanız, lütfen şifreyi girin: "))
        if entered_password == correct_password:
            self.file.seek(0)
            self.file.truncate()
            print("All books deleted." if language == "1" else "Tüm kitaplar silindi.")
        else:
            print("Wrong password!" if language == "1" else "Yanlış şifre!")

    def change_language(self):
        global language
        print("1) English")
        print("2) Türkçe")
        language = input("Choose language (1/2): " if language == "1" else "Dil seçiniz (1/2): ")
        if language == "1":
            print("Language set to English.")
        elif language == "2":
            print("Dil Türkçe olarak ayarlandı.")
        else:
            print("Invalid choice. Please enter 1 or 2." if language == "1" else "Geçersiz seçim. Lütfen 1 veya 2 girin.")

def print_menu():
    print("*** MENU ***" if language == "1" else "*** MENÜ ***")
    print("1) List Books" if language == "1" else "1) Kitapları Listele")
    print("2) Add Book" if language == "1" else "2) Kitap Ekle")
    print("3) Remove Book" if language == "1" else "3) Kitap Kaldır")
    print("4) Change Language" if language == "1" else "4) Dil Değiştir")
    print("5) Remove All Books" if language == "1" else "5) Tüm Kitapları Kaldır")
    print("q) Exit" if language == "1" else "q) Çıkış")

language = "2"
lib = Library()

while True:
    print_menu()
    choice = input("Make your choice (1/2/3/4/5/q): " if language == "1" else "Seçiminizi yapın (1/2/3/4/5/q): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        lib.change_language()
    elif choice == "5":
        lib.all_remove_book()