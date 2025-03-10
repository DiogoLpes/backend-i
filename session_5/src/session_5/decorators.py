import logging
from datetime import datetime
import time
logger = logging.getLogger(__name__)


def log_calls(func):
    """A decorator that logs function call details."""
    def wrapper(*args, **kwargs):
        logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
        logger.info(f"Started {func.__name__} {datetime.now()}")
        print(f"Calling {func.__name__} with args: {args} kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        logger.info(f"Finished {func.__name__} {datetime.now()}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b



if __name__ == '__main__':
    print("Result of add:", add(3, 4))