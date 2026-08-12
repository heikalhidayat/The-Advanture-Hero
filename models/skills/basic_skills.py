class Skills:
    def __init__(
        self,
        name: str,
        category: str,
        armed: bool,
        range_type: str,
        debuff: str,
        durability: int,
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
        self.energy = energy
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.defense = defense
        self.vitality = vitality
        self.magic = magic
        self.dexterity = dexterity
        self.resistance = resistance

    @classmethod
    def from_db_row(cls, row):
        return cls(
            name=row["name"],
            category=row["category"],
            armed=row["armed"],
            range_type=row["range_type"],
            debuff=row["debuff"],
            durability=row["durability"],
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
    ):
        if self.energy <= player_energy & self.mana <= player_mana & self.strength <= player_strength & self.agility <= player_agility & self.defense <= player_defense & self.vitality <= player_vitality & self.magic <= player_magic & self.dexterity <= player_dexterity & self.resistance <= player_resistance & self.intelligence <= player_intelligence:
            return f"{self.name} activated"
        else:
            return f"{self.name} not activated"
