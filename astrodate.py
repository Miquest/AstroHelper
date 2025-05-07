from datetime import datetime, timedelta
import numpy as np

class AstroDate:

    def __init__(self, date = None):

        self.datetime_obj = datetime.now()
        self.seconds = None
        self.minutes = None
        self.hours = None
        self.day = None
        self.month = None
        self.year = None
        self.julian_date = None

        if date:
            if type(date) == str:
                try:
                    self.datetime_obj = datetime.fromisoformat(date)
                except ValueError:
                    print("Date string has to be in ISO8601 format")
            elif type(date) == datetime:
                self.datetime_obj = date

        self._set_properties_from_object()
        self.to_julian()

    @property
    def date(self):
        return self.datetime_obj.isoformat()

    @date.setter
    def date(self, value):
        if type(value) == str:
            try:
                self.datetime_obj = datetime.fromisoformat(value)
            except ValueError:
                print("Date string has to be in ISO8601 format")
        elif type(value) == datetime:
            self.datetime_obj = value

        self._set_properties_from_object()
        self.to_julian()


    # Define properties for further and comfortable use in class and it's entities
    def _set_properties_from_object(self) -> None:
        self.seconds = self.datetime_obj.second
        self.minutes = self.datetime_obj.minute
        self.hours = self.datetime_obj.hour

        self.day = self.datetime_obj.day
        self.month = self.datetime_obj.month
        self.year = self.datetime_obj.year

    def _create_datetime_from_attributes(self) -> None:

        self.datetime_obj = datetime(
            year=self.year,
            month=self.month,
            day=self.day,
            hour=self.hours,
            minute=self.minutes,
            second=self.seconds
        )

    def _time_fraction(self) -> float:
        return (self.hours / 24) + (self.minutes / 1440) + (self.seconds / 86400)

    # calc_ prefix is used for values needed for the calculation
    def to_julian(self, date: datetime=None) -> float:

        if date:
            self.datetime_obj = date
            self._set_properties_from_object()

        calc_day = self.day + self._time_fraction()

        if self.month > 2:
            calc_year = self.year
            calc_month = self.month
        else:
            calc_year = self.year - 1
            calc_month = self.month + 12

        b = 2-np.floor(calc_year/100)+np.floor(calc_year/400)

        self.julian_date = np.floor(365.25 * (calc_year + 4716)) + np.floor(30.6001 * (calc_month + 1)) + calc_day + b - 1524.5
        return self.julian_date


    def from_julian(self, julian_date: float) -> datetime:

        z = np.floor(julian_date + 0.5)
        f = julian_date + 0.5 - z

        alpha = np.floor((z - 1867216.25) / 36524.25)
        a = z + 1 + alpha - np.floor(alpha / 4)

        b = a + 1524
        c = np.floor((b-122.1)/365.25)
        d = np.floor(365.25*c)
        e = np.floor((b-d)/30.6001)
        calc_day = b - d - np.floor(30.6001*e)+f
        self.day = int(calc_day)


        if e <= 13:
            self.month = int(e - 1)
            self.year = int(c-4716)
        else:
            self.month = int(e - 13)
            self.year = int(c - 4715)


        calc_hours = (calc_day - np.floor(calc_day))*24
        calc_minutes = (calc_hours - np.floor(calc_hours)) * 60
        calc_seconds = (calc_minutes - np.floor(calc_minutes)) * 60

        self.hours = int(calc_hours)
        self.minutes = int(calc_minutes)
        self.seconds = int(calc_seconds)

        self.datetime_obj = datetime.now()
        self._create_datetime_from_attributes()
        self.julian_date = julian_date

        return self.datetime_obj

    # Magic method for "toString()" function
    def __str__(self):
        return f"ISO8601 datetime: {self.datetime_obj.isoformat()}\nJulian date: {self.julian_date}"

    # Add a python timedelta
    def __add__(self, other: timedelta):
        self.datetime_obj += other
        return AstroDate(date=self.datetime_obj)

    # Subtract a python timedelta
    def __sub__(self, other: timedelta):
        self.datetime_obj -= other
        return AstroDate(date=self.datetime_obj)