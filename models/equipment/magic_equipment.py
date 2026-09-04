from config.config import BASE_DURABILITY
from models.equipment.base_equipment import Equipment

class WoodenStaff(Equipment):
    '''
    Tongkat kayu tua berinti kristal mentah yang berfungsi
    untuk memfokuskan sihir.
    '''
    def __init__(
        self,
        name = "Wooden Staff",
        category = "Magic",
        kind = "Weapon",
        price = 120,
        capacity = 3,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 0,
        defense = 0,
        magic = 5,
        dexterity = 0,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength,
            agility, defense, magic, dexterity, resistance
        )

class MagicWand(Equipment):
    '''
    Tongkat sihir pendek yang dapat meningkatkan daya hancur.
    '''
    def __init__(
        self,
        name = "Magic Wand",
        category = "Magic",
        kind = "Weapon",
        price = 500,
        capacity = 3,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 0,
        defense = 0,
        magic = 15,
        dexterity = 0,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength,
            agility, defense, magic, dexterity, resistance
        )

class SilkRobe(Equipment):
    '''
    Jubah sutra yang ditenun menggunakan benang khusus penyerap mana.
    '''
    def __init__(
        self,
        name = "Silk Robe",
        category = "Magic",
        kind = "Armor",
        price = 200,
        capacity = 3,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 0,
        defense = 0,
        magic = 6,
        dexterity = 0,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength,
            agility, defense, magic, dexterity, resistance
        )

class MageHat(Equipment):
    '''
    Topi kain berujung lancip yang membantu mempertajam konsentrasi.
    '''
    def __init__(
        self,
        name = "Mage Hat",
        category = "Magic",
        kind = "Armor",
        price = 100,
        capacity = 3,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 0,
        defense = 0,
        magic = 3,
        dexterity = 0,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength,
            agility, defense, magic, dexterity, resistance
        )

class CrystalRing(Equipment):
    '''
    Cincin yang terkoneksi langsung dengan kapasitas mana.
    '''
    def __init__(
        self,
        name = "Crystal Ring",
        category = "Magic",
        kind = "Accessory",
        price = 300,
        capacity = 3,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 0,
        defense = 0,
        magic = 10,
        dexterity = 0,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength,
            agility, defense, magic, dexterity, resistance
        )
