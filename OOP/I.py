class className:
    pass
    #Class Atribut

    #__init__()

    #Methods

#default argument and update instances
class Circle:

    def __init__(self, radius=5):
        self.radius = radius


my_circle = Circle()
print(my_circle.radius)

your_circle = Circle(8)
print(your_circle.radius)

#default argument
class Circle:

    def __init__(self, radius=5, color): # This throws an error
        self.radius = radius
        self.color = color


my_circle = Circle(7, "Blue")
print(my_circle.radius)
print(my_circle.color)

#update instances
class Book:

    def __init__(self):
        self.books = []

my_books = Book()
my_books.books = ["Pride and Prejudice", "Metamorphosis"]
print(my_books.books)
my_books.books[1] = "ROmeo"
print(my_books.books)

#mini project class bacteria
#This is a sample code for the Bacteria class:
class Bacteria:
	def __init__(self, x, y, shape, resistant, is_gram_positive):
		self.x = x
		self.y = y
		self.shape = shape
		self.resistant = resistant         # True if resistant to antibiotics; otherwise False.
		self.is_gram_positive = is_gram_positive

#These are three sample instances:
bacteria1 = Bacteria(50, 60, "coccus", True, True)
bacteria2 = Bacteria(50, 260, "bacillus", False, False)
bacteria3 = Bacteria(150, 200, "tetrad", True, True)

# Fix the errors
# Donut.py

class Donut
        def _ini__(flavor, toppings, filling, size):
                self.flavor = flavor
                self.toppings = toppings
                self.filling = filling
                size = self.size

        #solution
# class Donut:
        # def __ini__(self,flavor, toppings, filling, size):
        #         self.flavor = flavor
        #         self.toppings = toppings
        #         self.filling = filling
        #         self.size = self.size

# Customer.py

class Customer:
	def _init_(self, name, age address, favorite_dessert)
		self.name = name
		self.age = age
		self.address = address
		favorite_dessert= self.favorite_dessert

        # solution
        # def __init__(self, name, age address, favorite_dessert)
		# self.name = name
		# self.age = age
		# self.address = address
		# self.favorite_dessert= favorite_dessert
# Cake.py

class Cake:
	__init__(self, flavor, price, quality):
		self.flavor = flavor
		self.price = price
		self.quality = quality

        #solution
    # def __init__(self, flavor, price, quality):
    #     self.flavor = flavor
    #     self.price = price
    #     self.quality = quality


# class atribute / global variable
class Movie:
    id = 1
    #Access class aribute inside instances atribut
    id_counter = 1
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
        #add counter to acces from class atribute
        self.ids = Movie.id_counter

        Movie.id_counter += 1

#access class atribute
my_movie = Movie.id
print(my_movie)
print(Movie.id)

#acces class atribute incremental
my_movies = Movie("Juon", 1993)
print(my_movies.ids)

your_movies = Movie("Hercules", 1994)
print(your_movies.ids)

We_movies = Movie("Testing", 1995)
print(We_movies.ids)

# Modify Class Atribute
class Circle:
    # class atribute
    radius = 5

    def __init__(self, color):
        self.color = color

print(Circle.radius)

my_circle = Circle("Blue")
your_circle = Circle("Red")

print(my_circle.radius) #5
print(your_circle.radius) #5

#update class atribute
my_circle.radius = 10
print(my_circle.radius) #10

your_circle.radius = 20
print(your_circle.radius) #20

#What is the value of the class attribute attr1 after this sequence of statements?
class A:

    attr1 = 5

    def __init__(self):
        A.attr1 += 1

a1 = A()
a2 = A()
A.attr1 = 26
a3 = A()
print(A.attr1) # Output?

