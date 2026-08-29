from models.skills.base_skills import Skills

from config.config import (
      BASE_ENERGY,
      BASE_MANA,
      BASE_MAGIC,
      BASE_RESISTANCE,
      BASE_INTELLIGENCE
)

class HealingGrace(Skills):
    def __init__(
        self,
        name = "Healing Grace",
        category = "Magical",
        armed = False,
        range_type = "Mid-Range",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 6,
        dexterity = 1,
        resistance = 2,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, dexterity,
            resistance, intelligence
        )

class HolySantuary(Skills):
    def __init__(
        self,
        name = "Holy Santuary",
        category = "Magical",
        armed = False,
        range_type = "Mid-Range",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 3,
        dexterity = 2,
        resistance = 4,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, dexterity,
            resistance, intelligence
        )

class FrostNova(Skills):
    def __init__(
        self,
        name = "Frost Nova",
        category = "Magical",
        armed = False,
        range_type = "Mid-Range",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 7,
        dexterity = 0,
        resistance = 2,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, dexterity,
            resistance, intelligence
        )

class RaiseUndead(Skills):
    def __init__(
        self,
        name = "Raise Undead",
        category = "Magical",
        armed = False,
        range_type = "Mid-Range",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 5,
        dexterity = 4,
        resistance = 0,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, dexterity,
            resistance, intelligence
        )
