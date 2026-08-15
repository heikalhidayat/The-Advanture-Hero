from base_skills import Skills

from config import (
      BASE_ENERGY,
      BASE_MANA,
      BASE_STRENGTH,
      BASE_AGILITY,
      BASE_DEFENSE,
      BASE_VITALITY,
      BASE_MAGIC,
      BASE_DEXTERITY,
      BASE_RESISTANCE,
      BASE_INTELLIGENCE
)

class BasicJab(Skills):
    def __init__(
        self,
        name = "BASIC JAB",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = BASE_STRENGTH,
        agility = BASE_AGILITY,
        defense = BASE_DEFENSE,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = BASE_DEXTERITY,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(name, category, armed, range_type, debuff, level, competence, energy, mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence)

class LowKick(Skills):
    def __init__(
        self,
        name = "Low Kick",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = BASE_STRENGTH,
        agility = BASE_AGILITY,
        defense = BASE_DEFENSE,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = BASE_DEXTERITY,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(name, category, armed, range_type, debuff, level, competence, energy, mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence)

class HeavyFist(Skills):
    def __init__(
        self,
        name = "Heavy Fist",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = "Knockback",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = BASE_STRENGTH,
        agility = BASE_AGILITY,
        defense = BASE_DEFENSE,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = BASE_DEXTERITY,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(name, category, armed, range_type, debuff, level, competence, energy, mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence)

class SwepingLeg(Skills):
    def __init__(
        self,
        name = "Sweping Leg",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = BASE_STRENGTH,
        agility = BASE_AGILITY,
        defense = BASE_DEFENSE,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = BASE_DEXTERITY,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(name, category, armed, range_type, debuff, level, competence, energy, mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence)

class PalmPush(Skills):
    def __init__(
        self,
        name = "Palm Push",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = BASE_STRENGTH,
        agility = BASE_AGILITY,
        defense = BASE_DEFENSE,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = BASE_DEXTERITY,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(name, category, armed, range_type, debuff, level, competence, energy, mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence)

class ElbowCharge(Skills):
    def __init__(
        self,
        name = "Elbow Charge",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = BASE_STRENGTH,
        agility = BASE_AGILITY,
        defense = BASE_DEFENSE,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = BASE_DEXTERITY,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(name, category, armed, range_type, debuff, level, competence, energy, mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence)

class AirSlap(Skills):
    def __init__(
        self,
        name = "Air Slap",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = BASE_STRENGTH,
        agility = BASE_AGILITY,
        defense = BASE_DEFENSE,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = BASE_DEXTERITY,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(name, category, armed, range_type, debuff, level, competence, energy, mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence)

class StrikeSlash(Skills):
    def __init__(
        self,
        name = "Strike Slash",
        category = "Physical",
        armed = True,
        range_type = "Melee",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = BASE_STRENGTH,
        agility = BASE_AGILITY,
        defense = BASE_DEFENSE,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = BASE_DEXTERITY,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(name, category, armed, range_type, debuff, level, competence, energy, mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence)

class QuickTrust(Skills):
    def __init__(
        self,
        name = "Quick Trust",
        category = "Physical",
        armed = True,
        range_type = "Melee",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = BASE_STRENGTH,
        agility = BASE_AGILITY,
        defense = BASE_DEFENSE,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = BASE_DEXTERITY,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(name, category, armed, range_type, debuff, level, competence, energy, mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence)

class WideSwing(Skills):
    def __init__(
        self,
        name = "Wide Swing",
        category = "Physical",
        armed = True,
        range_type = "Melee",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = BASE_STRENGTH,
        agility = BASE_AGILITY,
        defense = BASE_DEFENSE,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = BASE_DEXTERITY,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(name, category, armed, range_type, debuff, level, competence, energy, mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence)

class GuardBreak(Skills):
    def __init__(
        self,
        name = "Guard Break",
        category = "Physical",
        armed = True,
        range_type = "Melee",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = BASE_STRENGTH,
        agility = BASE_AGILITY,
        defense = BASE_DEFENSE,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = BASE_DEXTERITY,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(name, category, armed, range_type, debuff, level, competence, energy, mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence)

class CircularSlash(Skills):
    def __init__(
        self,
        name = "Circular Slash",
        category = "Physical",
        armed = True,
        range_type = "Melee",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = BASE_STRENGTH,
        agility = BASE_AGILITY,
        defense = BASE_DEFENSE,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = BASE_DEXTERITY,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(name, category, armed, range_type, debuff, level, competence, energy, mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence)

class EnergyEdge(Skills):
    def __init__(
        self,
        name = "Energy Edge",
        category = "Magical",
        armed = False,
        range_type = "Ranged",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = BASE_STRENGTH,
        agility = BASE_AGILITY,
        defense = BASE_DEFENSE,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = BASE_DEXTERITY,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(name, category, armed, range_type, debuff, level, competence, energy, mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence)
