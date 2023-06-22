"""
The module containing the decorator.
"""
import logging


def logged(exception, mode):
    """
       Decorator that logs exceptions raised by the decorated function.

       Args:
           exception: The exception type to catch.
           mode: The logging mode ("console" or "file").

       Returns:
           The decorated function.

       """

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            try:
                result = func(*args, **kwargs)
            except exception as error:
                logger = logging.getLogger(__name__)
                if mode.lower() == "console":
                    console_handler = logging.StreamHandler()
                    logger.addHandler(console_handler)
                elif mode.lower() == "file":
                    file_handler = logging.FileHandler("errors.log")
                    logger.addHandler(file_handler)
                logger.exception(error)
            return result

        return wrapper

    return decorator
