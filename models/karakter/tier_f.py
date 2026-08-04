from config import BASE_HP, BASE_ENERGY, BASE_STRENGTH, BASE_AGILITY, BASE_DEFENSE, BASE_MAGIC, BASE_DEXTERITY, BASE_RESISTANCE, TIER_F
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
        magic = 0,
        dexterity = 0,
        resistance = 0,
        intelligence = 0,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(name, job, tier, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence, strength_bonus, agility_bonus, defense_bonus)

class Mage(Karakter):
    def __init__(
        self,
        name,
        job = "Mage",
        tier = TIER_F,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0, 
        vitality = 5,
        magic = BASE_MAGIC,
        dexterity = BASE_DEXTERITY,
        resistance = BASE_RESISTANCE,
        intelligence = 20,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(name, job, tier, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence, strength_bonus, agility_bonus, defense_bonus)

class Assassin(Karakter):
    def __init__(
        self,
        name,
        job = "Assassin",
        tier = TIER_F,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = 0,
        strength = 0,
        agility = BASE_AGILITY,
        defense = 0, 
        vitality = 10,
        magic = 0,
        dexterity = BASE_DEXTERITY,
        resistance = BASE_RESISTANCE,
        intelligence = 0,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(name, job, tier, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence, strength_bonus, agility_bonus, defense_bonus)

class Marksman(Karakter):
    def __init__(
        self,
        name,
        job = "Marksman",
        tier = TIER_F,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = 0,
        strength = 0,
        agility = BASE_AGILITY,
        defense = 0, 
        vitality = 15,
        magic = 0,
        dexterity = BASE_DEXTERITY,
        resistance = 0,
        intelligence = 0,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(name, job, tier, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence, strength_bonus, agility_bonus, defense_bonus)

class Support(Karakter):
    def __init__(
        self,
        name,
        job = "Support",
        tier = TIER_F,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = 0,
        strength = 0,
        agility = 0,
        defense = 0, 
        vitality = 10,
        magic = 0,
        dexterity = 0,
        resistance = 0,
        intelligence = 20,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(name, job, tier, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence, strength_bonus, agility_bonus, defense_bonus)
