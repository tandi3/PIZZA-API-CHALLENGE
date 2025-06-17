from server.app import create_app, db
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.create_all()

    pizza1 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    restaurant1 = Restaurant(name="Mario's Pizza", address="123 Main St")
    restaurant2 = Restaurant(name="Luigi's Pizza", address="456 Elm St")

    db.session.add_all([pizza1, pizza2, restaurant1, restaurant2])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, pizza_id=pizza1.id, restaurant_id=restaurant1.id)
    rp2 = RestaurantPizza(price=15, pizza_id=pizza2.id, restaurant_id=restaurant2.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()
