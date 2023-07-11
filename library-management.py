class Libraray_management():
    def __init__(self, list1):
        self.all_books = list1
        self.available_books = list1[:]
        self.taken_books = {}

    def all_books_in_lib(self):
        for books in self.all_books:
            print(books)

    def available_books_in_lib(self):
        for books in self.available_books:
            print(books)

    def borrow(self, name, book_name):
        if book_name not in self.all_books:
            print("Book is not available")
            return
        if book_name in self.available_books:
            self.taken_books.update({book_name: name})
            self.available_books.remove(book_name)
        else:
            print("Book is already taken by " + self.taken_books[book_name])

    def return_the_book(self, book):
        if book not in self.taken_books:
            print("It is not taken")
        if book in self.taken_books:
            del self.taken_books[book]
            self.available_books.append(book)


if __name__ == '__main__':

    lib = Libraray_management(["Secret", "Atomic Habits", "Escape Matrix", "Looped Life", "Trillionare mindset"])

    print("select options")
    while True:
        print("1.All books")
        print("2.Available books")
        print("3.Borrow")
        print("4.Return a book")
        print("5.quit")
        user_input = int(input("Enter here"))
        if user_input == 1:
            lib.all_books_in_lib()
        elif user_input == 2:
            lib.available_books_in_lib()
        elif user_input == 3:
            name = input("User name")
            book_name = input("Enter Book Name")
            lib.borrow(name, book_name)
        elif user_input == 4:
            book = input("Enter book name")
            lib.return_the_book(book)
        elif user_input == 5:
            break
        else:
            print("Invalid choice")
