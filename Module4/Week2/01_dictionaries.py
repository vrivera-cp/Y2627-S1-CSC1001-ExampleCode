# Defining a dictionary
populations = {
    'emperor penguin': 22800,
    'tiger': 5700,
    'rhinoceros': 6700,
}

# Accessing values
print(populations['emperor penguin'])

key = 'tiger'
print(populations[key])

# Updating a Value
populations['tiger'] = populations['tiger'] + 300

# Inserting a value
populations['wolf'] = 250000
print(populations)

# Removing a value
del populations['wolf']
print(populations)

# Sequences from a dictionary
keys = list(populations.keys())
values = list(populations.values())

# Iteration
for key in populations:
    print(key)
    print(populations[key])

# Functions and Dictionaries
def potentially_endangered(populations: dict[str, int], threshold: int) -> list[str]:
    output = []

    for key in populations:
        if populations[key] < threshold:
            output.append(key)

    return output

result = potentially_endangered(populations, 10000)

print(result)

# Accessing invalid key
print(populations['wolf'])