class Library:    
    def __init__(self, books):
        self.books = books
        self.no_of_books = len(books)
    @property
    def numberOfBooks(self):
        return len(self.books)
    
    def printAllBooks(self):
        for index, book in enumerate(self.books):
            print(f"{index + 1}. {book}")
    
    def addBook(self, book):
        self.books.append(book)

library1 = Library(['48 Laws Of Power', 'Atomic Habits', 'Rich Dad Poor Dad', 'Art Of Seduction'])
# print(library1.numberOfBooks)
library1.addBook('Physics Galaxy')
# print(library1.numberOfBooks)
# library1.printAllBooks()
