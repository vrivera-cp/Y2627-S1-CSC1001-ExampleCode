class Cat:
    pass

def make_cat(name: str, age: int) -> Cat:
    the_new_object = Cat()

    the_new_object.name = name
    the_new_object.age = age

    return the_new_object

def rate_name(cat: Cat) -> int:
    rating = len(cat.name)
    return rating

mochi = make_cat('mochi', 4)

print(mochi.name)
print(mochi.age)

rating = rate_name(mochi)
print(rating)