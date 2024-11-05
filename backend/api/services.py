# backend/api/services.py
from src.utils.simulation import run_simulation
from src.models.settings import ISimulationSettings
from src.models.banner import SingleBanner, PairBanner_1, PairBanner_2, QuadBanner


def calculate_probability(banner_type, data):
    # Создаем настройки из запроса или используем базовые
    settings = ISimulationSettings(
        base_rate=data.get("base_rate", 0.006),
        soft_pity=data.get("soft_pity", 70),
        soft_pity_increment=data.get("soft_pity_increment", 0.003),
        hard_pity=data.get("hard_pity", 90)
    )

    # Выбираем нужный баннер
    if banner_type == "single":
        banner = SingleBanner(settings)
    elif banner_type == "pair":
        banner = PairBanner_1(settings)
    elif banner_type == "quad":
        banner = QuadBanner(settings)

    # Запускаем расчет
    result = run_simulation(banner, data)
    return result
