from base_enemy import Enemy

class OrcBerseker(Enemy):
    '''Makhluk berbadan besar dengan kapak ganda'''
    def __init__(
        self,
        name = "Orc Berseker",
        job = "Rare",
        tier = 1,
        level = 1,
        exp = 100,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 100,
        base_energy = 100,
        base_mana = 100,
        strength = 5,
        agility = 1,
        defense = 8,
        vitality = 1,
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

class Gargoyle(Enemy):
    '''Patung batu hidup yang menyergap dari langit-langit'''
    def __init__(
        self,
        name = "Gargoyle",
        job = "Rare",
        tier = 1,
        level = 1,
        exp = 100,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 100,
        base_energy = 100,
        base_mana = 100,
        strength = 5,
        agility = 1,
        defense = 8,
        vitality = 1,
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

class Lizardman(Enemy):
    '''Manusia reptil bersenjata tombak dengan pertahanan tinggi'''
    def __init__(
        self,
        name = "Lizardman",
        job = "Rare",
        tier = 1,
        level = 1,
        exp = 100,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 100,
        base_energy = 100,
        base_mana = 100,
        strength = 5,
        agility = 1,
        defense = 8,
        vitality = 1,
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

class Harpy(Enemy):
    '''Mkhluk setengah wanita setengah burung yang menyerang dari udara'''
    def __init__(
        self,
        name = "Harpy",
        monster_type = "Rare",
        tier = 1,
        level = 1,
        exp = 100,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 100,
        base_energy = 100,
        base_mana = 100,
        strength = 5,
        agility = 1,
        defense = 8,
        vitality = 1,
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

class CentaurArcher(Enemy):
    '''Manusia setengah kuda yang mahir memanah'''
    def __init__(
        self,
        name = "Centaur Archer",
        monster_type = "Rare",
        tier = 1,
        level = 1,
        exp = 100,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 100,
        base_energy = 100,
        base_mana = 100,
        strength = 5,
        agility = 1,
        defense = 8,
        vitality = 1,
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

class ZombiePlaguebringer(Enemy):
    '''Mayat hidup yang menyebarkan racun di area sekitar'''
    def __init__(
        self,
        name = "Zombie Plague Bringer",
        monster_type = "Rare",
        tier = 1,
        level = 1,
        exp = 100,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 100,
        base_energy = 100,
        base_mana = 100,
        strength = 5,
        agility = 1,
        defense = 8,
        vitality = 1,
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

class Werewolf(Enemy):
    '''Manusia serigala lincah dengan serangan cakar beruntun'''
    def __init__(
        self,
        name = "Werewolf",
        monster_type = "Rare",
        tier = 1,
        level = 1,
        exp = 100,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 100,
        base_energy = 100,
        base_mana = 100,
        strength = 5,
        agility = 1,
        defense = 8,
        vitality = 1,
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
        
class Basilisk(Enemy):
    '''Kadal besar yang bisa memberikan efek kutukan atau kaku'''
    def __init__(
        self,
        name = "Basilisk",
        monster_type = "Rare",
        tier = 1,
        level = 1,
        exp = 100,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 100,
        base_energy = 100,
        base_mana = 100,
        strength = 5,
        agility = 1,
        defense = 8,
        vitality = 1,
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
