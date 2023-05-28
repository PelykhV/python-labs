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

        :return:
        """
        return len(self.hotels)

    def __getitem__(self, idx):
        """

        :param idx:
        :return:
        """
        return self.hotels[index]

    def __iter__(self):
        """

        :return:
        """
        return iter(self.hotels)

    def get_results_of_do_something(self):
        """

        :return:
        """
        return [hotel.do_something() for hotel in self.hotels]

    def get_enumerated_hotels(self):
        """

        :return:
        """
        return list(enumerate(self.hotels))

    def get_zip_results(self):
        """

        :return:
        """
        return [(hotel, hotel.do_something()) for hotel in self.hotels]

    def get_attributes_by_type(self, attribute_type):
        """

        :param attribute_type:
        :return:
        """
        return {key: value for key, value in self.hotels[0].__dict__.items()
                if isinstance(value, attribute_type)}

    def get_all_any_results(self, hotel_condition):
        """

        :param hotel_condition:
        :return:
        """
        return {
            "all": all(hotel_condition(hotel) for hotel in self.hotels),
            "any": any(hotel_condition(hotel) for hotel in self.hotels)
        }


if __name__ == "__main__":
    hotel_manager = HotelManager()

    hotel1 = ResortHotel("Ukraine", 260, 30, 4.3, "Resort A", 3, True, False)
    hotel2 = Motel("Elise", 100, 50, 3.9, "Richards highway", 150, "Kyiv-Lviv")
    hotel3 = ResortHotel("Monte", 456, 321, 4.5, "Resort B", 2, False, True)
    hotel4 = Motel("Grand", 80, 10, 2.7, "Pronto highway", 300, "Lviv-Odesa")

    hotel_manager.add_hotel(hotel1)
    hotel_manager.add_hotel(hotel2)
    hotel_manager.add_hotel(hotel3)
    hotel_manager.add_hotel(hotel4)

    hotels_with_high_rating = hotel_manager.find_hotels_with_rating_greater_than(4.0)
    print("Hotels with rating > 4.0:")
    for hotel_item in hotels_with_high_rating:
        print(hotel_item)

    hotels_with_pool = hotel_manager.find_hotels_with_pool()
    print("\nHotels with pool:")
    for hotel_item in hotels_with_pool:
        print(hotel_item)

    print("\nNumber of hotels:", len(hotel_manager))

    print("\nEnumerated hotels:")
    for index, hotel_item in hotel_manager.get_enumerated_hotels():
        print(index, hotel_item)

    print("\nZip results:")
    for hotel_item, result in hotel_manager.get_zip_results():
        print(hotel_item, result)

    print("\nAttributes of type float:")
    print(hotel_manager.get_attributes_by_type(float))

    print("\nAll and Any results:")
    condition = lambda hotel: hotel.rating > 3.5
    print(hotel_manager.get_all_any_results(condition))
