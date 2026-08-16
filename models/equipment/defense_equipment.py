from config import BASE_DURABILITY

class Defense(Equipment):
    def __init__(
        self,
        name: str,
        category: "Defense",
        kind: str,
        price: int,
        capasity: int,
        base_durability: int,
        defense: int
    ):
        super().__init__(name, category, kind, price, capasity, base_durability)
        self.defense = defense

    def total_defense(self, amount: int) -> int:
        self.defense += amount
        return self.defense

class IronShield(Defense):
    '''
    Perisai besi bundar untuk menangkis rentetan serangan fisik.
    '''
    def __init__(
        self,
        name = "Iron Shield",
        category = "Defense",
        kind = "Weapon",
        price = 180,
        capasity = 5,
        base_durability = BASE_DURABILITY,
        defense = 8
    ): 
        super().__init__(name, category, kind, price, capasity, base_durability, defense)

class ChainMail(Defense):
    '''
    Baju zirah besi yang menutup seluruh dada.
    '''
    def __init__(
        self,
        name = "Chain Mail",
        category = "Defense",
        kind = "Armor",
        price = 400,
        capasity = 6,
        base_durability = BASE_DURABILITY,
        defense = 15
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, defense)

class IronHelm(Defense):
    '''
    Pelindung kepala dari baja.
    '''
    def __init__(
        self,
        name = "Iron Helm",
        category = "Defense",
        kind = "Armor",
        price = 150,
        capasity = 3,
        base_durability = BASE_DURABILITY,
        defense = 5
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, defense)
