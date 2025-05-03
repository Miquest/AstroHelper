import json
from datetime import datetime, timedelta, time
import numpy
from astrodate import AstroDate
from methods import Ellipse
from coordinates import Coordinates




def test_coordinates():
    coords = Coordinates()
    my_coordinates = [[1,3],[-1,3],[-1,-3],[1,-3],[-1,0]]
    coords.coordinates = my_coordinates

    coords.add_coordinate([1, 2])
    print(coords)

def load_json():
    with open("orbital_elements.json", "r") as file:
        content = json.load(file)


if __name__ == "__main__":
    test_coordinates()

