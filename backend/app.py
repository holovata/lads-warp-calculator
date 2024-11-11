# backend/app.py
from flask import Flask
from flask_cors import CORS
from backend.api.simulation_routes import simulation_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(simulation_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=False)
