from typing import Required
# Import stat increase
from config import (
    STAT_INCREASE_ENERGY, 
    STAT_INCREASE_MANA, 
    STAT_INCREASE_STRENGTH,
    STAT_INCREASE_AGILITY,
    STAT_INCREASE_DEFENSE,
    STAT_INCREASE_MAGIC, 
    STAT_INCREASE_DEXTERITY,
    STAT_INCREASE_RESISTANCE, 
    STAT_INCREASE_INTELLIGENCE, 
    STAT_INCREASE_VITALITY
)

class Skills:
    def __init__(
        self,
        name: str,
        category: str,
        armed: bool,
        range_type: str,
        debuff: str,
        level: int,
        competence: int,
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
        # Information
        self.name = name
        self.category = category
        self.armed = armed
        self.range_type = range_type
        self.debuff = debuff
        self.level = level
        self.competence = competence

        # Stats
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

    @property
    def max_competence(self):
        return self.level ** 2 * 100

    @classmethod
    def from_db_row(cls, row):
        required = {"name", "category", "armed", "range_type", "debuff", "level", "competence", "energy", "mana", "strength", "agility", "defense", "vitality", "magic", "dexterity", "resistance", "intelligence"}
        missing = required - set(row.keys())
        if missing:
            raise KeyError(f"Missing fields: {missing}")
        return cls(
            name=row["name"],
            category=row["category"],
            armed=bool(row.get("armed")),
            range_type=row["range_type"],
            debuff=row["debuff"],
            level=int(row("level",1)),
            competence=int(row("competence",0)),
            energy=int(row("energy",0)),
            mana=int(row("mana",0)),
            strength=int(row("strength",0)),
            agility=int(row("agility",0)),
            defense=int(row("defense",0)),
            vitality=int(row("vitality",0)),
            magic=int(row("magic",0)),
            dexterity=int(row("dexterity",0)),
            resistance=int(row("resistance",0)),
            intelligence=int(row("intelligence",0))
        )

    def level_up(self):
        self.level += 1
        # Naikkan persyaratan stats
        stat_increases = {
            "energy": STAT_INCREASE_ENERGY,
            "mana": STAT_INCREASE_MANA,
            "strength": STAT_INCREASE_STRENGTH,
            "agility": STAT_INCREASE_AGILITY,
            "defense": STAT_INCREASE_DEFENSE,
            "vitality": STAT_INCREASE_VITALITY,
            "magic": STAT_INCREASE_MAGIC,
            "dexterity": STAT_INCREASE_DEXTERITY,
            "resistance": STAT_INCREASE_RESISTANCE,
            "intelligence": STAT_INCREASE_INTELLIGENCE
        }

        category_stats = {
            "Physical": ["strength", "agility", "defense", "vitality", "dexterity"],
            "Magical": ["mana", "magic", "resistance", "intelligence"]
        }

        stats_to_update = ["energy"] + category_stats.get(self.category, [])

        for stat_name in stats_to_update:
            old_value = getattr(self, stat_name)
            increase = stat_increases[stat_name]
            setattr(self, stat_name, old_value + (increase * self.level))
        print(f"LEVEL SKILL UP! {self.name} naik ke Level {self.level}")

    def gain_experience(self, amount: int):
        '''Tambah pengalaman skill dan level up jika cukup'''
        self.competence += amount
        while self.competence >= self.max_competence:
            self.competence -= self.max_competence
            self.level_up()

    def activate_skill(self, player_stats: dict) -> str:
        reqs = {
            "Level": self.level,
            "Energy": self.energy,
            "Mana": self.mana,
            "Strength": self.strength,
            "Agility": self.agility,
            "Defense": self.defense,
            "Vitality": self.vitality,
            "Magic": self.magic,
            "Dexterity": self.dexterity,
            "Resistance": self.resistance,
            "Intelligence": self.intelligence,
        }
        missing = [name for name, required in reqs.items() if player_stats.get(name.lower(), 0) < required]

        if not missing:
            return f"{self.name} activated"
        
        return f"({', '.join(missing)}) tidak memenuhi persyaratan"
 
    def __repr__(self) -> str:
        return f"Skills(name={self.name!r}, category={self.category!r}, armed={self.armed}, range_type={self.range_type!r}, debuff={self.debuff!r}, level={self.level})"

    def __str__(self) -> str:
        return (
            "=============================\n"
            f"<{self.name}>\tLV.{self.level}\n"
            "=============================\n"
            f"{self.competence}/{self.max_competence}\n\n"
            f"Category: {self.category}\n"
            f"Armed: {self.armed}\n"
            f"Range Type: {self.range_type}\n"
            f"Debuff: {self.debuff}\n"
            f"Energy: {self.energy}\n"
            f"Mana: {self.mana}\n"
            f"Strength: {self.strength}\n"
            f"Agility: {self.agility}\n"
            f"Defense: {self.defense}\n"
            f"Vitality: {self.vitality}\n"
            f"Magic: {self.magic}\n"
            f"Dexterity: {self.dexterity}\n"
            f"Resistance: {self.resistance}\n"
            f"Intelligence: {self.intelligence}\n"
          )
        
# Example 
player_stats = {
      "Level": 1,
      "Energy": 100,
      "Mana": 100,
      "Strength": 50,
      "Agility": 100,
      "Defense": 100,
      "Vitality": 100,
      "Magic": 100,
      "Dexterity": 100,
      "Resistance": 100,
      "Intelligence": 100,
}

stats_lower = {key.lower(): value for key, value in player_stats.items()}
