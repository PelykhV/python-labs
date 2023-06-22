from models.motel import Motel
from models.resort_hotel import ResortHotel


class HotelManager:

    def __init__(self):
        self.hotels = []

    def add_hotel(self, new_hotel):
       
        self.hotels.append(new_hotel)

    def find_hotels_with_rating_greater_than(self, rating):
        
        return [hotel for hotel in self.hotels if hotel.rating > rating]

    def find_hotels_with_pool(self):
        
        return [hotel for hotel in self.hotels if isinstance(hotel, ResortHotel) and (
                hotel.has_child_pool or hotel.has_adult_pool)]

    def __len__(self):
       
        return len(self.hotels)

    def __getitem__(self, index):
        
        return self.hotels[index]

    def __iter__(self):
       
        return iter(self.hotels)

    def get_results_of_method(self, method_name):
       
        return [getattr(obj, method_name)() for obj in self.hotels if hasattr(obj, method_name)]

    def get_enumerated_objects(self):
       
        return [f"Object at index {index}: {hotel}" for index, hotel in enumerate(self.hotels)]

    def get_zipped_results(self, method_name):
      
        method_results = self.get_results_of_method(method_name)
        return [
            f"Object: {hotel}, Result: {res}"
            for hotel, res in zip(self.hotels, method_results)
        ]

    def get_attributes_by_type(self, attribute_type):
      
        attributes = {}
        for hotel in self.hotels:
            for attr_name, attr_value in hotel.__dict__.items():
                if isinstance(attr_value, attribute_type):
                    attributes[attr_name] = attr_value
        return attributes

    def check_condition(self, condition):
       
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
    hotel3.update_rating(3.0)
    print(hotel3.rating)

    print(hotel2.available_rooms)
    hotel2.book_room()
    print(hotel2.available_rooms)
