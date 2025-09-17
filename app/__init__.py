from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Create a Migrate object globally to allow initializing it later
migrate = Migrate()
db = SQLAlchemy()

"""
    Flask application factory function.
    This is a recommended pattern in Flask for flexibility.
    Steps performed here:
      1. Create the Flask app object
      2. Load configuration
      3. Initialize extensions (DB, migrations)
      4. Register routes
      5. Return the app object
    """
def create_app():

    # Create Flask app instance
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_object("config.config")

    # Initialize extensions with the app instance
    
    # Binds SQLAlchemy to this Flask app
    db.init_app(app)

    # Binds Alembic migrations to this app & DB
    migrate.init_app(app, db)

    # Create temporary test route
    """
        Simple health check endpoint.
        Returns a JSON object indicating the server is running.
        """
    @app.route("/health")
    def health():
        return {"status": "Ok"}
    #Return flask app instance
    return app