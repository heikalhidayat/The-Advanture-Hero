from base_enemy import Enemy

class AncientDragon(Enemy):
    def __init__(
        self,
        name = "Ancient Dragon",
        job = "Legendary",
        tier = 1,
        level = 1,
        exp = 1000,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 1000,
        base_energy = 500,
        base_mana = 500,
        strength = 1000,
        agility = 500,
        defense = 1000,
        vitality = 10,
        magic = 100,
        dexterity = 100,
        resistance = 100,
        intelligence = 100,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0,
        drop_item = None
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04,
            base_hp, base_energy, base_mana, strength, agility, defense,
            vitality, magic, dexterity, resistance, intelligence, 
            strength_bonus, agility_bonus, defense_bonus, magic_bonus,
            dexterity_bonus, resistance_bonus, drop_item
        )
        self.skill_01 = None
        self.skill_02 = None
        self.skill_03 = None
        self.skill_04 = None

class Kraken(Enemy):
    def __init__(
        self,
        name = "Kraken",
        job = "Legendary",
        tier = 1,
        level = 1,
        exp = 1000,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 1000,
        base_energy = 500,
        base_mana = 500,
        strength = 1000,
        agility = 500,
        defense = 1000,
        vitality = 10,
        magic = 100,
        dexterity = 100,
        resistance = 100,
        intelligence = 100,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0,
        drop_item = None
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04,
            base_hp, base_energy, base_mana, strength, agility, defense,
            vitality, magic, dexterity, resistance, intelligence, 
            strength_bonus, agility_bonus, defense_bonus, magic_bonus,
            dexterity_bonus, resistance_bonus, drop_item
        )
        self.skill_01 = None
        self.skill_02 = None
        self.skill_03 = None
        self.skill_04 = None

class Phoenix(Enemy):
    def __init__(
        self,
        name = "Phoenix",
        job = "Legendary",
        tier = 1,
        level = 1,
        exp = 1000,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 1000,
        base_energy = 500,
        base_mana = 500,
        strength = 1000,
        agility = 500,
        defense = 1000,
        vitality = 10,
        magic = 100,
        dexterity = 100,
        resistance = 100,
        intelligence = 100,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0,
        drop_item = None
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04,
            base_hp, base_energy, base_mana, strength, agility, defense,
            vitality, magic, dexterity, resistance, intelligence, 
            strength_bonus, agility_bonus, defense_bonus, magic_bonus,
            dexterity_bonus, resistance_bonus, drop_item
        )
        self.skill_01 = None
        self.skill_02 = None
        self.skill_03 = None
        self.skill_04 = None

class Leviathan(Ememy):
    '''Penguasa lautan terdalam dengan sihir banjur bandang'''
    def __init__(
        self,
        name = "Leviathan",
        job = "Legendary",
        tier = 1,
        level = 1,
        exp = 1000,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 1000,
        base_energy = 500,
        base_mana = 500,
        strength = 1000,
        agility = 500,
        defense = 1000,
        vitality = 10,
        magic = 100,
        dexterity = 100,
        resistance = 100,
        intelligence = 100,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0,
        drop_item = None
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04,
            base_hp, base_energy, base_mana, strength, agility, defense,
            vitality, magic, dexterity, resistance, intelligence, 
            strength_bonus, agility_bonus, defense_bonus, magic_bonus,
            dexterity_bonus, resistance_bonus, drop_item
        )
        self.skill_01 = None
        self.skill_02 = None
        self.skill_03 = None
        self.skill_04 = None

class Titan(Enemy):
    '''Raksasa seukuran gunung tang mampu memicu gempa bumi'''
    def __init__(
        self,
        name = "Titan",
        job = "Legendary",
        tier = 1,
        level = 1,
        exp = 1000,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 1000,
        base_energy = 500,
        base_mana = 500,
        strength = 1000,
        agility = 500,
        defense = 1000,
        vitality = 10,
        magic = 100,
        dexterity = 100,
        resistance = 100,
        intelligence = 100,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0,
        drop_item = None
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04,
            base_hp, base_energy, base_mana, strength, agility, defense,
            vitality, magic, dexterity, resistance, intelligence, 
            strength_bonus, agility_bonus, defense_bonus, magic_bonus,
            dexterity_bonus, resistance_bonus, drop_item
        )
        self.skill_01 = None
        self.skill_02 = None
        self.skill_03 = None
        self.skill_04 = None
