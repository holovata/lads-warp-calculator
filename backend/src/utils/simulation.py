from multiprocessing import Pool
from backend.src.models.settings import ISimulationSettings

# Define the threshold for parallel processing
PARALLEL_THRESHOLD = 120

def run_single_simulation(banner, input_data):
    """Runs a single simulation and returns 1 if the target is achieved, otherwise returns 0."""
    char_data = {
        "copies": 0,
        "pity": input_data["initial_pity"],
        "guaranteed": input_data["is_guaranteed"],
        "losses": 0
    }
    pulls_left = input_data["pulls"]

    # Loop through the pulls until they are exhausted
    while pulls_left > 0:
        pulls_left -= 1
        # Use the banner's pull method to determine success
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

    # Return 1 if the desired copies have been achieved, otherwise 0
    return 1 if char_data["copies"] >= input_data["desired_copies"] else 0


def run_simulation(banner, input_data):
    """Runs multiple simulations and returns the average success rate, using parallel processing if necessary."""
    num_simulations = input_data["num_simulations"]

    if num_simulations < PARALLEL_THRESHOLD:
        # Run simulations in a single process if below the threshold
        results = [run_single_simulation(banner, input_data) for _ in range(num_simulations)]
    else:
        # Use multiprocessing if above the threshold
        with Pool() as pool:
            results = pool.starmap(run_single_simulation, [(banner, input_data) for _ in range(num_simulations)])

    return sum(results) / num_simulations


def run_single_simulation_pair(banner, input_data):
    """Runs a single simulation for Pair Banner and returns 1 if the target is achieved, otherwise returns 0."""
    char_data = {
        "copies": 0,
        "pity": input_data["initial_pity"],
        "guaranteed": input_data["is_guaranteed"],
        "losses": 0
    }
    l1 = False
    l2 = False
    pulls_left = input_data["pulls"]

    # Loop through the pulls until they are exhausted
    while pulls_left > 0:
        pulls_left -= 1
        # Use the banner's pull method to determine success
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

        if l1 and l2:
            char_data["copies"] += 1

    # Return 1 if the desired copies have been achieved, otherwise 0
    return 1 if char_data["copies"] >= input_data["desired_copies"] else 0


def run_simulation_Pair(banner, input_data):
    """Runs multiple Pair Banner simulations and returns the average success rate, using parallel processing if necessary."""
    num_simulations = input_data["num_simulations"]

    if num_simulations < PARALLEL_THRESHOLD:
        # Run simulations in a single process if below the threshold
        results = [run_single_simulation_pair(banner, input_data) for _ in range(num_simulations)]
    else:
        # Use multiprocessing if above the threshold
        with Pool() as pool:
            results = pool.starmap(run_single_simulation_pair, [(banner, input_data) for _ in range(num_simulations)])

    return sum(results) / num_simulations


class SimulationController:
    def __init__(self, settings: ISimulationSettings):
        self.settings = settings
