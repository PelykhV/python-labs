from models.hotel import Hotel


# pylint: disable=too-few-public-methods
class Motel(Hotel):


    # pylint: disable=too-many-arguments
    def __init__(self, name="", total_rooms=0, available_rooms=0, rating=0.0, highway="",
                 kilometer=0, cities=""):
       
        super().__init__(name, total_rooms, available_rooms, rating)
        self.highway = highway
        self.kilometer = kilometer
        self.cities = cities

    def get_location(self):
    
        return f"{self.highway}, {self.kilometer}km"

    @staticmethod
    def do_something():
     
        return "Resort hotel-specific action"
