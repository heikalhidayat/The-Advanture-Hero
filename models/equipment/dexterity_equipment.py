class Dexterity(Equipment):
    def __init__(
        self,
        name: str,
        category: "Dexterity",
        kind: str,
        price: int,
        capasity: int,
        base_durability: int,
        dexterity: int
    ):
        super().__init__(name, category, kind, price, capasity, base_durability)
        self.dexterity = dexterity

    def total_dexterity(self, amount: int) -> int:
        self.dexterity += amount
        return self.dexterity

class ShortBow(Dexterity):
    '''
    Busur pendek yang mudah ditarik.
    '''
    def __init__(
        self,
        name = "Short Bow",
        category = "Dexterity",
        kind = "Weapon",
        price = 130,
        capasity = 3,
        base_durability = BASE_DURABILITY,
        dexterity = 5
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, dexterity)

class LeatherGloves(Dexterity):
    '''
    Sarung tangan kulit yang menambah kecepatan tangan.
    '''
    def __init__(
        self,
        name = "Leather Gloves",
        category = "Dexterity",
        kind = "Armor",
        price = 90,
        capasity = 1,
        base_durability = BASE_DURABILITY,
        dexterity = 3
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, dexterity)

class LeatherHood(Dexterity):
    def __init__(
        self,
        name = "Leather Hood",
        category = "Dexterity",
        kind = "Armor",
        price = 110,
        capasity = 2,
        base_durability = BASE_DURABILITY,
        dexterity = 4
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, dexterity)
