#Made this program to practice with creating classes and class instances

class Contact:

    #This is a class variable
    phone_number_length = 10

    def __init__(self, name="Nameless", phone_number="0000000000", address="Nowhere"):
        self.__name = name
        self.__phone_number = phone_number
        self.__address = address

    @property
    def name(self):
        print("property name get")
        return self.__name

    @property
    def phone_number(self):
        print("property phone_number get")
        return self.__phone_number

    @property 
    def address(self):
        print("property address get")
        return self.__address

    @name.setter
    def name(self, name):
        print("property name set:", name)
        self.__name = name

    @phone_number.setter
    def phone_number(self, phone_number):
        print("property phone_number set:", phone_number)
        self.__phone_number = phone_number
    
    @address.setter
    def address(self, address):
        print("property address set:", address)
        self.__address = address

    def __str__(self):
        return "Contact name: "+self.__name+"\nPhone number: "+self.__phone_number+"\nAddress: "+self.__address

    
class Book:

    @staticmethod
    def a_static_method():
        print("This is a static method.")


    def __init__(self, title="Untitled", author="Nobody", publish_year="Never published"):
        self.__title = title
        self.__author = author
        self.__publish_year = publish_year

    @property
    def title(self):
        print("property title get")
        return self.__title

    @property
    def author(self):
        print("property author get")
        return self.__author

    @property
    def publish_year(self):
        print("property publish_year get")
        return self.__publish_year

    @title.setter
    def title(self, title):
        print("property title set:", title)
        self.__title = title

    @author.setter
    def author(self, author):
        print("property author set:", author)
        self.__author = author

    @publish_year.setter
    def publish_year(self, publish_year):
        print("property publish_year set:", publish_year)
        self.__publish_year = publish_year

    def __str__(self):
        return "Title: " + self.__title + "\nAuthor: " + self.__author + "\nPublish year: " + self.__publish_year

class Manga(Book):

    def __init__(self, title="Untitled", author="Nobody", publish_year="Never published", genre="No genre"):
        super().__init__(title=title, author=author, publish_year=publish_year)
        self.__genre = genre

    @property
    def genre(self):
        return self.__genre
    
    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    def __str__(self):
        return super().__str__() + "\nGenre: " + self.__genre

my_friend_contact = Contact()
print(my_friend_contact.name, my_friend_contact.phone_number, my_friend_contact.address)

my_best_friend_contact = Contact(name = "Best friend", phone_number = "7777777777", address = "Earth")
print(my_best_friend_contact.name, my_best_friend_contact.phone_number, my_best_friend_contact.address)

my_book = Book()
print(my_book.title, my_book.author, my_book.publish_year)

my_favorite_book = Book(title = "Favorite book", author = "Me", publish_year = "0")
print(my_favorite_book.title, my_favorite_book.author, my_favorite_book.publish_year)

print("The Contact class has a class variable called phone_number_length:", Contact.phone_number_length)

print("The Book class has a static method: ")
Book.a_static_method()

print("The __str__ method demonstrated: ")
print("My best friend contact")
print(my_best_friend_contact)
print("My favorite book")
print(my_favorite_book)


print("Manga is the subclass of Book.")
my_favorite_manga = Manga(title = "One punch man", author = "Yusuke Murata", publish_year = "2013", genre = "Action, Comedy, Superhero")
print(my_favorite_manga)