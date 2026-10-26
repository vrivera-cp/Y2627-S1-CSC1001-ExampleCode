class Cat:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    # Changes the functionality of printing objects, overriding
    # the "__repr__" method, if it exists.
    # as well as conversion with str()
    def __str__(self) -> str:
        return f'{self.name}, age {self.age}'

    # Changes the functionality of printing objects and the debugger
    # as well as conversion with repr() and as list elements
    def __repr__(self) -> str:
        return f'Cat(\'{self.name}\', {self.age})'


cat1 = Cat("mochi", 7)
cat2 = Cat("harvest", 5)

cats = [cat1, cat2, Cat("pearl", 4)]

print(cat1) # Uses __str__
print(cats) # Uses __repr__ for list elements

stringy_cat = str(cat2) #  Uses __str__
print(stringy_cat)

# "eval" evaluates a string of Python code
eval_number = eval("1 + 1")

eval_cat = eval('Cat("waffles", 8)')

# With a proper "__repr__" you can use it to clone objects
clone_maybe = eval(repr(cat1))
print(clone_maybe)