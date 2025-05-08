import numpy
from astrodate import AstroDate
from shapes import Ellipse
from coordinates import Coordinates
from orbital_elements import OrbitalElements
from math import pi


def test_ellipse():
    ellipsis = Ellipse(5, 3)

    ellipsis.radians = True
    excentricity = ellipsis.excentric_anomaly(pi)
    print(excentricity)




if __name__ == "__main__":
    test_ellipse()
