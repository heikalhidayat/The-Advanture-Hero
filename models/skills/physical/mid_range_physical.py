from models.skills.base_skills import Skills

from config.config import (
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

class ShadowStep(Skills):
    def __init__(
        self,
        name = "Shadow Step",
        category = "Physical",
        armed = False,
        range_type = "Mid-Range",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = 1,
        agility = 5,
        defense = 0,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = 3,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence, 
            energy, mana, strength, agility, defense, vitality, magic, 
            dexterity, resistance, intelligence
        )

class TumbleEscape(Skills):
    def __init__(
        self,
        name = "Tumble Escape",
        category = "Physical",
        armed = False,
        range_type = "Mid-Range",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = 1,
        agility = 6,
        defense = 0,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = 2,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence, 
            energy, mana, strength, agility, defense, vitality, magic,
            dexterity, resistance, intelligence
        )

class BounceStrike(Skills):
    def __init__(
        self,
        name = "Bounce Strike",
        category = "Physical",
        armed = False,
        range_type = "Mid-Range",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = 3,
        agility = 3,
        defense = 3,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = 0,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence, 
            energy, mana, strength, agility, defense, vitality, magic,
            dexterity, resistance, intelligence
        )
