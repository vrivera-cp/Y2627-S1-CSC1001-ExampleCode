import random
from pathlib import Path

def summation(numbers: list[int]) -> int:
    # 1. Initialize Accumulator
    running_total = 0

    # 2. Iterate over items
    for number in numbers:
        # 3. Combine each element into the accumulator
        running_total = running_total + number

    # 4. Return the accumulator
    return running_total

def largest_number(numbers: list[int]) -> int | None:
    # 1. Initialize Accumulator
    largest = None

    # 2. Iterate over items
    for number in numbers:
        # 3. Combine each element into the accumulator
        if largest is None or number > largest:
            largest = number

    # 4. Return the accumulator
    return largest

def count_letter_occurrences(text: str) -> int:
    # 1. Initialize Accumulator
    count = 0

    # 2. Iterate over items
    for character in text:
        # 3. Combine each element into the accumulator
        if character == 'a':
            count = count + 1

    # 4. Return the accumulator
    return count

if __name__ == '__main__':
    numbers = [random.randint(0, 9) for i in range(5)]

    text = 'banana'

    print(count_letter_occurrences(text))

    text = Path('alice.txt').read_text()
    print(count_letter_occurrences(text))
