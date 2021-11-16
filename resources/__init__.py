from resources.services.database import DB
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# Custom modules
import resources.routes
import resources.services
from resources.settings import host
