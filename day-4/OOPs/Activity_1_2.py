# Create a class Book with attributes title, author, and a method to display details.


class Book:
    total_books = 0
    def __init__(self,title,author):
        self.title = title
        self.author = author
        Book.total_books += 1
        
    def display_details(self):
        print('Book Title : ', self.title)
        print('Author Name : ', self.author)
        
book1=Book('Half Girlfriend ', 'Chetan Bhagat')
book2=Book('2 States ', 'Chetan Bhagat')

book1.display_details()
book2.display_details()

print('Total Books : ', Book.total_books)