from config.config import BASE_DURABILITY
from models.equipment.base_equipment import Equipment

class IronShield(Equipment):
    '''
    Perisai besi bundar untuk menangkis rentetan serangan fisik.
    '''
    def __init__(
        self,
        name = "Iron Shield",
        category = "Defense",
        kind = "Weapon",
        price = 180,
        capacity = 5,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 0,
        defense = 8,
        magic = 0,
        dexterity = 0,
        resistance = 0
    ): 
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength, 
            agility, defense, magic, dexterity, resistance
        )

class ChainMail(Equipment):
    '''
    Baju zirah besi yang menutup seluruh dada.
    '''
    def __init__(
        self,
        name = "Chain Mail",
        category = "Defense",
        kind = "Armor",
        price = 400,
        capacity = 6,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 0,
        defense = 15,
        magic = 0,
        dexterity = 0,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength, 
            agility, defense, magic, dexterity, resistance
        )

class IronHelm(Equipment):
    '''
    Pelindung kepala dari baja.
    '''
    def __init__(
        self,
        name = "Iron Helm",
        category = "Defense",
        kind = "Armor",
        price = 150,
        capacity = 3,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 0,
        defense = 5,
        magic = 0,
        dexterity = 0,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength, 
            agility, defense, magic, dexterity, resistance
        )
