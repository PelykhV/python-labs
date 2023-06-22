"""
This module provides a HotelManager class for managing hotels.
"""
from models.motel import Motel
from models.resort_hotel import ResortHotel


class HotelManager:
    """
    Class for managing hotels.
    """

    def __init__(self):
        self.hotels = []

    def add_hotel(self, new_hotel):
        """
        Add a new hotel to the manager.

        Parameters:
        hotel (Hotel): The hotel object to be added.
        """
        self.hotels.append(new_hotel)

    def find_hotels_with_rating_greater_than(self, rating):
        """
        Find hotels with a rating greater than the specified rating.

        Parameters:
        rating (float): The rating threshold.

        Returns:
        list: List of hotels with a rating greater than the specified rating.
        """
        return [hotel for hotel in self.hotels if hotel.rating > rating]

    def find_hotels_with_pool(self):
        """
        Find hotels that have pools.

        Returns:
        list: List of hotels that have pools.
        """
        return [hotel for hotel in self.hotels if isinstance(hotel, ResortHotel) and (
                hotel.has_child_pool or hotel.has_adult_pool)]

    def __len__(self):
        """
        Get the number of hotels in the manager.

        Returns:
        int: The number of hotels.
        """
        return len(self.hotels)

    def __getitem__(self, index):
        """
        Get the hotel at the specified index.

        Parameters:
        index (int): The index of the hotel.

        Returns:
        Hotel: The hotel at the specified index.
        """
        return self.hotels[index]

    def __iter__(self):
        """
        Return an iterator over the hotels.

        Returns:
        iterator: Iterator over the hotels.
        """
        return iter(self.hotels)

    def get_results_of_method(self, method_name):
        """
        Get a list of results from calling a specific method on each object in the manager.

        Parameters:
        method_name (str): The name of the method to call.

        Returns:
        list: List of results from calling the method on each object.
        """
        return [getattr(obj, method_name)() for obj in self.hotels if hasattr(obj, method_name)]

    def get_enumerated_objects(self):
        """
        Return a concatenation of the object and its index in the list using enumerate.

        Returns:
        list: List of concatenated strings of object and index.
        """
        return [f"Object at index {index}: {hotel}" for index, hotel in enumerate(self.hotels)]

    def get_zipped_results(self, method_name):
        """
        Return a concatenation of the object and the result of calling a specific method using zip.

        Parameters:
        method_name (str): The name of the method to call.

        Returns:
        list: List of concatenated strings of object and method result.
        """
        method_results = self.get_results_of_method(method_name)
        return [
            f"Object: {hotel}, Result: {res}"
            for hotel, res in zip(self.hotels, method_results)
        ]

    def get_attributes_by_type(self, attribute_type):
        """
        Get attributes of all hotels in the manager by their data type.

        Parameters:
        attribute_type (type): The data type of the attributes to retrieve.

        Returns:
        dict: A dictionary containing attribute names and
        their corresponding values of the specified type.
        """
        attributes = {}
        for hotel in self.hotels:
            for attr_name, attr_value in hotel.__dict__.items():
                if isinstance(attr_value, attribute_type):
                    attributes[attr_name] = attr_value
        return attributes

    def check_condition(self, condition):
        """
        Check if all objects in the manager satisfy the given condition.

        Parameters:
        condition (callable): A callable object that represents the condition to be checked.

        Returns:
        dict: A dictionary with keys "all" and "any" indicating whether all
        or any objects satisfy the condition.
        """
        all_condition = all(condition(obj) for obj in self.hotels)
        any_condition = any(condition(obj) for obj in self.hotels)

        return {"all": all_condition, "any": any_condition}


if __name__ == "__main__":
    hotel_manager = HotelManager()

    hotel1 = ResortHotel("Ukraine", 260, 0, 4.3, "Resort A", 3, True, False)
    hotel2 = Motel("Elise", 100, 50, 3.9, "Richards highway", 150, "Kyiv-Lviv")
    hotel3 = ResortHotel("Monte", 456, 321, 4.5, "Resort B", 2, False, True)
    hotel4 = Motel("Grand", 80, 10, 2.7, "Pronto highway", 300, "Lviv-Odesa")

    hotel_manager.add_hotel(hotel1)
    hotel_manager.add_hotel(hotel2)
    hotel_manager.add_hotel(hotel3)
    hotel_manager.add_hotel(hotel4)

    print(hotel3.rating)
    hotel3.update_rating(-3.0)
    print(hotel3.rating)

    print(hotel2.available_rooms)
    hotel2.book_room()
    print(hotel2.available_rooms)
