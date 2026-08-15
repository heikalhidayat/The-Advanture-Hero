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
