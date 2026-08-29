from config.config import BASE_DURABILITY
from models.equipment.base_equipment import Equipment

class Agility(Equipment):
    def __init__(
        self,
        name: str,
        category: "Agility",
        kind: str,
        price: int,
        capasity: int,
        base_durability: int,
        agility: int
    ):
        super().__init__(name, category, kind, price, capasity, base_durability)
        self.agility = agility

    def total_agility(self, amount: int) -> int:
        self.agility += amount
        return self.agility

class Dagger(Agility):
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
        capasity = 2,
        base_durability = BASE_DURABILITY,
        agility = 4
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, agility)

class LeatherBoots(Agility):
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
        capasity = 2,
        base_durability = BASE_DURABILITY,
        agility = 3
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, agility)

class ClothCloak(Agility):
    '''
    Jubah kain tipis yang berkibar mengikuti arah angin.
    '''
    def __init__(
        self,
        name = "Cloth Cloak",
        category = "Agility",
        kind = "Armor",
        price = 150,
        capasity = 4,
        base_durability = BASE_DURABILITY,
        agility = 5
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, agility)

class SilverNecklace(Agility):
    '''
    Kalung perak yang memberikan erek meringankan beban tubuh.
    '''
    def __init__(
        self,
        name = "Silver Necklace",
        category = "Agility",
        kind = "Accessory",
        price = 200,
        capasity = 1,
        base_durability = BASE_DURABILITY,
        agility = 4
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, agility)

class PocketWatch(Agility):
    '''
    Jam saku kuno yang bisa memperlambat waktu.
    '''
    def __init__(
        self,
        name = "Pocket Watch",
        category = "Agility",
        kind = "Accessory",
        price = 300,
        capasity = 1,
        base_durability = BASE_DURABILITY,
        agility = 8
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, agility)
