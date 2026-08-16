from config import BASE_DURABILITY
from base_equipment import Equipment

class Resistance(Equipment):
    def __init__(
        self,
        name: str,
        category: "Resistance",
        kind: str,
        price: int,
        capasity: int,
        base_durability: int,
        resistance: int
    ):
        super().__init__(name, category, kind, price, capasity, base_durability)
        self.resistance = resistance

    def total_resistance(self, amount: int) -> int:
        self.resistance += amount
        return self.resistance

class HeavyCloak(Resistance):
    '''
    Jubal wol tebal berlapis zat anti-bakar.
    '''
    def __init__(
        self,
        name = "Heavy Cloak",
        category = "Resistance",
        kind = "Armor",
        price = 250,
        capasity = 3,
        base_durability = BASE_DURABILITY,
        resistance = 8
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, resistance)

class LeatherVest(Resistance):
    '''
    Rompi kulit yang dinetralkan menggunakan ramuan khusus.
    '''
    def __init__(
        self,
        name = "Leather Vest",
        category = "Resistance",
        kind = "Armor",
        price = 180,
        capasity = 3,
        base_durability = BASE_DURABILITY,
        resistance = 5
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, resistance)

class JadeRing(Resistance):
    '''
    Cincin dari batu giok hijau penangkal kutukan.
    '''
    def __init__(
        self,
        name = "Jade Ring",
        category = "Resistance",
        kind = "Armor",
        price = 300,
        capasity = 1,
        base_durability = BASE_DURABILITY,
        resistance = 7
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, resistance)

class Talisman(Resistance):
    '''
    Jimat kertas bertuliskan mantra pelindung.
    '''
    def __init__(
        self,
        name = "Talisman",
        category = "Resistance",
        kind = "Accessory",
        price = 200,
        capasity = 1,
        base_durability = BASE_DURABILITY,
        resistance = 4
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, resistance)
