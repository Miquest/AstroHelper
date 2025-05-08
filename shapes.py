import numpy as np
from math import sqrt, pi


class Ellipse:

    def __init__(self, a: float, b: float, radians: bool = False):
        self.major_axis = a
        self.minor_axis = b
        self.epsilon = sqrt(1 - (b / a) ** 2)

        self.radians = radians

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

    def excentric_anomaly(self, value: float) -> float:

        # Define the minimum and maximum value we could possibly have.
        # Since we measure the excentric anomaly in degrees, the maximum is
        # 360 and minimum is 0
        if not self.radians:
            value = np.deg2rad(value)

        e_upper_bound = 2 * pi
        e_lower_bound = 0 * pi
        solved = False

        while not solved:

            interval = (e_lower_bound + e_upper_bound) / 2

            temp_solution_lb = self._kepler_equation(value, e_lower_bound)
            temp_solution_ub = self._kepler_equation(value, e_upper_bound)
            interval_solution = self._kepler_equation(value, interval)

            if (temp_solution_lb * interval_solution) < 0 :
                e_upper_bound = interval
            else:
                e_lower_bound = interval

            if abs(temp_solution_lb - temp_solution_ub) < 10**-7:
                solved = True

        if not self.radians:
            return np.rad2deg(e_lower_bound)

        return e_lower_bound

    def __str__(self):
        return f"a: {self.a}\nb: {self.b}\nepsilon: {self.epsilon}"

