from flask_pymongo import PyMongo
from __init__ import app
# Setup MongoDB here
mongo = PyMongo(uri="mongodb+srv://admin:admin@cluster0.ddiv96u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")