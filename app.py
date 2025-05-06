from grocery_app.extensions import app, db
from grocery_app.routes import main
from grocery_app import create_app


app.register_blueprint(main)

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=5002)
