from base_skills import Skills

from config import (
      BASE_ENERGY,
      BASE_MANA,
      BASE_MAGIC,
      BASE_RESISTANCE,
      BASE_INTELLIGENCE
)

class ShockTounch(Skills):
    def __init__(
        self,
        name = "Shock Tounch",
        category = "Magical",
        armed = False,
        range_type = "Melee",
        debuff = "Stun",
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

class SlimeDivide(Skills):
    def __init__(
        self,
        name = "Slime Divide",
        category = "Magical",
        armed = False,
        range_type = "Melee",
        debuff = "Stun",
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
