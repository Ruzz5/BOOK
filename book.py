class Book:
    def __init__(self):
        self.title = input("Enter book title: ")
        self.author = input("Enter author name: ")
        self.pyear = input("Enter publication year: ")
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print("Borrowed successfully.")
        else:
            print("The book is unavailable.")

    def return_book(self):
        if not self.available:
            self.available = True
            print("You returned the book successfully.")
        else:
            print("The book is already available.")

    def display(self):
        print(f"""\n--- BOOK DETAILS ---
                \nTitle: {self.title}
                \nAuthor: {self.author}
                \nYear Published: {self.pyear}""")

        if self.available:
            print("Status: Available")
        else:
            print("Status: Not Available")

    def Det(self):
        print("""\n1 Borrow")
                \n2 Return
                \n3 Display
                \n4 Exit""")

        option = input("Enter choice: ")

        match option:
            case "1":
                self.borrow()
                self.Det()
            case "2":
                self.return_book()
                self.Det()
            case "3":
                self.display()
                self.Det()
            case "4":
                print("Thank you.")
            case _:
                print("Invalid choice.")
                self.Det()

book = Book()
book.Det()
