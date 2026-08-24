from base_enemy import Enemy
# Import skills monster
from melee_physical import GelatinousAbsorb
from mid_range_physical import BounceStrike
from long_range_physical import
from melee_magic import SlimeDivide
from mid_range_magic import
from long_range_magic import AcidSpit

class Slime(Enemy):
    def __init__(
        self,
        name = "Slime",
        job = "Normal", 
        tier = 1,
        level = 1,
        exp = 100,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 100,
        base_energy = 0,
        base_mana = 0,
        strength = 10,
        agility = 10,
        defense = 10,
        vitality = 10,
        magic = 0,
        dexterity = 0,
        resistance = 0,
        intelligence = 0,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0,
        drop_item = 1,
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04,
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, strength_bonus, 
            agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, 
            resistance_bonus, drop_item
        )
        self.skill_01 = BounceStrike()
        self.skill_02 = AcidSpit()
        self.skill_03 = GelatinousAbsorb()
        self.skill_04 = SlimeDivide()

class GoblinScout(Enemy):
    def __init__(
        self,
        name = "Goblin Scout",
        job = "Normal", 
        tier = 1,
        level = 1,
        exp = 100,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 150,
        base_energy = 0,
        base_mana = 0,
        strength = 15,
        agility = 15,
        defense = 15,
        vitality = 15,
        magic = 0,
        dexterity = 0,
        resistance = 0,
        intelligence = 0,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0,
        drop_item = 0,
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04,
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, strength_bonus, 
            agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, 
            resistance_bonus, drop_item
        )
        self.skill_01 = None
        self.skill_02 = None
        self.skill_03 = None
        self.skill_04 = None

class Giantrat(Enemy):
    def __init__(
        self,
        name = "Giant Rat",
        job = "Normal", 
        tier = 1,
        level = 1,
        exp = 100,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 200,
        base_energy = 0,
        base_mana = 0,
        strength = 20,
        agility = 20,
        defense = 20,
        vitality = 20,
        magic = 0,
        dexterity = 0,
        resistance = 0,
        intelligence = 0,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0,
        drop_item = 1,
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04,
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, strength_bonus, 
            agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, 
            resistance_bonus, drop_item
        )
        self.skill_01 = None
        self.skill_02 = None
        self.skill_03 = None
        self.skill_04 = None

class GoblinWarrior(Enemy):
    def __init__(
        self,
        name = "Goblin Warrior",
        job = "Normal", 
        tier = 1,
        level = 1,
        exp = 100,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 250,
        base_energy = 0,
        base_mana = 0,
        strength = 25,
        agility = 15,
        defense = 15,
        vitality = 15,
        magic = 0,
        dexterity = 0,
        resistance = 0,
        intelligence = 0,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0,
        drop_item = 0,
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04,
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, strength_bonus, 
            agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, 
            resistance_bonus, drop_item
        )
        self.skill_01 = None
        self.skill_02 = None
        self.skill_03 = None
        self.skill_04 = None

class SkeletonWarrior(Enemy):
    def __init__(
        self,
        name = "Skeleton Warrior",
        job = "Normal", 
        tier = 1,
        level = 1,
        exp = 100,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 300,
        base_energy = 0,
        base_mana = 0,
        strength = 30,
        agility = 20,
        defense = 20,
        vitality = 20,
        magic = 0,
        dexterity = 0,
        resistance = 0,
        intelligence = 0,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0,
        drop_item = 0,
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04,
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, strength_bonus, 
            agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, 
            resistance_bonus, drop_item
        )
        self.skill_01 = None
        self.skill_02 = None
        self.skill_03 = None
        self.skill_04 = None

class Kobold(Enemy):
    def __init__(
        self,
        name = "Kobold",
        job = "Normal", 
        tier = 1,
        level = 1,
        exp = 100,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 350,
        base_energy = 0,
        base_mana = 0,
        strength = 35,
        agility = 25,
        defense = 25,
        vitality = 25,
        magic = 0,
        dexterity = 0,
        resistance = 0,
        intelligence = 0,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0,
        drop_item = 1,
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04,
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, strength_bonus, 
            agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, 
            resistance_bonus, drop_item
        )
        self.skill_01 = None
        self.skill_02 = None
        self.skill_03 = None
        self.skill_04 = None

class GiantSpider(Enemy):
    def __init__(
        self,
        name = "Giant Spider",
        job = "Normal", 
        tier = 1,
        level = 1,
        exp = 100,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 400,
        base_energy = 0,
        base_mana = 0,
        strength = 40,
        agility = 30,
        defense = 30,
        vitality = 30,
        magic = 0,
        dexterity = 0,
        resistance = 0,
        intelligence = 0,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0,
        drop_item = 0,
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04,
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, strength_bonus, 
            agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, 
            resistance_bonus, drop_item
        )
        self.skill_01 = None
        self.skill_02 = None
        self.skill_03 = None
        self.skill_04 = None

class FeralWolf(Enemy):
    def __init__(
        self,
        name = "Feral Wolf",
        job = "Normal", 
        tier = 1,
        level = 1,
        exp = 100,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 450,
        base_energy = 0,
        base_mana = 0,
        strength = 45,
        agility = 35,
        defense = 25,
        vitality = 20,
        magic = 0,
        dexterity = 0,
        resistance = 0,
        intelligence = 0,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0,
        drop_item = 0,
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04,
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, strength_bonus, 
            agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, 
            resistance_bonus, drop_item
        )
        self.skill_01 = None
        self.skill_02 = None
        self.skill_03 = None
        self.skill_04 = None

class Imps(Enemy):
    def __init__(
        self,
        name = "Imps",
        job = "Normal", 
        tier = 1,
        level = 1,
        exp = 100,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 500,
        base_energy = 0,
        base_mana = 0,
        strength = 50,
        agility = 40,
        defense = 30,
        vitality = 30,
        magic = 0,
        dexterity = 0,
        resistance = 0,
        intelligence = 0,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0,
        drop_item = 0,
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04,
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, strength_bonus, 
            agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, 
            resistance_bonus, drop_item
        )
        self.skill_01 = None
        self.skill_02 = None
        self.skill_03 = None
        self.skill_04 = None
