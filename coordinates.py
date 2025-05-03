import numpy as np


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

        if coords:
            self.coords = np.array(coords)

    @property
    def coordinates(self):
        return self.coords.tolist()

    @coordinates.setter
    def coordinates(self, value: list):
        self.coords = np.array(value)


    @property
    def polar_coordinates(self):
        return None

    @property
    def cartesian_coordinates(self):
        return None

    def add_coordinate(self, new_coords: list):

        if len(new_coords) != self.coords.shape[1]:
            raise ValueError(f"You cannot add a {len(new_coords)}D coordinate to an {self.coords.shape[1]}D array!")

        self.coords = np.append(self.coords, np.array(new_coords))

    def rotate_by_degrees(self, degrees: list[float], radians: bool = False):
        pass


    def __str__(self):
        return f"Coordinates saved in this instance: {self.coordinates}"