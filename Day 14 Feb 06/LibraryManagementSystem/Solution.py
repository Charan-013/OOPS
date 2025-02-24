class Book:
    def __init__(self,title,author,isbn,available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def getTitle(self):
        return self.title

    def isAvailable(self):
        return self.available
    
class Library:
    def __init__(self,list):
        self.books = list

    def addBook(self,book):
        self.books.append(book)

    def removeBook(self,isbn):
        for ele in self.books[:]:
            if isbn == ele.isbn:
                del ele
                return True
        return False
        

    def searchBookByTitle(self,title):
        for ele in self.books:
            if ele.title == title:
                return ele
        

    def listAllBooks(self):
        return self.books

def main():
    # Create books (including one unavailable)
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "ISBN001", True)
    book2 = Book("1984", "George Orwell", "ISBN002", True)
    book3 = Book("Moby Dick", "Herman Melville", "ISBN003", False)
    library = Library([])
    # Test adding books
    library.addBook(book1)
    library.addBook(book2)
    library.addBook(book3)
    if len(library.listAllBooks()) != 3:
        print("Error: Not all books added.")
    # Test listing all books
    print("Listing all books:")
    for b in library.listAllBooks():
        print(f"Title: {b.getTitle()}, Available: {b.isAvailable()}")
    # Test search method (existing and non-existing)
    found = library.searchBookByTitle("1984")
    print("Found '1984':", found is not None)
    not_found = library.searchBookByTitle("Nonexistent")
    print("Search for nonexistent title:", not_found is None)
    # Test removal (successful and failure)
    removed_success = library.removeBook("ISBN002")
    print("Removed ISBN002:", removed_success)
    removed_failure = library.removeBook("ISBN999")
    print("Attempted removal of non-existent ISBN:", removed_failure)
    # Final listing check
    print("Books remaining:")
    for b in library.listAllBooks():
        print(b.getTitle())
if __name__ == '__main__':
    main()