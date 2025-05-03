import numpy as np
from math import pi, sqrt

def rotation_matrix(angles: list):
    """
    theta = [winkel_x: int, winkel_y: int, winkel_z: int]
    """
    return rotation_matrix_x(angles[0]) @ rotation_matrix_y(angles[1]) @ rotation_matrix_z(
        angles[2])

def rotation_matrix_x(theta):
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta), np.cos(theta)]
    ])

# Rotationsmatrix um die y-Achse
def rotation_matrix_y(theta):
    return np.array([
        [np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

# Rotationsmatrix um die z-Achse
def rotation_matrix_z(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta), np.cos(theta), 0],
        [0, 0, 1]
    ])


# Class for handling 3D and 2D coordinates in cartesian and polar form
class Coordinates:

    def __init__(self, coords: list = None) -> None:

        self.coords = np.array([])
        self.radians = False

        if coords:
            self.coords = np.array(coords)

    @property
    def coordinates(self):
        return self.coords

    @coordinates.setter
    def coordinates(self, value: list):
        self.coords = np.array(value)

    @property
    def polar_coordinates(self):

        polar_array = []

        if self.coords.shape[1] == 2:
            for point in self.coords:
                x, y = point
                angle = np.arctan(abs(y / x))

                if x < 0 < y:
                    angle = pi - angle

                if x < 0 and y < 0:
                    angle += pi

                if x > 0 > y:
                    angle -= 2 * pi - angle

                radius = sqrt(x ** 2 + y ** 2)

                if self.radians:
                    polar_array.append([radius, angle])
                else:
                    polar_array.append([radius, np.rad2deg(angle)])
                    
        elif self.coords.shape[1] == 3:
            print("...")

        else:
            raise ValueError(f"Calculation is not possible for {self.coords.shape[1]}D coordinates!")

        return np.array(polar_array)

    @property
    def cartesian_coordinates(self):
        raise NotImplemented

    def add_coordinate(self, new_coords: list):

        if len(new_coords) != self.coords.shape[1]:
            raise ValueError(f"You cannot add a {len(new_coords)}D coordinate to an {self.coords.shape[1]}D array!")

        self.coords = np.append(self.coords, np.array([new_coords]), axis=0)

    def rotate_by_degrees(self, degrees: list[float], radians: bool = False):
        pass

    def __str__(self):
        return f"Coordinates saved in this instance: {self.coordinates.tolist()}"