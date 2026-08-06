from config import BASE_HP, BASE_ENERGY, BASE_MANA
from base_karakter import Karakter

class Fighter(Karakter):
    def __init__(
        self,
        name = "Ragnar",
        job = "Fighter",
        tier = 1,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 10,
        agility = 6,
        defense = 8, 
        vitality = 20,
        magic = 0,
        dexterity = 2,
        resistance = 4,
        intelligence = 10,
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
        name = "Aegis",
        job = "Tanker",
        tier = 0,
        level = 1, 
        exp = 0, 
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA, 
        strength = 10,
        agility = 5,
        defense = 13, 
        vitality = 25,
        magic = 0,
        dexterity = 0,
        resistance = 2,
        intelligence = 5,
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
        name = "Ignis",
        job = "Mage",
        tier = 0,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 2,
        agility = 2,
        defense = 1, 
        vitality = 5,
        magic = 15,
        dexterity = 6,
        resistance = 4,
        intelligence = 25,
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
        name = "Grim",
        job = "Assassin",
        tier = 0,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 8,
        agility = 15,
        defense = 1,
        vitality = 18,
        magic = 0,
        dexterity = 6,
        resistance = 0,
        intelligence = 12,
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
        name = "Hawkeye",
        job = "Marksman",
        tier = 0,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 6,
        agility = 6,
        defense = 1, 
        vitality = 12,
        magic = 0,
        dexterity = 15,
        resistance = 2,
        intelligence = 18,
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
        name = "Lyra",
        job = "Support",
        tier = 0,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 2,
        agility = 2,
        defense = 4, 
        vitality = 8,
        magic = 10,
        dexterity = 2,
        resistance = 10,
        intelligence = 22,
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
        name = "Zphyr",
        job = "Wizard",
        tier = 0,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 0,
        agility = 2,
        defense = 0, 
        vitality = 5,
        magic = 18,
        dexterity = 6,
        resistance = 4,
        intelligence = 25,
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
        name = "Mortis",
        job = "Necromancer",
        tier = 1,
        level = 1, 
        exp = 0,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 5,
        magic = 20,
        dexterity = 2,
        resistance = 8,
        intelligence = 25,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(name, tier, job, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence, strength_bonus, agility_bonus, defense_bonus)
