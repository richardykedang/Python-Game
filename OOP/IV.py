#Property Decorators
#sama seperti getter and setter cuma di persingkat dgn decorator menggunakan symbol @
class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        print("Calling the getter...")
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        print("Calling the setter...")
        if 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print("Please enter a valid rating.")


favorite_movie = Movie("Titanic", 4.3)
print(favorite_movie.rating)

favorite_movie.rating = 4.5
print(favorite_movie.rating)

favorite_movie.rating = -5.6 # Invalid value.
print(favorite_movie.rating)

# Contoh 2 backpack class decorator properties
class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("Please enter a valid list of items.")


my_backpack = Backpack()
print(my_backpack.items)

my_backpack.items = ["Water Bottle", "Sleeping Bag"]
print(my_backpack.items)

my_backpack.items = "Hello, World!" # Invalid value.
print(my_backpack.items)
