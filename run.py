from app import create_app

#Create the app using factory function
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)