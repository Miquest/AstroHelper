import json

class OrbitalElements:

    def __init__(self):
        self.data_table: dict = {}
        self.load_json()
        self.selected_planet: str = ""

    def load_json(self):
        with open("orbital_elements.json", "r") as f:
            self.data_table = json.load(f)

    @property
    def planets(self):
        planet_list = [planet for planet in self.data_table.keys()]
        return planet_list

    @property
    def planet(self):
        return self.selected_planet

    @planet.setter
    def planet(self, value: str):

        if value.lower() in self.planets:
            self.selected_planet = value.lower()
        else:
            raise ValueError("This planet is not available!")

    @property
    def change_rates(self) -> dict:

        if self.selected_planet == "":
            raise ValueError("Select a planet before accessing change rates!")

        return self.data_table[self.planet]["changes"]

    @property
    def elements(self) -> dict:

        if self.selected_planet == "":
            raise ValueError("Select a planet before accessing change rates!")

        return self.data_table[self.planet]["elements"]
