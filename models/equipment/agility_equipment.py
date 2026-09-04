from config.config import BASE_DURABILITY
from models.equipment.base_equipment import Equipment

class Dagger(Equipment):
    '''
    Pisau genggam ringan, memungkinkan penggunanya melakukan tusukan
    cepat bertubi-tubi.
    '''
    def __init__(
        self,
        name = "Dagger",
        category = "Agility",
        kind = "Weapon",
        price = 100,
        capacity = 2,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 4,
        defense = 0,
        magic = 0,
        dexterity = 0,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength, agility,
            defense, magic, dexterity, resistance
        )

class LeatherBoots(Equipment):
    '''
    Sepatu berbahan kulit elastis yang tidak bersuara, 
    dirancang khusus untuk meningkatkan kecepatan.
    '''
    def __init__(
        self,
        name = "Leather Boots",
        category = "Agility",
        kind = "Armor",
        price = 80,
        capacity = 2,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 3,
        defense = 0,
        magic = 0,
        dexterity = 0,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength, agility,
            defense, magic, dexterity, resistance
        )

class ClothCloak(Equipment):
    '''
    Jubah kain tipis yang berkibar mengikuti arah angin.
    '''
    def __init__(
        self,
        name = "Cloth Cloak",
        category = "Agility",
        kind = "Armor",
        price = 150,
        capacity = 4,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 5,
        defense = 0,
        magic = 0,
        dexterity = 0,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength, agility,
            defense, magic, dexterity, resistance
        )

class SilverNecklace(Equipment):
    '''
    Kalung perak yang memberikan erek meringankan beban tubuh.
    '''
    def __init__(
        self,
        name = "Silver Necklace",
        category = "Agility",
        kind = "Accessory",
        price = 200,
        capacity = 1,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 4,
        defense = 0,
        magic = 0,
        dexterity = 0,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength, agility,
            defense, magic, dexterity, resistance
        )

class PocketWatch(Equipment):
    '''
    Jam saku kuno yang bisa memperlambat waktu.
    '''
    def __init__(
        self,
        name = "Pocket Watch",
        category = "Agility",
        kind = "Accessory",
        price = 300,
        capacity = 1,
        base_durability = BASE_DURABILITY,
        strength = 0,
        agility = 8,
        defense = 0,
        magic = 0,
        dexterity = 0,
        resistance = 0
    ):
        super().__init__(
            name, category, kind, price, capacity, base_durability, strength, agility,
            defense, magic, dexterity, resistance
        )
