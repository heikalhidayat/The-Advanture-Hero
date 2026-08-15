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
