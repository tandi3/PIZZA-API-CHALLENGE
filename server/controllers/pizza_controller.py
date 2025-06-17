from flask import Blueprint, jsonify
from ..models.pizza import Pizza

bp = Blueprint('pizza_controller', __name__)

@bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{"id": p.id, "name": p.name, "ingredients": p.ingredients} for p in pizzas])
