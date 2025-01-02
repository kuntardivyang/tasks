# Class-Based Assignment:
# Create a Library class to manage a collection of books. Include methods to:
# Add a book.
# Remove a book.
# Display all books.

class Library:
    
    def __init__(self):
        self.books = []
        
    def add_book(self,name):
        self.books.append(name)
        print(name, " Book Added")
        
    def remove_book(self,name):
        self.books.remove(name)
        print(name, " Book removed")
        
    def display_books(self):
        print('List of Books : ',self.books)
        
        
library_object = Library()

library_object.add_book('The Murder Mystery')
library_object.add_book('Crime And Injustice')
library_object.add_book('White Nights')
library_object.add_book('Percy Jackson')

library_object.remove_book('Percy Jackson')

library_object.display_books()


