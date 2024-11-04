# main.py

from src.utils.simulation import run_simulation
from src.utils.simulation import run_simulation_Pair
from src.models.settings import ISimulationSettings
from src.models.banner import SingleBanner, PairBanner_1, PairBanner_2, QuadBanner
from src.views.web_interface import display_simulation_results


def main():
    # Define common settings for banners
    settings = ISimulationSettings(
        base_rate=0.01,
        soft_pity=60,
        soft_pity_increment=0.1,
        hard_pity=70,
    )

    # Define input data for simulation
    input_data = {
        "pulls": 100,
        "initial_pity": 0,
        "is_guaranteed": False,
        "desired_copies": 1,
        "num_simulations": 10000,
        "is_summoning_pair": True
    }
    is_summoning_pair = input_data["is_summoning_pair"]
    # Initialize banners with specific settings
    single_banner = SingleBanner(settings)
    if (is_summoning_pair):
        pair_banner = PairBanner_2(settings)
    else:
        pair_banner = PairBanner_1(settings)

    special_banner = QuadBanner(settings)
    # Simulate pulls for each banner type
    single_banner_result = run_simulation(single_banner, input_data)
    if (is_summoning_pair):
        pair_banner_result = run_simulation_Pair(pair_banner, input_data)
    else:
        pair_banner_result = run_simulation(pair_banner, input_data)
    special_banner_result = run_simulation(special_banner, input_data)

    # Display results
    print("Single Banner Simulation Result:")
    display_simulation_results(single_banner_result)

    print("\nPair Banner Simulation Result:")
    display_simulation_results(pair_banner_result)

    print("\nQuad Banner Simulation Result:")
    display_simulation_results(special_banner_result)


if __name__ == "__main__":
    main()
