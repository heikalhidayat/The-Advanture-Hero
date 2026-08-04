from config import BASE_HP, BASE_ENERGY, BASE_MANA, TIER_F, TIER_D
from base_karakter import Karakter

class Fighter(Karakter):
    def __init__(
        self,
        name,
        job = "Fighter",
        tier = 0,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = 0,
        strength = 10,
        agility = 6,
        defense = 4, 
        vitality = 18,
        magic = 0,
        dexterity = 2,
        resistance = 2,
        intelligence = 7,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(name, tier, job, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence, strength_bonus, agility_bonus, defense_bonus)

class Tank(Karakter):
    def __init__(
        self,
        name,
        job = "Tanker",
        tier = 0,
        level = 1, 
        exp = 0, 
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = 0, 
        strength = 10,
        agility = 2,
        defense = 10, 
        vitality = 19,
        magic = 0,
        dexterity = 0,
        resistance = 2,
        intelligence = 6,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(name, tier, job, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence, strength_bonus, agility_bonus, defense_bonus)

class Mage(Karakter):
    def __init__(
        self,
        name,
        job = "Mage",
        tier = 0,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0, 
        vitality = 5,
        magic = 14,
        dexterity = 6,
        resistance = 4,
        intelligence = 20,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(name, tier, job, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence, strength_bonus, agility_bonus, defense_bonus)

class Assassin(Karakter):
    def __init__(
        self,
        name,
        job = "Assassin",
        tier = 0,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = 0,
        strength = 6,
        agility = 12,
        defense = 0,
        vitality = 15,
        magic = 0,
        dexterity = 6,
        resistance = 0,
        intelligence = 10,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(name, tier, job, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence, strength_bonus, agility_bonus, defense_bonus)

class Marksman(Karakter):
    def __init__(
        self,
        name,
        job = "Marksman",
        tier = 0,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = 0,
        strength = 2,
        agility = 6,
        defense = 0, 
        vitality = 9,
        magic = 0,
        dexterity = 14,
        resistance = 2,
        intelligence = 16,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(name, tier, job, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence, strength_bonus, agility_bonus, defense_bonus)

class Support(Karakter):
    def __init__(
        self,
        name,
        job = "Support",
        tier = 0,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = 0,
        strength = 0,
        agility = 2,
        defense = 4, 
        vitality = 7,
        magic = 8,
        dexterity = 2,
        resistance = 8,
        intelligence = 18,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(name, tier, job, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence, strength_bonus, agility_bonus, defense_bonus)

class Wizard(Karakter):
    def __init__(
        self,
        name,
        job = "Wizard",
        tier = 0,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0, 
        vitality = 5,
        magic = 14,
        dexterity = 6,
        resistance = 4,
        intelligence = 20,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(name, tier, job, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence, strength_bonus, agility_bonus, defense_bonus)

class Necromancer(Karakter):
    def __init__(
        self,
        name,
        job = "Necromancer",
        tier = 0,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 5,
        magic = 14,
        dexterity = 6,
        resistance = 4,
        intelligence = 20,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(name, tier, job, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence, strength_bonus, agility_bonus, defense_bonus)
