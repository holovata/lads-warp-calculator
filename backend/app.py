# backend/app.py
from flask import Flask, render_template, request, redirect, url_for
from src.utils.simulation import run_simulation, run_simulation_Pair
from src.models.settings import ISimulationSettings
from src.models.banner import SingleBanner, PairBanner_1, QuadBanner

app = Flask(__name__)
settings = ISimulationSettings(base_rate=0.01, soft_pity=60, soft_pity_increment=0.1, hard_pity=70)

@app.route('/')
def index():
    return redirect(url_for('single_banner'))

@app.route('/single-banner', methods=['GET', 'POST'])
def single_banner():
    result = None
    if request.method == 'POST':
        num_rolls = int(request.form['num_rolls'])
        initial_pity = int(request.form['pity'])
        is_guaranteed = request.form.get('is_guaranteed') == 'on'
        desired_copies = int(request.form['desired_copies'])

        banner = SingleBanner(settings)

        result = run_simulation(banner, {
            "pulls": num_rolls,
            "initial_pity": initial_pity,
            "is_guaranteed": is_guaranteed,
            "desired_copies": desired_copies,
            "num_simulations": 10000
        })

    return render_template('single_banner.html', result=result)

@app.route('/pair-banner', methods=['GET', 'POST'])
def pair_banner():
    result = None
    if request.method == 'POST':
        num_rolls = int(request.form['num_rolls'])
        initial_pity = int(request.form['pity'])
        is_guaranteed = request.form.get('is_guaranteed') == 'on'
        summoning_pair = request.form.get('summoning_pair') == 'on'

        banner = PairBanner_1(settings)

        result = run_simulation_Pair(banner, {
            "pulls": num_rolls,
            "initial_pity": initial_pity,
            "is_guaranteed": is_guaranteed,
            "desired_copies": 1,
            "summoning_pair": summoning_pair,
            "num_simulations": 10000
        })

    return render_template('pair_banner.html', result=result)

@app.route('/quad-banner', methods=['GET', 'POST'])
def quad_banner():
    result = None
    if request.method == 'POST':
        num_rolls = int(request.form['num_rolls'])
        initial_pity = int(request.form['pity'])
        is_guaranteed = request.form.get('is_guaranteed') == 'on'

        banner = QuadBanner(settings)

        result = run_simulation(banner, {
            "pulls": num_rolls,
            "initial_pity": initial_pity,
            "is_guaranteed": is_guaranteed,
            "desired_copies": 1,  # По умолчанию
            "num_simulations": 10000
        })

    return render_template('quad_banner.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
