class Defense(Equipment):
    def __init__(
        self,
        name: str,
        category: "Defense",
        kind: str,
        capasity: int,
        base_durability: int,
        defense: int
    ):
        super().__init__(name, category, kind, capasity, base_durability)
        self.defense = defense

    def total_defense(self, amount: int) -> int:
        self.defense += amount
        return self.defense
