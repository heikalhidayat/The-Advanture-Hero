from config import BASE_HP, BASE_ENERGY, BASE_MANA
from base_karakter import Karakter
from physical import (
    # Fighter's innate ability
    HeavySmash, BattleCry, CycloneSlash, BerserkCharge, BasicJab
    # Tank's innate ability
    # Mage's innate ability
    # Assassin's innate ability
    # Marksman's innate ability
    # Support's innate ability
    # Wizard's innate ability
    # Necromancer's innate ability
)

class Fighter(Karakter):
    def __init__(
        self,
        name = "Ragnar",
        job = "Fighter",
        tier = 1,
        level = 1, 
        exp = 0,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
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
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04, 
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, intelligence, strength_bonus,
            agility_bonus, defense_bonus
        )

        self.skill_01 = HeavySmash()
        self.skill_02 = BattleCry()
        self.skill_03 = CycloneSlash()
        self.skill_04 = BerserkCharge()

class Tank(Karakter):
    def __init__(
        self,
        name = "Aegis",
        job = "Tanker",
        tier = 1,
        level = 1, 
        exp = 0, 
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
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
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04, 
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, intelligence, strength_bonus,
            agility_bonus, defense_bonus
        )

class Mage(Karakter):
    def __init__(
        self,
        name = "Ignis",
        job = "Mage",
        tier = 1,
        level = 1, 
        exp = 0,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
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
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04, 
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, intelligence, strength_bonus,
            agility_bonus, defense_bonus
        )

class Assassin(Karakter):
    def __init__(
        self,
        name = "Grim",
        job = "Assassin",
        tier = 1,
        level = 1, 
        exp = 0,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
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
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04, 
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, intelligence, strength_bonus,
            agility_bonus, defense_bonus
        )

class Marksman(Karakter):
    def __init__(
        self,
        name = "Hawkeye",
        job = "Marksman",
        tier = 1,
        level = 1, 
        exp = 0,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
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
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04, 
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, intelligence, strength_bonus,
            agility_bonus, defense_bonus
        )

class Support(Karakter):
    def __init__(
        self,
        name = "Lyra",
        job = "Support",
        tier = 1,
        level = 1, 
        exp = 0,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
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
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04, 
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, intelligence, strength_bonus,
            agility_bonus, defense_bonus
        )

class Wizard(Karakter):
    def __init__(
        self,
        name = "Zphyr",
        job = "Wizard",
        tier = 1,
        level = 1, 
        exp = 0,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
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
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04, 
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, intelligence, strength_bonus,
            agility_bonus, defense_bonus
        )

class Necromancer(Karakter):
    def __init__(
        self,
        name = "Mortis",
        job = "Necromancer",
        tier = 1,
        level = 1, 
        exp = 0,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
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
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04, 
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, intelligence, strength_bonus,
            agility_bonus, defense_bonus
        )

# EXAMPLE
karu = Fighter()
jab = BasicJab()

print(jab.dict_skill)
print(karu.skill_01)
print(karu.strength)
print(karu.change_skill(jab))
