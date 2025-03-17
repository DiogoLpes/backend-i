from contextlib import contextmanager
import time
import logging

logging.basicConfig(filename='example.txt', level=logging.INFO)
logger = logging.getLogger(__name__)


@contextmanager
def open_file(filename, mode):
    try:
        print(f"Opening file {filename}")
        f = open(filename, mode)
        logger.info(f"starts here {time.process_time()}")
        yield f
    except:
        if filename == int:
            raise TypeError("Only integers are allowed")

    finally:
        print(f"Closing file {filename}")
        f.close()
        logger.info(f"ends here {time.process_time()}")


# Usage example:
if __name__ == "__main__":
    with open_file("example.txt", "a") as f:
        f.write("\n1" * 5)
    File_read = open("example.txt", "r")
    for line in File_read:
        if line is str:
            print(line)
            raise TypeError("joreroerjer")
    File_read.close()