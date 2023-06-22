from abc import ABC, abstractmethod

from exceptions import NoAvailableRoomsException, NegativeValueException


class Hotel(ABC):
  

    def __init__(self, name="", total_rooms=0, available_rooms=0, rating=0.0):
       
        self.name = name
        self.total_rooms = total_rooms
        self.available_rooms = available_rooms
        self.rating = rating

    @abstractmethod
    def get_location(self):
      

    def book_room(self):
      
        if self.available_rooms > 0:
            self.available_rooms -= 1
        else:
            raise NoAvailableRoomsException("No available rooms in the hotel.")

    def release_room(self):
       
        if self.available_rooms < self.total_rooms:
            self.available_rooms += 1

    def get_available_rooms(self):
       
        return self.available_rooms

    def get_booked_rooms_count(self):
       
        return self.total_rooms - self.available_rooms

    def __str__(self):
     
        return f"{self.__class__.__name__}(name={self.name}, total_rooms={self.total_rooms}, " \
               f"available_rooms={self.available_rooms}, rating={self.rating})"

    def get_attributes_by_type(self, data_type):
      
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

    def update_rating(self, new_rating):
  
        if new_rating < 0:
            raise NegativeValueException("Rating cannot be a negative value.")

        self.rating = new_rating

    __instance = None

    @staticmethod
    def get_instance():
    
        if not Hotel.__instance:
            Hotel.__instance = Hotel()
        return Hotel.__instance
