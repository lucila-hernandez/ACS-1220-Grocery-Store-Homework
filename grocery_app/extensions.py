from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from grocery_app.config import Config
import os
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt()
