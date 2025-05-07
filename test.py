import numpy
from astrodate import AstroDate
from shapes import Ellipse
from coordinates import Coordinates
from orbital_elements import OrbitalElements
from math import pi


def test_coordinates():
    coords = Coordinates([[1, 2],[-1, 2],[-1, 2]])
    coords.radians = True
    print(coords.polar_coordinates)
    coords.add_coordinate([2.23606798, 2.03444394], polar=True)
    print(coords.coordinates)


if __name__ == "__main__":
    test_coordinates()
