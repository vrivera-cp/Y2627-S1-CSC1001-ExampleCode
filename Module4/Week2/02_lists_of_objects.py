from classes import AnimalSpecies

# List of objects
animal_species = [
    AnimalSpecies('emperor penguin', 'aptenodytes forsteri', 22800),
    AnimalSpecies('tiger', 'panthera tigris', 5700),
    AnimalSpecies('black rhinoceros', 'diceros bicornis', 6700),
]

# Accessing specific attributes
print(animal_species[0].population)
print(animal_species[2].scientific_name)

tiger_index = 1
print(animal_species[tiger_index].name)

# Appending
wolves = AnimalSpecies('wolf', 'canis lupis', 250000)
animal_species.append(wolves)

# Loop over items
for species in animal_species:
    print(species)

# Loop over indexes and display formatted information
for i in range(len(animal_species)):
    species = animal_species[i]
    print(f'{i}:\t{species.name.title()} ({species.scientific_name.title()})\n\t\tPopulation: {species.population}')

# Function to find potentially endangered populations
def potentially_endangered(populations: list[AnimalSpecies], threshold: int) -> list[AnimalSpecies]:
    output = []

    for species in animal_species:
        if species.population < threshold:
            output.append(species)

    return output

# Returns a list of references
result = potentially_endangered(animal_species, 10000)
print(result)