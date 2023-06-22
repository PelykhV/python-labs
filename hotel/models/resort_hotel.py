"""
The module containing the ResortHotel class is a subclass of the Hotel class
representing a resort hotel.
"""
from models.hotel import Hotel


# pylint: disable=too-few-public-methods
class ResortHotel(Hotel):
    """
    Represents a hotel in a resort.
    """

    # pylint: disable=too-many-arguments
    def __init__(self, name="", total_rooms=0, available_rooms=0, rating=0.0, resort_name="",
                 num_restaurants=0, has_child_pool=False, has_adult_pool=False):
        """
        Creates a new instance of a ResortHotel.

        Parameters:
        name (str): The name of the hotel.
        total_rooms (int): The total number of rooms in the hotel.
        available_rooms (int): The number of available rooms in the hotel.
        rating (float): The rating of the hotel.
        resort_name (str): The name of the resort.
        num_restaurants (int): The number of restaurants in the hotel.
        has_child_pool (bool): Indicates if the hotel has a child pool.
        has_adult_pool (bool): Indicates if the hotel has an adult pool.
        """
        super().__init__(name, total_rooms, available_rooms, rating)
        self.resort_name = resort_name
        self.num_restaurants = num_restaurants
        self.has_child_pool = has_child_pool
        self.has_adult_pool = has_adult_pool

    def get_location(self):
        """
        Returns the name of the resort.
        """
        return self.resort_name

    @staticmethod
    def do_something():
        """
        This method do something
        """
        return "Motel-specific action"
