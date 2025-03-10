import typer

app = typer.Typer()

@app.command()
def square(number: int):
    input("Insert  a num to calculate the equare: " + number)
    """
    Calculate and print the square.
    """
    typer.echo(f"The square of {number} is {number * number}")

if __name__ == "__main__":
    app()
