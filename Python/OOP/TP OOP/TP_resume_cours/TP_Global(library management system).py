import datetime as dt
import ttkbootstrap as ttk

#class creation

#book class

class Book:
    def __init__(self, title, author, pages, status):
        self.title = title.title()
        self.author = author.title()
        self.pages = pages 
        self.status = status
        
    def borrow_book(self):
        if self.status == "Available":
            self.status = "Borrowed"
            return
        else:
            return f"Book is already borrowed"

    def return_book(self):
        if self.status == "Borrowed":
            self.status = "Available"
            return
        else:
            return f"Book was not borrowed"
        
    def __str__(self):
         return f"Book('{self.title}', '{self.author}', {self.pages} pages, '{self.status}')"
    def __repr__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Status: {self.status}"
    

#user class

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
        
    def borrow_book(self, book):
        if book.status == "Available":
            book.status = "Borrowed"
            self.borrowed_books.append(book)
            print(f"Thank you for borrowing the book")
            return 
        else:
            return f"The book is unavailable"
    
    def return_book(self, book):
        if book.status == "Borrowed" and book in self.borrowed_books:
            book.status = "Available"
            self.borrowed_books.remove(book)
            print(f"Thank you for returning the book")
            return 
        else:
            return f"You did not borrow this book"
        
    def __str__(self):
        books = [book.title for book in self.borrowed_books]
        return f"{self.name},{books}"
    
    def __repr__(self):
        return f"User: {self.name}, Borrowed Books:" + ",".join([book.title for book in self.borrowed_books])
        
#library class

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        
    def search_book(self, title):
        title = title.title()
        for book in self.books:
            if book.title == title:
                return book
            return "Book not found"
        
    def display_available_books(self):
        for book in self.books:
            if book.status == "Available":
                print(book)
    
    def display_borrowed_books(self):
        for book in self.books:
            if book.status == "Borrowed":
                print(book)
                
    @staticmethod
    def total_borrowed_books(books):
        borrowed_books = [book for book in books if book.status == "Borrowed"]
        return len(borrowed_books)
                

#boorrowed book class

class BorrowedBook(Book):
    def __init__(self, title, author, pages, status, borrowing_date):
        super().__init__(title, author, pages, status)
        self.borrowing_date = dt.strptime(borrowing_date, "%Y-%m-%d")
        
    def __str__(self):
        return f"Borrowed Book('{self.title}', '{self.author}', {self.pages}, '{self.status}', borrowed on:'{self.borrowing_date}')"

    
#---------------------------------------Main---------------------------------------------------------

library = Library()

books = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", 180, "Available"),
    Book("To Kill a Mockingbird", "Harper Lee", 336, "Available"),
    Book("1984", "George Orwell", 328, "Available"),
    Book("The Catcher in the Rye", "J.D. Salinger", 224, "Available"),
    Book("The Lord of the Rings", "J.R.R. Tolkien", 1216, "Available"),
    Book("Pride and Prejudice", "Jane Austen", 432, "Available"),
    Book("The Hobbit", "J.R.R. Tolkien", 310, "Available"),
    Book("The Alchemist", "Paulo Coelho", 208, "Available"),
    Book("The Da Vinci Code", "Dan Brown", 454, "Available"),
    Book("The Hunger Games", "Suzanne Collins", 374, "Available")]

for book in books:
    library.add_book(book)
    
user1 = User("Adam Smith")

User.borrow_book(user1, books[0])
User.return_book(user1, books[0])

#---------------------------------------Functions------------------------------------------------------




#---------------------------------------Window---------------------------------------------------------

#window creation

app = ttk.Window()
app.title("Library Management System")
app.geometry("600x400")
style = ttk.style("morph")

#---------------------------------------Widgets---------------------------------------------------------

#input frame
input_frame = ttk.Frame(app)


#title label and entry field
title_label = ttk.Label(input_frame, text="Title", font=("Garamond", 12))
book_title = ttk.StringVar()
title_input = ttk.Entry(input_frame, text=book_title, font=("Garamond", 12))

title_label.grid(row=0, column=0, padx=10, pady=10)
title_input.grid(row=0, column=1, padx=10, pady=10)


#author label and entry field

author_label = ttk.Label(input_frame, text="Author", font=("Garamond", 12))
book_author = ttk.StringVar()
author_input = ttk.Entry(input_frame, text=book_author, font=("Garamond", 12))

author_label.grid(row=1, column=0, padx=10, pady=10)
author_input.grid(row=1, column=1, padx=10, pady=10)

#pages label and entry field

pages_label = ttk.Label(input_frame, text="Pages", font=("Garamond", 12))
book_pages = ttk.StringVar()
pages_input = ttk.Entry(input_frame, text=book_pages, font=("Garamond", 12))

pages_label.grid(row=2, column=0, padx=10, pady=10)
pages_input.grid(row=2, column=1, padx=10, pady=10)


#status label and entry field

status_label = ttk.Label(input_frame, text="Status", font=("Garamond", 12))
book_status = ttk.StringVar()
status_input = ttk.Entry(input_frame, text=book_status, font=("Garamond", 12))

status_label.grid(row=3, column=0, padx=10, pady=10)
status_input.grid(row=3, column=1, padx=10, pady=10)

#borrowing date label and entry field

