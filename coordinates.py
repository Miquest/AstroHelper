import numpy as np
from math import pi, sqrt


def rotation_matrix_2d(angle):
    return np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])


def rotation_matrix_3d(angles: list):

    if len(angles) != 3:
        raise ValueError("You have to pass 3 angles for 3D coordinate transformation!")

    return rotation_matrix_x(angles[0]) @ rotation_matrix_y(angles[1]) @ rotation_matrix_z(angles[2])

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

    def __init__(self, coords: list = None, radians: bool = False) -> None:

        self._coords = np.array([])
        self.radians = radians

        if coords:
            self._coords = np.array(coords)

    @property
    def coordinates(self):
        return self._coords

    @coordinates.setter
    def coordinates(self, value: list):
        self._coords = np.array(value)

    def _convert_cartesian_2d(self) -> list:

        polar_array = []

        for point in self._coords:
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

        return polar_array

    def _convert_cartesian_3d(self) -> list:

        polar_array = []

        return polar_array

    @property
    def polar_coordinates(self):

        coordinate_array = []

        if self._coords.shape[1] == 2:
            coordinate_array = self._convert_cartesian_2d()

        elif self._coords.shape[1] == 3:
            print("...")

        else:
            raise ValueError(f"Calculation is not possible for {self._coords.shape[1]}D coordinates!")

        return np.array(coordinate_array)

    def add_coordinate(self, new_coords: list, polar: bool = False):

        if len(new_coords) != self._coords.shape[1]:
            raise ValueError(f"You cannot add a {len(new_coords)}D coordinate to an {self._coords.shape[1]}D array!")

        self._coords = np.append(self._coords, np.array([new_coords]), axis=0)

    def rotate_by_degrees(self, degrees):

        if not isinstance(degrees, (int, float, list)):
            raise TypeError("You've passed an invalid data type!")

        rotated_coordinates = []

        if type(degrees) == list:

            # Transform degrees to radians for calculation
            if not self.radians:
                transformed_degrees = [np.deg2rad(degree) for degree in degrees]
                degrees = transformed_degrees

            if len(degrees) != self.coordinates.shape[1]:
                raise ValueError(f"You cannot transform {self._coords.shape[1]}D coordinates!")

            rotation_matrix = rotation_matrix_3d(degrees)

        else:
            if not self.radians:
                degrees = np.deg2rad(degrees)

            rotation_matrix = rotation_matrix_2d(degrees)


        # Iterate through coordinates and rotate them one by one
        for coordinate in self._coords:
            rotated_coordinate = rotation_matrix @ coordinate
            rotated_coordinates.append(rotated_coordinate)

        return np.array(rotated_coordinates)

    def __str__(self):
        return f"Coordinates saved in this instance: {self.coordinates.tolist()}"