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
        super().__init__(name, category, kind, capasity, base_durability)
        self.agility = agility

    def total_agility(self, amount: int) -> int:
        self.agility += amount
        return self.agility
