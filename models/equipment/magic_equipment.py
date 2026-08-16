from config import BASE_DURABILITY
from base_equipment import Equipment

class Magic(Equipment):
    def __init__(
        self,
        name: str,
        category: "Magic",
        kind: str,
        price: int,
        capasity: int,
        base_durability: int,
        magic: int
    ):
        super().__init__(name, category, kind, price, capasity, base_durability)
        self.magic = magic

    def total_magic(self, amount: int) -> int:
        self.magic += amount
        return self.magic

class WoodenStaff(Magic):
    '''
    Tongkat kayu tua berinti kristal mentah yang berfungsi
    untuk memfokuskan sihir.
    '''
    def __init__(
        self,
        name = "Wooden Staff",
        category = "Magic",
        kind = "Weapon",
        price = 120,
        capasity = 3,
        base_durability = BASE_DURABILITY,
        magic = 5
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, magic)

class MagicWand(Magic):
    '''
    Tongkat sihir pendek yang dapat meningkatkan daya hancur.
    '''
    def __init__(
        self,
        name = "Magic Wand",
        category = "Magic",
        kind = "Weapon",
        price = 500,
        capasity = 3,
        base_durability = BASE_DURABILITY,
        magic = 15
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, magic)

class SilkRobe(Magic):
    '''
    Jubah sutra yang ditenun menggunakan benang khusus penyerap mana.
    '''
    def __init__(
        self,
        name = "Silk Robe",
        category = "Magic",
        kind = "Armor",
        price = 200,
        capasity = 3,
        base_durability = BASE_DURABILITY,
        magic = 6
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, magic)

class MageHat(Magic):
    '''
    Topi kain berujung lancip yang membantu mempertajam konsentrasi.
    '''
    def __init__(
        self,
        name = "Mage Hat",
        category = "Magic",
        kind = "Armor",
        price = 100,
        capasity = 3,
        base_durability = BASE_DURABILITY,
        magic = 3
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, magic)

class CrystalRing(Magic):
    '''
    Cincin yang terkoneksi langsung dengan kapasitas mana.
    '''
    def __init__(
        self,
        name = "Crystal Ring",
        category = "Magic",
        kind = "Accessory",
        price = 300,
        capasity = 3,
        base_durability = BASE_DURABILITY,
        magic = 10
    ):
        super().__init__(name, category, kind, price, capasity, base_durability, magic)
