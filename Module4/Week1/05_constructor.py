class Cat:
    # The special __init__ method changes the
    # call used to instantiate the class
    def __init__(self, name: str, age: int) -> None:
        # With __init__, a reference to newly created
        # object is automatically passed as the
        # first argument when called
        self.name = name
        self.age = age

# Calling "Cat" automatically calls the
# class's __init__ function
cat1 = Cat("mochi", 7)
cat2 = Cat("harvest", 5)

cats = [cat1, cat2, Cat("pearl", 4)]

print(cats)
