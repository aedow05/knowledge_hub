# run.py
# Entry point to start the Flask server. Exposes the app object for Flask CLI.
# Import the factory function
from app import create_app  

# Create the app instance by calling the factory
app = create_app()

# Only run the server if this file is executed directly
if __name__ == "__main__":
    
    # debug=True enables live reloads and detailed error messages
    app.run(debug=True)
