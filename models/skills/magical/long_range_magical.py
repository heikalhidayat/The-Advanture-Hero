from base_skills import Skills

from config import (
      BASE_ENERGY,
      BASE_MANA,
      BASE_MAGIC,
      BASE_RESISTANCE,
      BASE_INTELLIGENCE
)

class ManaBurst(Skills):
    def __init__(
        self,
        name = "Mana Burst",
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
        magic = BASE_MAGIC,
        dexterity = 0,
        resistance = BASE_RESISTANCE,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence, 
            energy, mana, strength, agility, defense, vitality, magic, dexterity,
            resistance, intelligence
        )

class ShockWave(Skills):
    def __init__(
        self,
        name = "Shock Wave",
        category = "Magical",
        armed = False,
        range_type = "Long-Range",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = BASE_MAGIC,
        dexterity = 0,
        resistance = BASE_RESISTANCE,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, 
            dexterity, resistance, intelligence
        )

class RepelWave(Skills):
    def __init__(
        self,
        name = "Repel Wave",
        category = "Magical",
        armed = False,
        range_type = "Long-Range",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = BASE_MAGIC,
        dexterity = 0,
        resistance = BASE_RESISTANCE,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence, 
            energy, mana, strength, agility, defense, vitality, magic, dexterity,
            resistance, intelligence
        )

class ArcaneRing(Skills):
    def __init__(
        self,
        name = "Arcane Ring",
        category = "Magical",
        armed = False,
        range_type = "Long-Range",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = BASE_MAGIC,
        dexterity = 0,
        resistance = BASE_RESISTANCE,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, dexterity,
            resistance, intelligence
        )

class MagicShield(Skills):
    def __init__(
        self,
        name = "Magic Shield",
        category = "Magical",
        armed = False,
        range_type = "Long-Range",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = BASE_MAGIC,
        dexterity = 0,
        resistance = BASE_RESISTANCE,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence, 
            energy, mana, strength, agility, defense, vitality, magic, dexterity, 
            resistance, intelligence
        )

class MagicArrow(Skills):
    def __init__(
        self,
        name = "Magic Arrow",
        category = "Magical",
        armed = False,
        range_type = "Long-Range",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = BASE_MAGIC,
        dexterity = 0,
        resistance = BASE_RESISTANCE,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, dexterity,
            resistance, intelligence
        )

class SparkProjectile(Skills):
    def __init__(
        self,
        name = "Spark Projectile",
        category = "Magical",
        armed = False,
        range_type = "Long-Range",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = BASE_MAGIC,
        dexterity = 0,
        resistance = BASE_RESISTANCE,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, dexterity, 
            resistance, intelligence
        )

class Fireball(Skills):
    def __init__(
        self,
        name = "Fireball",
        category = "Magical",
        armed = False,
        range_type = "Long-Range",
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
        dexterity = 0,
        resistance = 3,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, dexterity,
            resistance, intelligence
        )

class LightningStrike(Skills):
    def __init__(
        self,
        name = "Lightning Strike",
        category = "Magical",
        armed = False,
        range_type = "Long-Range",
        debuff = "Stun",
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

class MeteorStrike(Skills):
    def __init__(
        self,
        name = "Meteor Strike",
        category = "Magical",
        armed = False,
        range_type = "Long-Range",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 9,
        dexterity = 0,
        resistance = 0,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, dexterity,
            resistance, intelligence
        )

class GuardianLink(Skills):
    def __init__(
        self,
        name = "Guardian Link",
        category = "Magical",
        armed = False,
        range_type = "Long-Range",
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
        dexterity = 2,
        resistance = 2,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, dexterity,
            resistance, intelligence
        )

class DivineIntervention(Skills):
    def __init__(
        self,
        name = "Divine Intervention",
        category = "Magical",
        armed = False,
        range_type = "Long-Range",
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
        dexterity = 3,
        resistance = 3,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, dexterity,
            resistance, intelligence
        )

class ChronoShift(Skills):
    def __init__(
        self,
        name = "Chrono Shift",
        category = "Magical",
        armed = False,
        range_type = "Long-Range",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 4,
        dexterity = 2,
        resistance = 3,
        intelligence = BASE_INTELLIGENCE,
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, dexterity,
            resistance, intelligence
        )

class GravityWell(Skills):
    def __init__(
        self,
        name = "Gravity Well",
        category = "Magical",
        armed = False,
        range_type = "Long-Range",
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
        dexterity = 2,
        resistance = 2,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, dexterity,
            resistance, intelligence
        )

class BlackHole(Skills):
    def __init__(
        self,
        name = "Black Hole",
        category = "Magical",
        armed = False,
        range_type = "Long-Range",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 8,
        dexterity = 1,
        resistance = 0,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, dexterity,
            resistance, intelligence
        )

class Decay(Skills):
    def __init__(
        self,
        name = "Decay",
        category = "Magical",
        armed = False,
        range_type = "Long-Range",
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
        dexterity = 3,
        resistance = 3,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, dexterity,
            resistance, intelligence
        )

class SoulFeast(Skills):
    def __init__(
        self,
        name = "Soul Feast",
        category = "Magical",
        armed = False,
        range_type = "Long-Range",
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
        
class ArmyDarkness(Skills):
    def __init__(
        self,
        name = "Army Darkness",
        category = "Magical",
        armed = False,
        range_type = "Long-Range",
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
        dexterity = 2,
        resistance = 2,
        intelligence = BASE_INTELLIGENCE
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, dexterity,
            resistance, intelligence
        )
