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

class EnergyEdge(Skills):
    def __init__(
        self,
        name = "Energy Edge",
        category = "Physical",
        armed = False,
        range_type = "Long-Range",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = BASE_STRENGTH,
        agility = BASE_AGILITY,
        defense = BASE_DEFENSE,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = BASE_DEXTERITY,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence, 
            energy, mana, strength, agility, defense, vitality, magic, 
            dexterity, resistance, intelligence
        )

class HallArrows(Skills):
    def __init__(
        self,
        name = "Hall Arrows",
        category = "Physical",
        armed = False,
        range_type = "Long-Range",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = 3,
        agility = 2,
        defense = 0,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = 4,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence, 
            energy, mana, strength, agility, defense, vitality, magic, 
            dexterity, resistance, intelligence
        )

    class PiercingArrow(Skills):
    def __init__(
        self,
        name = "Piercing Arrow",
        category = "Physical",
        armed = False,
        range_type = "Long-Range",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = 3,
        agility = 1,
        defense = 0,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = 5,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence, 
            energy, mana, strength, agility, defense, vitality, magic, 
            dexterity, resistance, intelligence
        )

    class QuickShot(Skills):
    def __init__(
        self,
        name = "Quick Shot",
        category = "Physical",
        armed = False,
        range_type = "Long-Range",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = 2,
        agility = 4,
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
