from flask import Blueprint, request, jsonify
from ..app import db
from ..models.restaurant_pizza import RestaurantPizza
from ..models.pizza import Pizza
from ..models.restaurant import Restaurant

bp = Blueprint('restaurant_pizza_controller', __name__)

@bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')

    if not (1 <= price <= 30):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    new_rp = RestaurantPizza(
        price=price,
        pizza_id=data['pizza_id'],
        restaurant_id=data['restaurant_id']
    )
    db.session.add(new_rp)
    db.session.commit()

    return jsonify({
        "id": new_rp.id,
        "price": new_rp.price,
        "pizza_id": new_rp.pizza_id,
        "restaurant_id": new_rp.restaurant_id,
        "pizza": {
            "id": new_rp.pizza.id,
            "name": new_rp.pizza.name,
            "ingredients": new_rp.pizza.ingredients
        },
        "restaurant": {
            "id": new_rp.restaurant.id,
            "name": new_rp.restaurant.name,
            "address": new_rp.restaurant.address
        }
    }), 201
