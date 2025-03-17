from typer import Typer
import logging
import time
import pytest
from rich import print

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Typer()

@app.command()
def triangle(base: int, altura: int):
    area = (base * altura)/2
    print("[bold red] Toma ai o resultado ![/bold red]")
    print(f"The area of the triangle is {round(area)}")


@app.command()
def square(number: int):
    """
    Calculate and print the square.
    """
    print("[bold red] Toma ai o resultado ![/bold red]")
    print(f"The area square of {number} is {number ** 2}")


@app.command()
def sum(num1: int, num2: int) -> int:
    logger.info(f"App started {time.process_time()}")
    sumresult = num1 + num2
    print("[bold red] Toma ai o resultado ![/bold red]")
    print(f"The sum of the numbers is {sumresult}")
    logger.info(f"App Finished {time.process_time()}")


@app.command()
def subtraction(num1: int, num2: int) -> int:
    logger.info(f"App started {time.process_time()}")
    subresult = num1 - num2
    print("[bold red] Toma ai o resultado ![/bold red]")
    print(f"The subtraction of the numbers is {subresult}")
    logger.info(f"App Finished {time.process_time()}")


if __name__ == "__main__":
    app()
