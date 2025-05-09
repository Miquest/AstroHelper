from datetime import datetime
from orbital_elements import OrbitalElements
from astrodate import AstroDate
import numpy as np

class Planets:

    def __init__(self, time: datetime = datetime.now(), radians: bool = False):
        self.orbital_elements = OrbitalElements()
        self.selected_planet = None
        self.selected_time = AstroDate(time)

        self.radians = radians
        self.equinox = AstroDate(datetime(year=2000, month=1, day=1, hour=12))
        self.time_difference_centuries = (self.selected_time.julian_date - self.equinox.julian_date) / 36525

    @property
    def time(self):
        return self.selected_time

    @time.setter
    def time(self, value: AstroDate):
        self.selected_time = value
        self.time_difference_centuries = (self.selected_time.julian_date - self.equinox.julian_date) / 36525

    @property
    def planet_list(self):
        return self.orbital_elements.planets

    @property
    def planet(self):
        return self.selected_planet

    @planet.setter
    def planet(self, value: str):

        if value.lower() not in self.planet_list:
            raise ValueError("This planet is not available")

        self.selected_planet = value.lower()
        self.orbital_elements.planet = value.lower()

    @property
    def excentricity(self):

        difference = self.orbital_elements.change_rates["de"] * self.time_difference_centuries
        return self.orbital_elements.elements["e"] + difference

    @property
    def major_axis(self):

        difference = self.orbital_elements.change_rates["da_au"] * self.time_difference_centuries
        return self.orbital_elements.elements["a_au"] + difference

    @property
    def inclination(self):

        difference = self.orbital_elements.change_rates["di_deg"] * self.time_difference_centuries

        if self.radians:
            return np.deg2rad(self.orbital_elements.elements["i_deg"] + difference)

        return self.orbital_elements.elements["i_deg"] + difference

    @property
    def ascending_node(self):

        difference = self.orbital_elements.change_rates["dOmega_deg"] * self.time_difference_centuries

        if self.radians:
            return np.deg2rad(self.orbital_elements.elements["Omega_deg"] + difference)

        return self.orbital_elements.elements["Omega_deg"] + difference

    @property
    def arg_of_perihelon(self):

        difference = self.orbital_elements.change_rates["domega_deg"] * self.time_difference_centuries

        if self.radians:
            return np.deg2rad(self.orbital_elements.elements["omega_deg"] + difference)

        return self.orbital_elements.elements["omega_deg"] + difference

    @property
    def mean_anomaly(self):

        difference = self.orbital_elements.change_rates["dM_deg"] * self.time_difference_centuries

        if self.radians:
            return np.deg2rad(self.orbital_elements.elements["dM_deg"] + difference)

        return self.orbital_elements.elements["dM_deg"] + difference

