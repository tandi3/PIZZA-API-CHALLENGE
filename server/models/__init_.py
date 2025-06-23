# Import the single db instance from app.py
from server.app import db

# Import models here so they get registered with SQLAlchemy
from .restaurant import Restaurant
from .pizza import Pizza
from .restaurant_pizza import RestaurantPizza
