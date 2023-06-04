import logging

def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                logger = logging.getLogger(__name__)
                if mode.lower() == "console":
                    console_handler = logging.StreamHandler()
                    logger.addHandler(console_handler)
                elif mode.lower() == "file":
                    file_handler = logging.FileHandler("errors.log")
                    logger.addHandler(file_handler)
                logger.exception(e)

        return wrapper

    return decorator
