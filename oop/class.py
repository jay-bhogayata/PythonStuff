class CarShop:
    # Class attribute / variable
    # total_cars = 0
    # use __init__ to initialize the class attribute

    def __init__(self,start_cars):
        self.total_cars = start_cars

    # Method
    def add_car(self,num):
        self.total_cars += num
    

    def get_total_cars(self):
        return self.total_cars


# Create an instance of the Car class
acme = CarShop(10)
print(f"Total cars in acme now: {acme.get_total_cars()}") 
acme.add_car(10)
print(f"Total cars in acme now: {acme.get_total_cars()}")

# Create another instance of the Car class
tesla = CarShop(20)
print(f"Total cars in tesla: {tesla.get_total_cars()}")
tesla.add_car(10)
print(f"Total cars in tesla: {tesla.get_total_cars()}")


class Employee:
    company_name = "Age of Dragons, Inc."
    total_employees = 0

    def __init__(self, first_name, last_name, id, position, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.position = position
        self.salary = salary

        Employee.total_employees += 1

    def get_name(self):
        return f"{self.first_name} {self.last_name}"
    
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        for lib_book in self.books:
            if book.title == lib_book.title and book.author == lib_book.author:
                self.books.remove(lib_book)

    def search_books(self, search_string):
        results = []
        for book in self.books:
            if (
                search_string.lower() in book.title.lower()
                or search_string.lower() in book.author.lower()
            ):
                results.append(book)
        return results


# Create a library
library = Library("The Great Library")

# Create some books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Search for books
results = library.search_books("the")
for book in results:
    print(f"{book.title} by {book.author}")

# Remove a book
library.remove_book(book2)

# Search for books again
results = library.search_books("the")
for book in results:
    print(f"{book.title} by {book.author}")

