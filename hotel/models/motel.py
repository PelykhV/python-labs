"""
The module containing the Motel class is a subclass of the Hotel class representing a motel.
"""
from models.hotel import Hotel


# pylint: disable=too-few-public-methods
class Motel(Hotel):
    """
    Represents a motel.
    """

    # pylint: disable=too-many-arguments
    def __init__(self, name="", total_rooms=0, available_rooms=0, rating=0.0, highway="",
                 kilometer=0, cities=""):
        """
        Creates a new instance of a Motel.

        Parameters:
        name (str): The name of the motel.
        total_rooms (int): The total number of rooms in the motel.
        available_rooms (int): The number of available rooms in the motel.
        rating (float): The rating of the motel.
        highway (str): The name of the highway where the motel is located.
        kilometer (int): The kilometer on the highway where the motel is located.
        cities (str): The cities between which the highway is located (e.g., "Kyiv-Lviv").
        """
        super().__init__(name, total_rooms, available_rooms, rating)
        self.highway = highway
        self.kilometer = kilometer
        self.cities = cities

    def get_location(self):
        """
        Returns the combination of highway name and kilometer as the motel's location.
        """
        return f"{self.highway}, {self.kilometer}km"

    @staticmethod
    def do_something():
        """
        This method do something
        """
        return "Resort hotel-specific action"
