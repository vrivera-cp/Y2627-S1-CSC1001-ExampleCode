def filter_short_words(input_words: list[str]) -> list[str]:
    # 2
    filtered = []

    # 3
    for word in input_words:
        if len(word) < 5:
            filtered.append(word)

    # 4
    return filtered

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

filtered_words = filter_short_words(words)

print(filtered_words)