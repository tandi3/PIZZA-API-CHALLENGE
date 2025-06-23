import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from faker import Faker
from server.app import app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

fake = Faker()

pizza_data = [
    {"name": "Meat Lovers", "ingredients": "Tomato, Mozzarella, Sausage, Bacon, Pepperoni"},   
    {"name": "Buffalo Chicken", "ingredients": "Buffalo Sauce, Chicken, Mozzarella, Blue Cheese"},
    {"name": "Supreme", "ingredients": "Tomato, Mozzarella, Pepperoni, Sausage, Bell Peppers, Onions"}, 
    {"name": "Margherita", "ingredients": "Tomato, Mozzarella, Basil"},
    {"name": "Pepperoni", "ingredients": "Tomato, Mozzarella, Pepperoni"},
    {"name": "BBQ Chicken", "ingredients": "BBQ Sauce, Chicken, Red Onion, Cilantro"},
    {"name": "Hawaiian", "ingredients": "Tomato, Mozzarella, Ham, Pineapple"},
   
]

restaurant_names = [
    "Pepper's Pizzeria",
    "The Pizza Dough",
    "Dough Doo Pizzeria",
    "Peponi's Pizza",
    "Just n' Time Pizzeria",
    "Pizza Sauce Pizzeria",
    "Pizza Nation",    
]

with app.app_context():
    print("Dropping existing tables...")
    db.drop_all()
    print("Creating tables...")
    db.create_all()

    # Create restaurants
    restaurants = []
    for name in restaurant_names:
        r = Restaurant(name=name, address=fake.address())
        restaurants.append(r)

    # Create pizzas
    pizzas = []
    for p in pizza_data:
        pizza = Pizza(name=p["name"], ingredients=p["ingredients"])
        pizzas.append(pizza)

    db.session.add_all(restaurants + pizzas)
    db.session.commit()

    # Create restaurant_pizzas with prices
    restaurant_pizzas = []
    for i in range(len(pizzas)):
        rp = RestaurantPizza(
            price=fake.random_int(min=1, max=30),
            pizza_id=pizzas[i].id,
            restaurant_id=restaurants[i].id
        )
        restaurant_pizzas.append(rp)

    db.session.add_all(restaurant_pizzas)
    db.session.commit()

    print("Seed complete!")
