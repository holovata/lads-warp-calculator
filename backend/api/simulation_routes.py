# backend/api/simulation_routes.py

from flask import Blueprint, request, jsonify, redirect, url_for
from backend.src.utils.simulation import run_simulation, run_simulation_Pair
from backend.src.models.settings import ISimulationSettings
from backend.src.models.banner import SingleBanner, PairBanner_1, PairBanner_2, QuadBanner

simulation_bp = Blueprint('simulation', __name__)

settings = ISimulationSettings(base_rate=0.01, soft_pity=60, soft_pity_increment=0.1, hard_pity=70)

@simulation_bp.route('/')
def index():
    # Удалим redirect и вернем приветственное сообщение в JSON-формате
    return jsonify({"message": "Welcome to the Banner Probability Calculator API"}), 200

@simulation_bp.route('/single-banner', methods=['POST'])
def single_banner():
    data = request.json
    num_rolls = int(data['num_rolls'])
    initial_pity = int(data['initial_pity'])
    is_guaranteed = data.get('is_guaranteed', False)
    desired_copies = int(data['desired_copies'])

    banner = SingleBanner(settings)

    result = run_simulation(banner, {
        "pulls": num_rolls,
        "initial_pity": initial_pity,
        "is_guaranteed": is_guaranteed,
        "desired_copies": desired_copies,
        "num_simulations": 10000
    })

    return jsonify({"result": result})

@simulation_bp.route('/pair-banner', methods=['POST'])
def pair_banner():
    data = request.json
    num_rolls = int(data['num_rolls'])
    initial_pity = int(data['initial_pity'])
    is_guaranteed = data.get('is_guaranteed', False)
    is_summoning_pair = data.get('is_summoning_pair', False)

    if is_summoning_pair:
        banner = PairBanner_2(settings)
        result = run_simulation_Pair(banner, {
            "pulls": num_rolls,
            "initial_pity": initial_pity,
            "is_guaranteed": is_guaranteed,
            "desired_copies": 1,
            "is_summoning_pair": is_summoning_pair,
            "num_simulations": 10000
        })
    else:
        banner = PairBanner_1(settings)
        result = run_simulation(banner, {
            "pulls": num_rolls,
            "initial_pity": initial_pity,
            "is_guaranteed": is_guaranteed,
            "desired_copies": 1,
            "num_simulations": 10000
        })

    return jsonify({"result": result})

@simulation_bp.route('/quad-banner', methods=['POST'])
def quad_banner():
    data = request.json
    num_rolls = int(data['num_rolls'])
    initial_pity = int(data['initial_pity'])
    is_guaranteed = data.get('is_guaranteed', False)

    banner = QuadBanner(settings)

    result = run_simulation(banner, {
        "pulls": num_rolls,
        "initial_pity": initial_pity,
        "is_guaranteed": is_guaranteed,
        "desired_copies": 1,  # По умолчанию
        "num_simulations": 10000
    })

    return jsonify({"result": result})
