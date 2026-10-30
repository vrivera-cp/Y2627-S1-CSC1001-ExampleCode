class Unknown:
    def __init__(self, attribute: list[list[int]]) -> None:
        self.attribute = attribute

class Another:
    def __init__(self, attribute: list[dict[str, Unknown]]) -> None:
        self.attribute = attribute

# Initialize values needed to make an "Unknown" instance
a = [1, 2, 3]
b = [4, 5, 6, 7]

unknown_attribute = [a, b]

# Instantiate the "Unknown" class
unknown_object = Unknown(unknown_attribute)

# Initialize values needed to make an "Another" instance
c = {"unknown": unknown_object}
d = {"some other string": Unknown([[10, 9, 3, 4], [1, 2, 3], [4, 5, 6]])}

another_attribute = [c, d]

# Instantiate the "Another" class
another_object = Another(another_attribute)

# Accesses the "7" from the list created on line 11
the_value = another_object.attribute[0]["unknown"].attribute[1][3]

print(the_value)