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
