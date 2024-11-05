# backend/api/endpoints.py
from flask import Blueprint, request, jsonify
from .services import calculate_probability

api = Blueprint('api', __name__)

@api.route('/api/single-banner', methods=['POST'])
def single_banner():
    data = request.json
    result = calculate_probability("single", data)
    return jsonify(result)

@api.route('/api/pair-banner', methods=['POST'])
def pair_banner():
    data = request.json
    result = calculate_probability("pair", data)
    return jsonify(result)

@api.route('/api/quad-banner', methods=['POST'])
def quad_banner():
    data = request.json
    result = calculate_probability("special", data)
    return jsonify(result)
