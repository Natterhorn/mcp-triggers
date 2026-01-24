"""
Dice Triggers - 8-sided dice roller and odds calculator
"""
from flask import Flask


def create_app():
    """Application factory"""
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SECRET_KEY'] = 'dev-key-change-in-production'
    
    # Register blueprints
    from .routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
