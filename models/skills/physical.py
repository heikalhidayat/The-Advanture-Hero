from base_skills import Skills

class BasicJab(Skills):
    def __init__(
        self,
        name = "BASIC JAB",
        category = "Physical",
        armed = False,
        range_type = "Melee",
        debuff = None,
        level = 1,
        competence = 100,
        energy = 0,
        mana = 0,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 0,
        dexterity = 0,
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
        energy = 0,
        mana = 0,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 0,
        dexterity = 0,
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
        energy = 0,
        mana = 0,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 0,
        dexterity = 0,
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
        energy = 0,
        mana = 0,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 0,
        dexterity = 0,
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
        energy = 0,
        mana = 0,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 0,
        dexterity = 0,
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
        energy = 0,
        mana = 0,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 0,
        dexterity = 0,
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
        energy = 0,
        mana = 0,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 0,
        dexterity = 0,
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
        energy = 0,
        mana = 0,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 0,
        dexterity = 0,
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
        energy = 0,
        mana = 0,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 0,
        dexterity = 0,
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
        energy = 0,
        mana = 0,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 0,
        dexterity = 0,
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
        energy = 0,
        mana = 0,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 0,
        dexterity = 0,
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
        energy = 0,
        mana = 0,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 0,
        dexterity = 0,
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
        energy = 0,
        mana = 0,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 0,
        dexterity = 0,
        resistance = 0,
        intelligence = 0
    ):
        super().__init__(name, category, armed, range_type, debuff, level, competence, energy, mana, strength, agility, defense, vitality, magic, dexterity, resistance, intelligence)
