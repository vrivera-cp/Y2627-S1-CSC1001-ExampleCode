class AnimalSpecies:
    def __init__(self, name: str, scientific_name: str, population: int):
        self.name = name
        self.scientific_name = scientific_name
        self.population = population

    def __repr__(self) -> str:
        return f'Species(\'{self.name}\', \'{self.scientific_name}\', {self.population})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, AnimalSpecies):
            return False
        return (
                self.name == other.name and
                self.scientific_name == other.scientific_name and
                self.population == other.population
        )
