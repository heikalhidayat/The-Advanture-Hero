from config import BASE_DURABILITY

class Strength(Equipment):
    def __init__(
        self,
        name: str,
        category: "Strength",
        kind: str,
        price: int,
        capasity: int,
        base_durability: int,
        strength: int
    ):
        super().__init__(name, category, kind, price, capasity, base_durability)
        self.strength = strength

    def total_strength(self, amount: int) -> int:
        self.strength += amount
        return self.strength

class GreatSword(Strength):
    def __init__(
        self,
        name = "Great Sword",
        category = "Strength",
        kind = "Weapon",
        price = 500,
        capasity = 8,
        base_durability = BASE_DURABILITY,
        strength = 20
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, strength)

class BattleAxe(Strength):
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
        capasity = 7,
        base_durability = BASE_DURABILITY,
        strength = 20
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, strength)

class LongSword(Strength):
    '''
    Pedang besi dua tangan standar.
    '''
    def __init__(
        self,
        name = "Long Sword",
        category = "Strength",
        kind = "Weapon",
        price = 150,
        capasity = 8,
        base_durability = BASE_DURABILITY,
        strength = 5
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, strength)

class Mace(Strength):
    def __init__(
        self,
        name = "Mace",
        category = "Strength",
        kind = "Weapon",
        price = 200,
        capasity = 8,
        base_durability = BASE_DURABILITY,
        strength = 10
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, strength)

class IronGauntlets(Strength):
    '''
    Sarung tangan besi yang menambah berat pukulan tangan.
    '''
    def __init__(
        slef,
        name = "Iron Gauntlets",
        category = "Strength",
        kind = "Armor",
        price = 100,
        capasity = 8,
        base_durability = BASE_DURABILITY,
        strength = 5
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, strength)
