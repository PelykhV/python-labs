"""
The module that contains the Hotel class is an abstract class that represents a hotel.
"""
from abc import ABC, abstractmethod

from exceptions import NoAvailableRoomsException, NegativeValueException


class Hotel(ABC):
    """
    Abstract class representing a Hotel.
    """

    def __init__(self, name="", total_rooms=0, available_rooms=0, rating=0.0):
        """
        Creates a new instance of a Hotel.

        Parameters:
        name (str): The name of the hotel.
        total_rooms (int): The total number of rooms in the hotel.
        available_rooms (int): The number of available rooms in the hotel.
        rating (float): The rating of the hotel.
        """
        self.name = name
        self.total_rooms = total_rooms
        self.available_rooms = available_rooms
        self.rating = rating

    @abstractmethod
    def get_location(self):
        """
        Abstract method to get the location information of the hotel.
        """

    def book_room(self):
        """
        Book a room from available rooms.
        """
        if self.available_rooms > 0:
            self.available_rooms -= 1
        else:
            raise NoAvailableRoomsException("No available rooms in the hotel.")

    def release_room(self):
        """
        Release a room to available rooms.
        """
        if self.available_rooms < self.total_rooms:
            self.available_rooms += 1

    def get_available_rooms(self):
        """
        Returns the count of available rooms.
        """
        return self.available_rooms

    def get_booked_rooms_count(self):
        """
        Returns the count of booked rooms.
        """
        return self.total_rooms - self.available_rooms

    def __str__(self):
        """
        Returns a string representation of the hotel.

        Returns:
        str: A string that includes the hotel name, total rooms, available rooms, and rating.
        """
        return f"{self.__class__.__name__}(name={self.name}, total_rooms={self.total_rooms}, " \
               f"available_rooms={self.available_rooms}, rating={self.rating})"

    def get_attributes_by_type(self, data_type):
        """
        Get a dictionary of attributes with their values for a specific data type.

        Parameters:
        data_type (type): The data type to filter the attributes.

        Returns:
        dict: Dictionary of attributes with their values for the specified data type.
        """
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    def update_rating(self, new_rating):
        """
        Update the rating of the hotel.

        Args:
            new_rating (float): The new rating of the hotel.

        Raises:
            NegativeValueException: If the new rating is a negative value.
        """
        if new_rating < 0:
            raise NegativeValueException("Rating cannot be a negative value.")

        self.rating = new_rating

    __instance = None

    @staticmethod
    def get_instance():
        """
        Get instanceof the Hotel class
        """
        if not Hotel.__instance:
            Hotel.__instance = Hotel()
        return Hotel.__instance
