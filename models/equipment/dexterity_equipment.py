from config.config import BASE_DURABILITY
from models.equipment.base_equipment import Equipment

class ShortBow(Equipment):
    '''
    Busur pendek yang mudah ditarik.
    '''
    def __init__(
        self,
        name = "Short Bow",
        category = "Dexterity",
        kind = "Weapon",
        price = 130,
        capacity = 3,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 0,
        defense = 0,
        magic = 0,
        dexterity = 5,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength,
            agility, defense, magic, dexterity, resistance
        )

class LeatherGloves(Equipment):
    '''
    Sarung tangan kulit yang menambah kecepatan tangan.
    '''
    def __init__(
        self,
        name = "Leather Gloves",
        category = "Dexterity",
        kind = "Armor",
        price = 90,
        capacity = 1,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 0,
        defense = 0,
        magic = 0,
        dexterity = 3,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength,
            agility, defense, magic, dexterity, resistance
        )

class LeatherHood(Equipment):
    def __init__(
        self,
        name = "Leather Hood",
        category = "Dexterity",
        kind = "Armor",
        price = 110,
        capacity = 2,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 0,
        defense = 0,
        magic = 0,
        dexterity = 4,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength,
            agility, defense, magic, dexterity, resistance
        )
