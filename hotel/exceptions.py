"""
The module containing the exceptions.
"""


class NegativeValueException(ValueError):
    """
    Exception raised when a field is assigned a negative value.

    Attributes:
        field_name (str): The name of the field with the negative value.
    """

    def __init__(self, field_name):
        self.field_name = field_name

    def __str__(self):
        return f"Field {self.field_name} cannot have a negative value"


class NoAvailableRoomsException(Exception):
    """
    Exception raised when there are no available rooms for booking.
    """

    def __str__(self):
        return "No available rooms for booking"
