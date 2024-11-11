# controllers/simulation.py
from backend.src.models.settings import ISimulationSettings


def run_simulation(banner, input_data):
    successful_simulations = 0

    for _ in range(input_data["num_simulations"]):
        char_data = {
            "copies": 0,
            "pity": input_data["initial_pity"],
            "guaranteed": input_data["is_guaranteed"],
            "losses": 0
        }

        pulls_left = input_data["pulls"]

        while pulls_left > 0:
            pulls_left -= 1

            # Use the provided banner's pull method
            success = banner.pull(char_data["pity"], char_data["guaranteed"])
            if success:
                char_data["copies"] += 1
                char_data["pity"] = 0
                char_data["guaranteed"] = False
                char_data["losses"] = 0
            elif success is False:
                char_data["losses"] += 1
                char_data["guaranteed"] = True
                char_data["pity"] = 0

            else:
                char_data["pity"] += 1

        if char_data["copies"] >= input_data["desired_copies"]:
            successful_simulations += 1

    return successful_simulations / input_data["num_simulations"]


def run_simulation_Pair(banner, input_data):
    successful_simulations = 0

    for _ in range(input_data["num_simulations"]):
        char_data = {
            "copies": 0,
            "pity": input_data["initial_pity"],
            "guaranteed": input_data["is_guaranteed"],
            "losses": 0
        }
        l1 = False
        l2 = False
        pulls_left = input_data["pulls"]
        while pulls_left > 0:
            pulls_left -= 1
            # Use the provided banner's pull method
            success = banner.pull(char_data["pity"], char_data["guaranteed"])
            if success == "l1":
                l1 = True
                char_data["pity"] = 0
                char_data["guaranteed"] = False
                char_data["losses"] = 0
            elif success == "l2":
                l2 = True
                char_data["pity"] = 0
                char_data["guaranteed"] = False
                char_data["losses"] = 0
            elif success is False:
                char_data["losses"] += 1
                char_data["guaranteed"] = True
                char_data["pity"] = 0
            else:
                char_data["pity"] += 1

            if l2 is True & l1 is True:
                char_data["copies"] += 1

        if char_data["copies"] >= input_data["desired_copies"]:
            successful_simulations += 1

    return successful_simulations / input_data["num_simulations"]

class SimulationController:
    def __init__(self, settings: ISimulationSettings):
        self.settings = settings
