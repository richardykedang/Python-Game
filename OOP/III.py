#public and non public atribute
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

my_car = Car("Porsche", "91Carera", 2020)
print(my_car.year)

my_car.year = 2500
print(my_car.year)

#Non public atruibute = atribute yg tdk bisa di akses atau modified diluar dri kelasnya sendiri

# - Explain why an attribute is never really private in Python. In your explanation, please explain the process of name mangling with an example.

# - Make the following attributes "protected" in the Book class and submit the final version of the class:

#       * num_pages

#       * publisher

#       * ISBN

class Book:

	def __init__(self, title, author, num_pages, ISBN, publisher):
		self.title = title
		self.author = author
		self._num_pages = num_pages
		self.ISBN = ISBN
		self._publisher = publisher

class BaseballBat:

	def __init__(self, length, weight, model):
		self.length = length
		self._weight = weight
		self.__model = model


baseball_bar = BaseballBat(42, 32, "MZM110")
print(baseball_bar._weight)
#32
print(baseball_bar._BaseballBat__model)
#'MZM110'

#getter and setter
# getter and setter di pakai ketika atribut yg digunakan merupakan atribut non public
#Getter
class Movie:

    def __init__(self, title, rating):
        self._title = title
        self.rating = rating

    def get_title(self):
        return self._title
#erate instance movie
my_movie = Movie("Godfather", 4.8)
print(my_movie.get_title())

#Setter # update value non public atribute
class Dog:

    def __init__(self, name, age):
        self._name = name
        self.age = age

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else:
            print(" Please Enter a valid name")

my_dog = Dog("Nora", 4)
print("My dog name is : ", my_dog.get_name())

my_dog.set_name("Norita")
print("My Dog New Name is : ", my_dog.get_name())
# negative case jika nonaphabetic
my_dog.set_name("Norita123")
#kena validasi
print("My Dog New Name is : ", my_dog.get_name())

# gtter setter contoh 2 list non public
class Backpack:

    def __init__(self):
        self._item = []

    def get_item(self):
        return self._item

    def set_item(self, new_items):
        if isinstance(new_items, list):
            self._item = new_items
        else:
            print("Please enter a valid of list item")

my_backpack = Backpack()
print(my_backpack.get_item())
my_backpack.set_item(["kaos", "celana"])
print(my_backpack.get_item())
#negative case
my_backpack.set_item("handuk")
print(my_backpack.get_item())

# getter setter contoh 3 float non public
class Circle:

    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, float) and new_radius > 0 :
            self._radius = new_radius

        else:
            print("Please enter a valid value for the radius")

my_circle = Circle(23.3)
print(my_circle.get_radius())
my_circle.set_radius(20)
print(my_circle.get_radius())

# getter setter contoh 4 with class atribute
class Circle:

    VALID_COLORS = ("Red", "Blue", "Green")

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, int) and new_radius > 0:
            self._radius = new_radius
        else:
            print("Please enter a valid radius.")

    radius = property(get_radius, set_radius)

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            print("Please enter a valid color.")

    color = property(get_color, set_color)


my_circle = Circle(10, "Blue")

# Radius
print("radius : ", my_circle.radius)
my_circle.radius = 16
print(my_circle.radius)

my_circle.radius = 0
print(my_circle.radius)

# Color
print(my_circle.color)
my_circle.color = "Red"
print(my_circle.color)

my_circle.color = "White"
print(my_circle.color)
