#Made this program to practice with creating classes and class instances

class Contact:
    
    def __init__(self, name="Nameless", phone_number="0000000000", address="Nowhere"):
        self.name = name
        self.phone_number = phone_number
        self.address = address

class Book:

    def __init__(self, title="Untitled", author="Nobody", publish_year="Never published"):
        self.title = title
        self.author = author
        self.publish_year = publish_year


my_friend_contact = Contact()
print(my_friend_contact.name, my_friend_contact.phone_number, my_friend_contact.address)

my_best_friend_contact = Contact(name = "Best friend", phone_number = "7777777777", address = "Earth")
print(my_best_friend_contact.name, my_best_friend_contact.phone_number, my_best_friend_contact.address)

my_book = Book()
print(my_book.title, my_book.author, my_book.publish_year)

my_favorite_book = Book(title = "Favorite book", author = "Me", publish_year = "0")
print(my_favorite_book.title, my_favorite_book.author, my_favorite_book.publish_year)

