from config import BASE_HP, BASE_ENERGY, BASE_STRENGTH, BASE_AGILITY, BASE_DEFENSE, TIER_F
from base_karakter import Karakter

class Tanker(Karakter):
    def __init__(
        self,
        name,
        job = "Tanker",
        tier = TIER_F,
        level = 1, 
        exp = 0, 
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = 0, 
        strength = BASE_STRENGTH,
        agility = BASE_AGILITY,
        defense = BASE_DEFENSE, 
        vitality = 20,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0
    ):
        super().__init__(name, job, tier, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, strength_bonus, agility_bonus, defense_bonus)
