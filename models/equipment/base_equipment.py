class Equipment:
    def __init__(
        self,
        name: str,
        category: str,
        kind: str,
        price: int,
        capasity: int,
        base_durability: int,
    ):
        self.name = name
        self.category = category
        self.kind = kind
        self.price = price
        self.capasity = capasity
        self.base_durability = base_durability
        self.current_durability = base_durability
    
    def repair(self, amount: int) -> int:
        self.current_durability += amount
        if self.current_durability > self.base_durability:
            self.current_durability = self.base_durability
        return self.current_durability
    
    def use(self, amount: int) -> int:
        self.current_durability -= amount
        if self.current_durability < 0:
            self.current_durability = 0
        return self.current_durability

    def __repr__(self) -> str:
        try:
            dur_max = self.base_durability
        except Exception:
            dur_max = "?"
        return f"{self.name!r} ({self.category!r}, {self.kind!r}, {self.current_durability}/{dur_max})"

    def __str__(self) -> str:
        return (
            "====================\n"
            f"< {self.name.upper()} >\n"
            "====================\n"
            f"[{self.current_durability}/{self.base_durability}]\n\n"
            f"Category: {self.category}\n"
            f"Kind: {self.kind}"
        )
