class Equipment:
    def __init__(
        self,
        # Information
        name: str,
        category: str,
        kind: str,
        price: int,
        capasity: int,
        # Base Values
        base_durability: int,
        # Core Stats
        strenth: int,
        agility: int,
        defense: int, 
        magic: int,
        dexterity: int, 
        resistance: int,
    ):
        # Information
        self.name = name
        self.category = category
        self.kind = kind
        self.price = price
        self.capasity = capasity

        # Base Values
        self.base_durability = base_durability
        self.current_durability = base_durability

        # Core Stats
        self.strenth = strenth
        self.agility = agility
        self.defense = defense
        self.magic = magic
        self.dexterity = dexterity
        self.resistance = resistance

    def total_strenth(self, amount: int) -> int:
        self.strenth += amount
        return self.strenth

    def total_agility(self, amount: int) -> int:
        self.agility += amount
        return self.agility

    def total_defense(self, amount: int) -> int:
        self.defense += amount
        return self.defense

    def total_magic(self, amount: int) -> int:
        self.magic += amount
        return self.magic

    def total_dexterity(self, amount: int) -> int:
        self.dexterity += amount
        return self.dexterity

    def total_resistance(self, amount: int) -> int:
        self.resistance += amount
        return self.resistance

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
            f"Kind: {self.kind}\n"
            f"Str: {self.strenth} | Agi: {self.agility} | Def: {self.defense}\n"
            f"Mag: {self.magic} | Dex: {self.dexterity} | Res: {self.resistance}\n"
        )