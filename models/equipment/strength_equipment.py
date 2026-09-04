from config.config import BASE_DURABILITY
from models.equipment.base_equipment import Equipment

class GreatSword(Equipment):
    def __init__(
        self,
        name = "Great Sword",
        category = "Strength",
        kind = "Weapon",
        price = 500,
        capacity = 8,
        base_durability = BASE_DURABILITY,
        strength = 20,
        agility = 0,
        defense = 0,
        magic = 0,
        dexterity = 0,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength,
            agility, defense, magic, dexterity, resistance
        )

class BattleAxe(Equipment):
    '''
    Kapak perang berat yang membutuhkan tenaga besar untuk diayunkan,
    namun menghasilkan damage yang besar.
    '''
    def __init__(
        self,
        name = "Battle Axe",
        category = "Strength",
        kind = "Weapon",
        price = 300,
        capacity = 7,
        base_durability = BASE_DURABILITY,
        strength = 20,
        agility = 0,
        defense = 0,
        magic = 0,
        dexterity = 0,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength,
            agility, defense, magic, dexterity, resistance
        )

class LongSword(Equipment):
    '''
    Pedang besi dua tangan standar.
    '''
    def __init__(
        self,
        name = "Long Sword",
        category = "Strength",
        kind = "Weapon",
        price = 150,
        capacity = 8,
        base_durability = BASE_DURABILITY,
        strength = 5,
        agility = 0,
        defense = 0,
        magic = 0,
        dexterity = 0,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength,
            agility, defense, magic, dexterity, resistance
        )

class Mace(Equipment):
    def __init__(
        self,
        name = "Mace",
        category = "Strength",
        kind = "Weapon",
        price = 200,
        capacity = 8,
        base_durability = BASE_DURABILITY,
        strength = 10,
        agility = 0,
        defense = 0,
        magic = 0,
        dexterity = 0,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength,
            agility, defense, magic, dexterity, resistance
        )

class IronGauntlets(Equipment):
    '''
    Sarung tangan besi yang menambah berat pukulan tangan.
    '''
    def __init__(
        slef,
        name = "Iron Gauntlets",
        category = "Strength",
        kind = "Armor",
        price = 100,
        capacity = 8,
        base_durability = BASE_DURABILITY,
        strength = 5,
        agility = 0,
        defense = 0,
        magic = 0,
        dexterity = 0,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength,
            agility, defense, magic, dexterity, resistance
        )
