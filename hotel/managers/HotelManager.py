from models.Motel import Motel
from models.ResortHotel import ResortHotel


class HotelManager:
    """
    Class for managing hotels.
    """

    def __init__(self):
        self.hotels = []

    def addHotel(self, hotel):
        """
        Add a new hotel to the manager.

        Parameters:
        hotel (Hotel): The hotel object to be added.
        """
        self.hotels.append(hotel)

    def findHotelsWithRatingGreaterThan(self, rating):
        """
        Find hotels with a rating greater than the specified rating.

        Parameters:
        rating (float): The rating threshold.

        Returns:
        list: List of hotels with a rating greater than the specified rating.
        """
        return [hotel for hotel in self.hotels if hotel.rating > rating]

    def findHotelsWithPool(self):
        """
        Find hotels that have pools.

        Returns:
        list: List of hotels that have pools.
        """
        return [hotel for hotel in self.hotels if isinstance(hotel, ResortHotel) and (
                hotel.has_child_pool or hotel.has_adult_pool)]


if __name__ == "__main__":
    hotel_manager = HotelManager()

    hotel1 = ResortHotel("Lviv", 280, 21, 4.2, "Resort A", 3, True, False)
    hotel2 = Motel("Motel B", 100, 50, 3.8, "Highway 1", 150, "Kyiv-Lviv")
    hotel3 = ResortHotel("Monte", 456, 321, 4.5, "Resort B", 2, False, True)
    hotel4 = Motel("Motel C", 80, 10, 4.0, "Highway 2", 300, "Lviv-Odesa")

    hotel_manager.addHotel(hotel1)
    hotel_manager.addHotel(hotel2)
    hotel_manager.addHotel(hotel3)
    hotel_manager.addHotel(hotel4)

    hotels_with_high_rating = hotel_manager.findHotelsWithRatingGreaterThan(4.0)
    print("Hotels with rating > 4.0:")
    for hotel in hotels_with_high_rating:
        print(hotel)

    hotels_with_pool = hotel_manager.findHotelsWithPool()
    print("\nHotels with pool:")
    for hotel in hotels_with_pool:
        print(hotel)
