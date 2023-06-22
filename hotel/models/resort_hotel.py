from models.hotel import Hotel


# pylint: disable=too-few-public-methods
class ResortHotel(Hotel):
   

    # pylint: disable=too-many-arguments
    def __init__(self, name="", total_rooms=0, available_rooms=0, rating=0.0, resort_name="",
                 num_restaurants=0, has_child_pool=False, has_adult_pool=False):
      
        super().__init__(name, total_rooms, available_rooms, rating)
        self.resort_name = resort_name
        self.num_restaurants = num_restaurants
        self.has_child_pool = has_child_pool
        self.has_adult_pool = has_adult_pool

    def get_location(self):
     
        return self.resort_name

    @staticmethod
    def do_something():
      
        return "Motel-specific action"
