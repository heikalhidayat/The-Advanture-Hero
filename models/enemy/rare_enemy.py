from models.enemy.base_enemy import Enemy

class OrcBerseker(Enemy):
    '''Makhluk berbadan besar dengan kapak ganda'''
    def __init__(
        self,
        name = "Orc Berseker",
        job = "Rare",
        tier = 2,
        level = 1,
        exp = 200,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 200,
        base_energy = 50,
        base_mana = 50,
        strength = 20,
        agility = 20,
        defense = 20,
        vitality = 2,
        magic = 5,
        dexterity = 5,
        resistance = 5,
        intelligence = 1,
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
        tier = 2,
        level = 1,
        exp = 200,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 200,
        base_energy = 50,
        base_mana = 50,
        strength = 20,
        agility = 20,
        defense = 20,
        vitality = 2,
        magic = 5,
        dexterity = 5,
        resistance = 5,
        intelligence = 1,
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
        tier = 2,
        level = 1,
        exp = 200,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 200,
        base_energy = 50,
        base_mana = 50,
        strength = 20,
        agility = 20,
        defense = 20,
        vitality = 2,
        magic = 5,
        dexterity = 5,
        resistance = 5,
        intelligence = 1,
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
        job = "Rare",
        tier = 2,
        level = 1,
        exp = 200,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 200,
        base_energy = 50,
        base_mana = 50,
        strength = 20,
        agility = 20,
        defense = 20,
        vitality = 2,
        magic = 5,
        dexterity = 5,
        resistance = 5,
        intelligence = 1,
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
        job = "Rare",
        tier = 2,
        level = 1,
        exp = 200,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 200,
        base_energy = 50,
        base_mana = 50,
        strength = 20,
        agility = 20,
        defense = 20,
        vitality = 2,
        magic = 5,
        dexterity = 5,
        resistance = 5,
        intelligence = 1,
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
        job = "Rare",
        tier = 2,
        level = 1,
        exp = 200,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 200,
        base_energy = 50,
        base_mana = 50,
        strength = 20,
        agility = 20,
        defense = 20,
        vitality = 2,
        magic = 5,
        dexterity = 5,
        resistance = 5,
        intelligence = 1,
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
        job = "Rare",
        tier = 2,
        level = 1,
        exp = 200,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 200,
        base_energy = 50,
        base_mana = 50,
        strength = 20,
        agility = 20,
        defense = 20,
        vitality = 2,
        magic = 5,
        dexterity = 5,
        resistance = 5,
        intelligence = 1,
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
        job = "Rare",
        tier = 2,
        level = 1,
        exp = 200,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = 200,
        base_energy = 50,
        base_mana = 50,
        strength = 20,
        agility = 20,
        defense = 20,
        vitality = 2,
        magic = 5,
        dexterity = 5,
        resistance = 5,
        intelligence = 1,
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
