# models/settings.py

class ISimulationSettings:
    def __init__(self, base_rate, soft_pity, soft_pity_increment, hard_pity):
        self.base_rate = base_rate
        self.soft_pity = soft_pity
        self.soft_pity_increment = soft_pity_increment
        self.hard_pity = hard_pity
