import random
from base_enemy import Enemy

random_tier = random.randint(1, 2)
random_level = random.randint(1, 5)
random_exp = random.randint(100, 200)
random_drop_item = random.randint(1, 2)
total_exp = random_exp * (random_tier * random_level)

class Slime(Enemy):
    def __init__(
        self,
        name = "Slime",
        job = "Normal", 
        tier = random_tier,
        level = random_level,
        exp = total_exp,
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
        drop_item = random_drop_item,
    ):
        super().__init__(name, job, tier, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, strength_bonus, agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, resistance_bonus)

class GoblinScout(Enemy):
    def __init__(
        self,
        name = "Goblin Scout",
        job = "Normal", 
        tier = random_tier,
        level = random_level,
        exp = total_exp,
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
        drop_item = random_drop_item,
    ):
        super().__init__(name, job, tier, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, strength_bonus, agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, resistance_bonus)

class Giantrat(Enemy):
    def __init__(
        self,
        name = "Giant Rat",
        job = "Normal", 
        tier = random_tier,
        level = random_level,
        exp = total_exp,
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
        drop_item = random_drop_item,
    ):
        super().__init__(name, job, tier, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, strength_bonus, agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, resistance_bonus)

class GoblinWarrior(Enemy):
    def __init__(
        self,
        name = "Goblin Warrior",
        job = "Normal", 
        tier = random_tier,
        level = random_level,
        exp = total_exp,
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
        drop_item = random_drop_item,
    ):
        super().__init__(name, job, tier, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, strength_bonus, agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, resistance_bonus)

class SkeletonWarrior(Enemy):
    def __init__(
        self,
        name = "Skeleton Warrior",
        job = "Normal", 
        tier = random_tier,
        level = random_level,
        exp = total_exp,
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
        drop_item = random_drop_item,
    ):
        super().__init__(name, job, tier, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, strength_bonus, agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, resistance_bonus)

class Kobold(Enemy):
    def __init__(
        self,
        name = "Kobold",
        job = "Normal", 
        tier = random_tier,
        level = random_level,
        exp = total_exp,
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
        drop_item = random_drop_item,
    ):
        super().__init__(name, job, tier, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, strength_bonus, agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, resistance_bonus)

class GiantSpider(Enemy):
    def __init__(
        self,
        name = "Giant Spider",
        job = "Normal", 
        tier = random_tier,
        level = random_level,
        exp = total_exp,
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
        drop_item = random_drop_item,
    ):
        super().__init__(name, job, tier, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, strength_bonus, agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, resistance_bonus)

class FeralWolf(Enemy):
    def __init__(
        self,
        name = "Feral Wolf",
        job = "Normal", 
        tier = random_tier,
        level = random_level,
        exp = total_exp,
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
        drop_item = random_drop_item,
    ):
        super().__init__(name, job, tier, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, strength_bonus, agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, resistance_bonus)

class Imps(Enemy):
    def __init__(
        self,
        name = "Imps",
        job = "Normal", 
        tier = random_tier,
        level = random_level,
        exp = total_exp,
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
        drop_item = random_drop_item,
    ):
        super().__init__(name, job, tier, level, exp, base_hp, base_energy, base_mana, strength, agility, defense, vitality, magic, dexterity, resistance, strength_bonus, agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, resistance_bonus)
