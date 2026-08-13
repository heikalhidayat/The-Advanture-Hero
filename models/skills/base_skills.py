# Import stat increase
from config import STAT_INCREASE_HP, STAT_INCREASE_ENERGY, STAT_INCREASE_MANA, STAT_INCREASE_STRENGTH, STAT_INCREASE_AGILITY, STAT_INCREASE_DEFENSE, STAT_INCREASE_MAGIC, STAT_INCREASE_DEXTERITY, STAT_INCREASE_RESISTANCE, STAT_INCREASE_INTELLIGENCE, STAT_INCREASE_VITALITY


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

        # recompute max competence
        self.max_competence = self.compute_max_competence()

    def compute_max_competence(self):
        return self.level ** 2 * 100

    @classmethod
    def from_db_row(cls, row):
        return cls(
            name=row["name"],
            category=row["category"],
            armed=row["armed"],
            range_type=row["range_type"],
            debuff=row["debuff"],
            level=row["level"],
            competence=row["competence"],
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
    
    def level_up(self):
        self.level += 1
        # Naikkan persyaratan stats
        self.energy += (STAT_INCREASE_ENERGY * self.level)
        self.mana += (STAT_INCREASE_MANA * self.level)
        self.strength += (STAT_INCREASE_STRENGTH * self.level)
        self.agility += (STAT_INCREASE_AGILITY * self.level)
        self.defense += (STAT_INCREASE_DEFENSE * self.level)
        self.vitality += (STAT_INCREASE_VITALITY * self.level)
        self.magic += (STAT_INCREASE_MAGIC * self.level)
        self.dexterity += (STAT_INCREASE_DEXTERITY * self.level)
        self.resistance += (STAT_INCREASE_RESISTANCE * self.level)
        self.intelligence += (STAT_INCREASE_INTELLIGENCE * self.level)
        # recompute competence cap
        self.max_competence = self.compute_max_competence()
        print(f"LEVEL SKILL UP! {self.name} naik ke Level {self.level}")
    
    def up(self):
        while self.competence >= self.max_competence:
            self.competence -= self.max_competence
            self.level_up()

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
