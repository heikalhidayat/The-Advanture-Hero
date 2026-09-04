from config.config import BASE_DURABILITY
from models.equipment.base_equipment import Equipment

class HeavyCloak(Equipment):
    '''
    Jubal wol tebal berlapis zat anti-bakar.
    '''
    def __init__(
        self,
        name = "Heavy Cloak",
        category = "Resistance",
        kind = "Armor",
        price = 250,
        capacity = 3,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 0,
        defense = 0,
        magic = 0,
        dexterity = 0,
        resistance = 8
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength,
            agility, defense, magic, dexterity, resistance
        )

class LeatherVest(Equipment):
    '''
    Rompi kulit yang dinetralkan menggunakan ramuan khusus.
    '''
    def __init__(
        self,
        name = "Leather Vest",
        category = "Resistance",
        kind = "Armor",
        price = 180,
        capacity = 3,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 0,
        defense = 0,
        magic = 0,
        dexterity = 0,
        resistance = 5
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength,
            agility, defense, magic, dexterity, resistance
        )

class JadeRing(Equipment):
    '''
    Cincin dari batu giok hijau penangkal kutukan.
    '''
    def __init__(
        self,
        name = "Jade Ring",
        category = "Resistance",
        kind = "Armor",
        price = 300,
        capacity = 1,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 0,
        defense = 0,
        magic = 0,
        dexterity = 0,
        resistance = 7
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength,
            agility, defense, magic, dexterity, resistance
        )

class Talisman(Equipment):
    '''
    Jimat kertas bertuliskan mantra pelindung.
    '''
    def __init__(
        self,
        name = "Talisman",
        category = "Resistance",
        kind = "Accessory",
        price = 200,
        capacity = 1,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 0,
        defense = 0,
        magic = 0,
        dexterity = 0,
        resistance = 4
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength,
            agility, defense, magic, dexterity, resistance
        )
