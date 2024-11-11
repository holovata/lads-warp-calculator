from flask import Flask, redirect, send_from_directory
from flask_cors import CORS
from backend.api.simulation_routes import simulation_bp

app = Flask(__name__, static_folder="build", static_url_path="")
CORS(app)

# Регистрируем Blueprint для API
app.register_blueprint(simulation_bp, url_prefix='/api')

@app.route('/')
def serve_frontend():
    # Отдаем index.html из папки build
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=False)
