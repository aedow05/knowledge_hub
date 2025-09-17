# config.py
# This file contains all configuration variables for the Flask app.
# It uses environment variables stored in a .env file to keep secrets and
# environment-specific settings out of source code.
import os
from dotenv import load_dotenv

#loads variables from .env file into environment
load_dotenv()

"""
    Central configuration class for the Flask application.
    Attributes:
        SECRET_KEY: Used by Flask to secure sessions and cryptographic operations.
        SQLALCHEMY_DATABASE_URI: Database connection string.
            Defaults to a local SQLite file if DATABASE_URL is not set.
        SQLALCHEMY_TRACK_MODIFICATIONS: Disables a feature that tracks object changes
            to save memory. Recommended to leave False unless needed.
    """
class config:
    
    # Secret key used by flask and extensions for security purposes
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key")
    
    # Database URL, fallback to SQLite for local development
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///knowledge_hub.db")
    
    # Database URL, fallback to SQLite for local development
    SQLALCHEMY_TRACK_MODIFICATIONS = False