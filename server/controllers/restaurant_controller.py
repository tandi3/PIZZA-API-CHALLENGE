from flask import Blueprint, jsonify, request
from ..app import db
from ..models.restaurant import Restaurant

bp = Blueprint('restaurant_controller', __name__)

@bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{"id": r.id, "name": r.name, "address": r.address} for r in restaurants])

@bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        return jsonify({
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            "pizzas": [{"id": rp.pizza.id, "name": rp.pizza.name, "ingredients": rp.pizza.ingredients}
                       for rp in restaurant.restaurant_pizzas]
        })
    return jsonify({"error": "Restaurant not found"}), 404

@bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    return jsonify({"error": "Restaurant not found"}), 404
