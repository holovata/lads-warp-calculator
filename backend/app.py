# backend/app.py
from flask import Flask
from api.endpoints import api

app = Flask(__name__)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)
