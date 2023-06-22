"""
This module include class Hotel
methods:
    book_room
    release_room
    get_available_rooms
    get_booked_rooms_count
    str
    getinstance
and main in which we created exemplars
"""


class Hotel:
    """
    Creates a class Hotel
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

    def book_room(self):
        """
        Book room from available rooms
        """
        if self.available_rooms > 0:
            self.available_rooms -= 1

    def release_room(self):
        """
        Release room to available rooms
        """

        if self.available_rooms < self.total_rooms:
            self.available_rooms += 1

    def get_available_rooms(self):
        """
        Returns available rooms count
        """
        return self.available_rooms

    def get_booked_rooms_count(self):
        """
        Returns booked rooms count
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

    __instance = None

    @staticmethod
    def getinstance(name, total_rooms, available_rooms, rating):
        """
        Get a singleton instance of the Hotel class.
        If an instance does not exist, create a new instance with the provided arguments.
        Returns:
        - instance: The Hotel instance.
        """
        if not Hotel.__instance:
            Hotel.__instance = Hotel(name, total_rooms, available_rooms, rating)
        return Hotel.__instance


if __name__ == "__main__":
    hotels = [
        Hotel(),
        Hotel("Lviv", 280, 21, 4.2)
    ]

    print(hotels[1].getinstance("Monte", 456, 321, 4.5))
    print(hotels[1].get_available_rooms())
    hotels[1].release_room()
    print(hotels[1].get_booked_rooms_count())

    for hotel in hotels:
        print(hotel)
        
