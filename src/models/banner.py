# models/banner.py
import random
from abc import ABC, abstractmethod
from src.models.settings import ISimulationSettings


class BaseBanner(ABC):
    def __init__(self, settings: ISimulationSettings, base_rate, soft_pity, soft_pity_increment, hard_pity):
        self.base_rate = base_rate
        self.soft_pity = soft_pity
        self.soft_pity_increment = soft_pity_increment
        self.hard_pity = hard_pity
        self.settings = settings

    @abstractmethod
    def pull(self, pity, guaranteed):
        """
        Abstract method that each subclass must implement.
        Determines the result of a pull based on pity, guaranteed state, and banner-specific logic.
        """
        pass


class SingleBanner(BaseBanner):
    def __init__(self, settings: ISimulationSettings):
        super().__init__(settings, settings.base_rate, settings.soft_pity,
                         settings.soft_pity_increment, settings.hard_pity)

    def pull(self, pity, guaranteed):
        # Calculate the current probability rate based on pity count
        rate = self.base_rate + self.soft_pity_increment * max(0, pity - self.soft_pity)

        # Check for hard pity condition, which guarantees success
        if pity + 1 >= self.hard_pity:
            return True

        # Roll for success based on the current rate
        if random.random() <= rate:
            # If guaranteed is True, return success immediately;
            # otherwise, calculate the limited rate probability
            return guaranteed or (random.random() <= 0.5)

        # If neither hard pity nor success, return None (no success)
        return None


class PairBanner(BaseBanner):
    def __init__(self, settings: ISimulationSettings, is_summoning_pair=False):
        super().__init__(settings, settings.base_rate, settings.soft_pity,
                         settings.soft_pity_increment, settings.hard_pity)
        self.is_summoning_pair = is_summoning_pair

#   UPDATE PULL LOGIC
    def pull(self, pity, guaranteed):
        # Calculate the current probability rate based on pity count
        rate = self.base_rate + self.soft_pity_increment * max(0, pity - self.soft_pity)

        # Check for hard pity condition, which guarantees success
        if pity + 1 >= self.hard_pity:
            return True

        # Roll for success based on the current rate
        if random.random() <= rate:
            # If guaranteed is True, return success immediately;
            # otherwise, calculate the limited rate probability
            return guaranteed or (random.random() <= 0.5)

        # If neither hard pity nor success, return None (no success)
        return None


class QuadBanner(BaseBanner):
    def __init__(self, settings: ISimulationSettings):
        super().__init__(settings, settings.base_rate, settings.soft_pity,
                         settings.soft_pity_increment, settings.hard_pity)

    #   UPDATE PULL LOGIC
    def pull(self, pity, guaranteed):
        # Calculate the current probability rate based on pity count
        rate = self.base_rate + self.soft_pity_increment * max(0, pity - self.soft_pity)

        # Check for hard pity condition, which guarantees success
        if pity + 1 >= self.hard_pity:
            return True

        # Roll for success based on the current rate
        if random.random() <= rate:
            # If guaranteed is True, return success immediately;
            # otherwise, calculate the limited rate probability
            return guaranteed or (random.random() <= 0.25)

        # If neither hard pity nor success, return None (no success)
        return None
