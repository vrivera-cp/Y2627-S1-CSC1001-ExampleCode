items = [1, 2, 3, 4]

mapped = [item * 2 for item in items]


filtered = [item for item in items if item % 2 == 0]

words = [
    "pikachu",
    "squirtle",
    "charmander",
    "bulbasaur",
    "onyx",
    "abra",
    "jynx",
    "mew",
]

filtered = [word for word in words if len(word) < 5]

mapped = [len(word) for word in words]

print(filtered)
print(mapped)