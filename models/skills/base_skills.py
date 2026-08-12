class Skills:
    def __init__(
        self,
        name: str,
        category: str,
        armed: bool,
        range_type: str,
        debuff: str,
        durability: int,
        level: int,
        energy: int,
        mana: int,
        strength: int,
        agility: int,
        defense: int,
        vitality: int,
        magic: int,
        dexterity: int,
        resistance: int,
        intelligence: int
    ):
        self.name = name
        self.category = category
        self.armed = armed
        self.range_type = range_type
        self.debuff = debuff
        self.durability = durability
        self.level = level
        self.energy = energy
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.defense = defense
        self.vitality = vitality
        self.magic = magic
        self.dexterity = dexterity
        self.resistance = resistance
        self.intelligence = intelligence

    @classmethod
    def from_db_row(cls, row):
        return cls(
            name=row["name"],
            category=row["category"],
            armed=row["armed"],
            range_type=row["range_type"],
            debuff=row["debuff"],
            durability=row["durability"],
            level=row["level"],
            energy=row["energy"],
            mana=row["mana"],
            strength=row["strength"],
            agility=row["agility"],
            defense=row["defense"],
            vitality=row["vitality"],
            magic=row["magic"],
            dexterity=row["dexterity"],
            resistance=row["resistance"],
            intelligence=row["intelligence"]
        )

    def activate_skill(
        self,
        player_level,
        player_energy,
        player_mana,
        player_strength,
        player_agility,
        player_defense,
        player_vitality,
        player_magic,
        player_dexterity,
        player_resistance,
        player_intelligence
    ) -> str:

        missing = list([])

        if self.level > player_level:
            missing.append("level")
        if self.energy > player_energy:
            missing.append("energy")
        if self.mana > player_mana:
            missing.append("mana")
        if self.strength > player_strength:
            missing.append("strength")
        if self.agility > player_agility:
            missing.append("agility")
        if self.defense > player_defense:
            missing.append("defense")
        if self.vitality > player_vitality:
            missing.append("vitality")
        if self.magic > player_magic:
            missing.append("magic")
        if self.dexterity > player_dexterity:
            missing.append("dexterity")
        if self.resistance > player_resistance:
            missing.append("resistance")
        if self.intelligence > player_intelligence:
            missing.append("intelligence")

        if len(missing) == 0:
            return f"{self.name} activated"
        else:
            for i, item in enumerate(missing):
                missing[i] = item.capitalize()
                return f"({', '.join(missing)}) tidak memenuhi persyaratan"
