class Hotel:
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

    def back_room(self):
        if self.available_rooms > 0:
            self.available_rooms -= 1

    def release_room(self):
        if self.available_rooms < self.total_rooms:
            self.available_rooms += 1

    def get_available_rooms(self):
        return self.available_rooms

    def get_booked_rooms_count(self):
        return self.total_rooms - self.available_rooms

    def __str__(self):
        """
        Returns a string representation of the hotel.

        Returns:
        str: A string that includes the hotel name, total rooms, available rooms, and rating.
        """
        return f"{self.__class__.__name__}(name={self.name}, total_rooms={self.total_rooms}, " \
               f"available_rooms={self.available_rooms}, rating={self.rating})"
