import json
from datetime import datetime, timedelta, time
import numpy
from astrodate import AstroDate
from methods import Ellipse
from coordinates import Coordinates
from orbital_elements import OrbitalElements
from math import pi


def test_coordinates():
    coords = Coordinates([[1,3],[-1,3],[-1,-3],[1,-3],[-1,0]])
    print(coords.coordinates)
    print(coords.polar_coordinates)

if __name__ == "__main__":
    test_coordinates()
