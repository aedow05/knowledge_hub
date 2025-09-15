from flask import Flask

def create_app():
    #Create Flask app
    app = Flask(__name__)

    #Create temporary test route
    @app.route("/health")
    def health():
        return {"status": "Ok"}
    
    return app