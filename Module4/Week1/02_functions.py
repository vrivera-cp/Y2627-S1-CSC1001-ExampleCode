class Cat:
    pass

def rate_name(cat: Cat) -> int:
    rating = len(cat.name)
    return rating

def clone_cat(cat: Cat) -> Cat:
    clone = Cat()
    clone.name = cat.name
    return clone

mochi = Cat()
mochi.name = 'mochi'

rating = rate_name(mochi)
print(rate_name(mochi))

morechi = clone_cat(mochi)
print(morechi.name)

print(mochi == morechi)
print(mochi is morechi)

harvest = Cat()

rate_name(harvest) # failure because harvest doesn't have a name