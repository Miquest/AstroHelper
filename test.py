from shapes import Ellipse
from math import pi
from planets import Planets


def test_ellipse():
    ellipsis = Ellipse(5, 3)

    ellipsis.radians = True
    excentricity = ellipsis.excentric_anomaly(pi)
    print(excentricity)

def test_planet():

    planet = Planets()
    planet.planet = "mercury"

    print(planet.excentricity)


if __name__ == "__main__":
    test_planet()
