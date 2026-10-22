class Cat:
    # With methods, the calling object is passed in
    # automatically passed in as the first argument
    def rate_name(self) -> int:
        # "self" is just a parameter name, it's not special
        # keyword
        rating = len(self.name)
        return rating

def make_cat(name: str, age: int) -> Cat:
    cat = Cat()
    
    cat.name = name
    cat.age = age

    return cat

def rate_name(cat: Cat) -> int:
    rating = len(cat.name)
    return rating

our_cat = make_cat("Mochi", 3)

rating = rate_name(our_cat) # Functions are "Third Person"
rating = our_cat.rate_name() # Methods are "First Person"

print(rating)
