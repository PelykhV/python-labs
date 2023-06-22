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

    hotels_with_high_rating = hotel_manager.find_hotels_with_rating_greater_than(4.0)
    print("Hotels with rating > 4.0:")
    for hotel_item in hotels_with_high_rating:
        print(hotel_item)

    hotels_with_pool = hotel_manager.find_hotels_with_pool()
    print("\nHotels with pool:")
    for hotel_item in hotels_with_pool:
        print(hotel_item)

    results = hotel_manager.get_results_of_method("do_something")
    print("\nResults of do_something():")
    for result in results:
        print(result)

    enumerated_objects = hotel_manager.get_enumerated_objects()
    print("\nEnumerated objects:")
    for enumerated_object in enumerated_objects:
        print(enumerated_object)

    zipped_results = hotel_manager.get_zipped_results("do_something")
    print("\nZipped results:")
    for zipped_result in zipped_results:
        print(zipped_result)

    int_attributes = hotel_manager.get_attributes_by_type(int)
    print(int_attributes)

    str_attributes = hotel_manager.get_attributes_by_type(str)
    print(str_attributes)

    bool_attributes = hotel_manager.get_attributes_by_type(bool)
    print(bool_attributes)


    def check_condition(hotel):
        """

        :param hotel:
        :return:
        """
        return hotel.rating > 4.0


    result = hotel_manager.check_condition(check_condition)
    print(result)

    print("\nNumber of hotels:", len(hotel_manager))
    print("First hotel:", hotel_manager[0])

    print("\nAll hotels:")
    for hotel_item in hotel_manager:
        print(hotel_item)

