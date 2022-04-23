import os

from flask import Flask
from resources import app


if __name__ == "__main__":
    app.run(
        debug=True,
        host=os.environ.get("BACKEND_HOST", "127.0.0.1"),
        port=os.environ.get("BACKEND_PORT"),
    )
