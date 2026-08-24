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

class HeavySmash(Skills):
    def __init__(
        self,
        name = "Heavy Smash",
        category = "Physical",
        armed = True,
        range_type = "Melee",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = 6,
        agility = 1,
        defense = 1,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = 1,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic, 
            dexterity, resistance, intelligence
        )

class BattleCry(Skills):
    def __init__(
        self,
        name = "Battle Cry",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = 5,
        agility = 1,
        defense = 3,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = 1,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence, 
            energy, mana, strength, agility, defense, vitality, magic, 
            dexterity, resistance, intelligence
        ) 

class CycloneSlash(Skills):
    def __init__(
        self,
        name = "Cyclone Slash",
        category = "Physical",
        armed = True,
        range_type = "Melee",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = 4,
        agility = 2,
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

class BerserkCharge(Skills):
    def __init__(
        self,
        name = "Berserk Charge",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = 5,
        agility = 2,
        defense = 0,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = 1,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence,
            energy, mana, strength, agility, defense, vitality, magic,
            dexterity, resistance, intelligence
    )     
        
class ShieldBash(Skills):
    def __init__(
        self,
        name = "Shield Bash",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = 3,
        agility = 0,
        defense = 6,
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

class IronFortress(Skills):
    def __init__(
        self,
        name = "Iron Fortress",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = 4,
        agility = 0,
        defense = 5,
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
         
class GroundTremor(Skills):
    def __init__(
        self,
        name = "Ground Tremor",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = 3,
        agility = 2,
        defense = 4,
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

class BastionHope(Skills):
    def __init__(
        self,
        name = "Bastion Hope",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = "Stun",
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = 0,
        agility = 0,
        defense = 9,
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

class PoisonBlade(Skills):
    def __init__(
        self,
        name = "Poison Blade",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = "Stun",
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

class FlurryBlows(Skills):
    def __init__(
        self,
        name = "Flurry Blows",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = 4,
        agility = 3,
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

class Assassinate(Skills):
    def __init__(
        self,
        name = "Assassinate",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = 6,
        agility = 2,
        defense = 0,
        vitality = BASE_VITALITY,
        magic = 0,
        dexterity = 1,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(
            name, category, armed, range_type, debuff, level, competence, 
            energy, mana, strength, agility, defense, vitality, magic, 
            dexterity, resistance, intelligence
        )

class GelatinousAbsorb(Skills):
    def __init__(
        self,
        name = "Gelatinous Absorb",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = None,
        level = 1,
        competence = 0,
        energy = BASE_ENERGY,
        mana = 0,
        strength = 3,
        agility = 2,
        defense = 4,
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
