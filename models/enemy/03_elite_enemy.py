from base_enemy import Enemy

class Minotaur(Enemy):
    '''Monster berkepala banteng yang menjaga labirin dan koridor sempit'''
    def __init__(
        self,
        name = "Minotaur",
        job = "Elite",
        tier = 3,
        level = 1,
        exp = 400,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 400,
        base_energy = 100,
        base_mana = 100,
        strength = 80,
        agility = 80,
        defense = 80,
        vitality = 3,
        magic = 10,
        dexterity = 10,
        resistance = 10,
        intelligence = 2,
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

class Golem(Enemy):
    '''Raksasa batu atau besi dengan pertahanan fisik absolut'''
    def __init__(
        self,
        name = "Golem",
        job = "Elite",
        tier = 3,
        level = 1,
        exp = 400,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 400,
        base_energy = 100,
        base_mana = 100,
        strength = 80,
        agility = 80,
        defense = 80,
        vitality = 3,
        magic = 10,
        dexterity = 10,
        resistance = 10,
        intelligence = 2,
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

class Wyvern(Enemy):
    '''Kerabat naga yang lebih kecil namun sangat agresif di udara'''
    def __init__(
        self,
        name = "Wyvern",
        job = "Elite",
        tier = 3,
        level = 1,
        exp = 400,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 400,
        base_energy = 100,
        base_mana = 100,
        strength = 80,
        agility = 80,
        defense = 80,
        vitality = 3,
        magic = 10,
        dexterity = 10,
        resistance = 10,
        intelligence = 2,
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

class Cyclops(Enemy):
    '''Raksasa bermata satu yang mampu melempar batu besar'''
    def __init__(
        self,
        name = "Cyclops",
        job = "Elite",
        tier = 3,
        level = 1,
        exp = 400,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 400,
        base_energy = 100,
        base_mana = 100,
        strength = 80,
        agility = 80,
        defense = 80,
        vitality = 3,
        magic = 10,
        dexterity = 10,
        resistance = 10,
        intelligence = 2,
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

class Succubus(Enemy):
    '''Monster penggoda yang mencuri nyawa (HP) menggunkan sihir'''
    def __init__(
        self,
        name = "Succubus",
        job = "Elite",
        tier = 3,
        level = 1,
        exp = 400,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 400,
        base_energy = 100,
        base_mana = 100,
        strength = 80,
        agility = 80,
        defense = 80,
        vitality = 3,
        magic = 10,
        dexterity = 10,
        resistance = 10,
        intelligence = 2,
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

class Chimera(Enemy):
    '''Makhluk hibrida berkepala singa, kambing, dan berekor ular'''
    def __init__(
        self,
        name = "Chimera",
        job = "Elite",
        tier = 3,
        level = 1,
        exp = 400,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 400,
        base_energy = 100,
        base_mana = 100,
        strength = 80,
        agility = 80,
        defense = 80,
        vitality = 3,
        magic = 10,
        dexterity = 10,
        resistance = 10,
        intelligence = 2,
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

class Lich(Enemy):
    '''Penyihir mayat hidup yang menguasai sihir es tingkat tinggi'''
    def __init__(
        self,
        name = "Lich",
        job = "Elite",
        tier = 3,
        level = 1,
        exp = 400,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 400,
        base_energy = 100,
        base_mana = 100,
        strength = 80,
        agility = 80,
        defense = 80,
        vitality = 3,
        magic = 10,
        dexterity = 10,
        resistance = 10,
        intelligence = 2,
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
