import numpy as np
from math import sqrt


class Ellipse:

    def __init__(self, a: float, b: float):
        self.major_axis = a
        self.minor_axis = b
        self.epsilon = sqrt( 1 - (b / a) ** 2)
        self.e = None

    @property
    def excentricity(self):
        if self.e:
            return self.e
        else:
            raise ValueError("Currently not available!")

    @property
    def a(self):
        return self.major_axis

    @a.setter
    def a(self, value: int):
        self.major_axis = value
        self.epsilon = sqrt(1 - (self.minor_axis / self.major_axis) ** 2)

    @property
    def b(self):
        return self.minor_axis

    @b.setter
    def b(self, value: float):
        self.minor_axis = value
        self.epsilon = sqrt(1 - (self.minor_axis / self.major_axis) ** 2)


    def _kepler_equation(self, m: float, e: float) -> float:
        return m - e + self.epsilon * np.sin(e)

    def search_exzentricity(self, value: float) -> float:

        # Define the minimum and maximum value we could possibly have.
        # Since we measure the excentric anomaly in degrees, the maximum is
        # 360 and minimum is 0
        upper_bound = 360
        lower_bound = 0


        return 0.0


    def __str__(self):
        return f"a: {self.a}\nb: {self.b}\ne: {self.e}\nepsilon: {self.epsilon}"



