from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import restaurant, pizza, restaurant_pizza
    from .controllers import restaurant_controller, pizza_controller, restaurant_pizza_controller

    app.register_blueprint(restaurant_controller.bp)
    app.register_blueprint(pizza_controller.bp)
    app.register_blueprint(restaurant_pizza_controller.bp)

    return app
