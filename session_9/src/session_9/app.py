from typer import Typer
from session_9.bot import *
import os

app = Typer()

@app.command()
def bot():
    return client.run(os.getenv('DISCORD_TOKEN', None))

if __name__ == "__main__":
    app()