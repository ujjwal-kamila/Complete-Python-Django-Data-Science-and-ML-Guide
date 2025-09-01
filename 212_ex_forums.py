# 212. Example - Creating Instances of the Forum, User, and Post Classes


# Example - Creating Library, Book, and Member Classes

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False   


class Library:
    def __init__(self):
        self.members = []
        self.books = []

    def register_member(self, name, member_id):
        member = Member(name, member_id)
        self.members.append(member)
        return member

    def add_book(self, title, author, isbn):
        book = Book(title, author, isbn)
        self.books.append(book)
        return book

    def borrow_book(self, member: Member, book: Book):
        if not book.is_borrowed:
            book.is_borrowed = True
            print(f"{member.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already borrowed!")


# Create library object
library = Library()

# Register members
m1 = library.register_member("Ujjwal", "MK3171")
m2 = library.register_member("Dip", "MK8618")

# Add books
b1 = library.add_book("1984", "George Orwell", "ISBN123")
b2 = library.add_book("The Hobbit", "J.R.R. Tolkien", "ISBN456")

# Show members and books
print(library.members)  
print(library.books)    

# Borrow books
library.borrow_book(m1, b1)
library.borrow_book(m2, b1)
