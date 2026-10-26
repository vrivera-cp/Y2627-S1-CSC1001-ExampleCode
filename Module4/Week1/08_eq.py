class Cat:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    # Modifies the behavior of the "==" operator with Cat objects
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cat):
            # If the other object is not a cat, don't check its attributes
            return False
        # Two cats are "equal" if they have the same name and age
        return self.age == other.age and self.name == other.name


a = Cat("mochi", 7) # Instantiation
b = Cat("mochi", 7) # Instantiation
c = a # Alias

print(a is b)
print(a is c)
print(a == b) # Calls a.__eq__()
print(a == c) # Calls a.__eq__()