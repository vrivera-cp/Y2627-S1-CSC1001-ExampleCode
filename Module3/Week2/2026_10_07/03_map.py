def name_lengths(input_words: list[str]) -> list[int]:
    # 2
    word_lengths = []

    # 3
    for word in input_words:
        word_length = len(word)
        word_lengths.append(word_length)

    # 4
    return word_lengths

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

word_lengths = name_lengths(words)

print(words)
print(word_lengths)