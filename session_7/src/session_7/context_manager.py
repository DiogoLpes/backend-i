import time
import logging



logging.basicConfig(filename='example.txt', level=logging.INFO)
logger = logging.getLogger(__name__)


class FileOpener:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening file {self.filename}")
        self.file = open(self.filename, self.mode)
        logger.info(f"starts here {time.process_time()}")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file {self.filename}")
        if self.file:
            self.file.close()
            logger.info(f"ends here {time.process_time()}")
        # Do not suppress exceptions
        return False

# Usage example:


if __name__ == "__main__":
    with FileOpener("example.txt", "w") as f:
        f.write("Hello, Context Managers!")
        f.write("Hello, Context Managers!")
        f.write("Hello, Context Managers!")
        f.write("Hello, Context Managers!")

