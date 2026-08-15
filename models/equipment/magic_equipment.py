class Magic(Equipment):
    def __init__(
        self,
        name: str,
        category: "Magic",
        kind: str,
        capasity: int,
        base_durability: int,
        magic: int
    ):
        super().__init__(name, category, kind, capasity, base_durability)
        self.magic = magic

    def total_magic(self, amount: int) -> int:
        self.magic += amount
        return self.magic
