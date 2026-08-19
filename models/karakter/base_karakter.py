# Import config base atribut
from config import (
    # Import config base atribut
    BASE_HP, BASE_ENERGY, BASE_MANA, BASE_STRENGTH, BASE_AGILITY, BASE_DEFENSE,
    BASE_MAGIC, BASE_DEXTERITY, BASE_RESISTANCE,
    # Import config multiplier atribut
    BASE_HP_MULTIPLIER, BASE_ENERGY_MULTIPLIER, BASE_MANA_MULTIPLIER,
    BASE_STRENGTH_MULTIPLIER, BASE_AGILITY_MULTIPLIER,
    BASE_DEFENSE_MULTIPLIER, BASE_MAGIC_MULTIPLIER, BASE_DEXTERITY_MULTIPLIER,
    BASE_RESISTANCE_MULTIPLIER,
    # Import stat increase
    STAT_INCREASE_HP, STAT_INCREASE_ENERGY, STAT_INCREASE_MANA,
    STAT_INCREASE_STRENGTH, STAT_INCREASE_AGILITY, STAT_INCREASE_DEFENSE,
    STAT_INCREASE_MAGIC, STAT_INCREASE_DEXTERITY, STAT_INCREASE_RESISTANCE,
    # Import slot skil
    SLOT_SKILL, BASE_CAPASITY_SKILL
)

class Karakter:
    def __init__(
        self,
        name: str,
        job: str,
        tier: int,
        level: int,
        exp: int,
        skill_01: str,
        skill_02: str,
        skill_03: str,
        skill_04: str,
        # base values
        base_hp: int = BASE_HP,
        base_energy: int = BASE_ENERGY,
        base_mana: int = BASE_MANA,
        # core stats
        strength: int = BASE_STRENGTH,
        agility: int = BASE_AGILITY,
        defense: int = BASE_DEFENSE,
        vitality: int = 1,
        magic: int = BASE_MAGIC,
        dexterity: int = BASE_DEXTERITY,
        resistance: int = BASE_RESISTANCE,
        intelligence: int = 1,
        # equipment bonuses
        strength_bonus: int = 0,
        agility_bonus: int = 0,
        defense_bonus: int = 0,
        magic_bonus: int = 0,
        dexterity_bonus: int = 0,
        resistance_bonus: int = 0,
    ):
        self.name = name
        self.job = job
        self.tier = tier
        self.level = level
        self.exp = exp
        self.skill_01 = skill_01
        self.skill_02 = skill_02
        self.skill_03 = skill_03
        self.skill_04 = skill_04

        # base values and current values
        self.base_hp = base_hp
        self.current_hp = base_hp
        self.base_energy = base_energy
        self.current_energy = base_energy
        self.base_mana = base_mana
        self.current_mana = base_mana

        # stats
        self.strength = strength
        self.agility = agility
        self.defense = defense
        self.vitality = vitality
        self.magic = magic
        self.dexterity = dexterity
        self.resistance = resistance
        self.intelligence = intelligence

        # bonuses
        self.strength_bonus = strength_bonus
        self.agility_bonus = agility_bonus
        self.defense_bonus = defense_bonus
        self.magic_bonus = magic_bonus
        self.dexterity_bonus = dexterity_bonus
        self.resistance_bonus = resistance_bonus

        # derived persisted value
        self.max_exp = self.compute_max_exp()

    def compute_max_exp(self) -> int:
        return self.level ** 2 * 100

    @classmethod
    def from_db_row(cls, row):
        return cls(
            name=row["name"],
            job=row["job"],
            tier=row["tier"],
            level=row["level"],
            exp=row["exp"],
            base_hp=row["base_hp"],
            base_energy=row["base_energy"],
            base_mana=row["base_mana"],
            strength=row["strength"],
            agility=row["agility"],
            defense=row["defense"],
            vitality=row["vitality"],
            magic=row["magic"],
            dexterity=row["dexterity"],
            resistance=row["resistance"],
            intelligence=row["intelligence"],
            strength_bonus=row["strength_bonus"],
            agility_bonus=row["agility_bonus"],
            defense_bonus=row["defense_bonus"],
            magic_bonus=row["magic_bonus"],
            dexterity_bonus=row["dexterity_bonus"],
            resistance_bonus=row["resistance_bonus"],
        )

    @property
    def dict_karaker(self) -> dict:
        dict_karaker = {
            "Level": self.level,
            "Energy": self.base_energy,
            "Mana": self.base_mana,
            "Strength": self.strength,
            "Agility": self.agility,
            "Defense": self.defense,
            "Vitality": self.vitality,
            "Magic": self.magic,
            "Dexterity": self.dexterity,
            "Resistance": self.resistance,
            "Intelligence": self.intelligence,
        }

        return dict_karaker

    @property
    def max_hp(self) -> int:
        return self.base_hp + (self.vitality * self.tier * BASE_HP_MULTIPLIER)

    @property
    def max_energy(self) -> int:
        return self.base_energy + (self.vitality * self.tier * BASE_ENERGY_MULTIPLIER)

    @property
    def max_mana(self) -> int:
        return self.base_mana + (self.intelligence * self.tier * BASE_MANA_MULTIPLIER)

    def total_strength(self) -> int:
        return self.strength + (self.vitality * self.tier * BASE_STRENGTH_MULTIPLIER) + self.strength_bonus

    def total_agility(self) -> int:
        return self.agility + (self.vitality * self.tier * BASE_AGILITY_MULTIPLIER) + self.agility_bonus

    def total_defense(self) -> int:
        return self.defense + (self.vitality * self.tier * BASE_DEFENSE_MULTIPLIER) + self.defense_bonus

    def total_magic(self) -> int:
        return self.magic + (self.intelligence * self.tier * BASE_MAGIC_MULTIPLIER) + self.magic_bonus

    def total_dexterity(self) -> int:
        return self.dexterity + (self.intelligence * self.tier * BASE_DEXTERITY_MULTIPLIER) + self.dexterity_bonus

    def total_resistance(self) -> int:
        return self.resistance + (self.intelligence * self.tier * BASE_RESISTANCE_MULTIPLIER) + self.resistance_bonus

    def level_up(self):
        self.level += 1
        # restore sedikit current HP
        self.current_hp = min(self.current_hp + 10, self.max_hp)
        # naikkan base stats
        self.base_hp += (STAT_INCREASE_HP * 1)
        self.base_energy += (STAT_INCREASE_ENERGY * self.level)
        self.base_mana += (STAT_INCREASE_MANA * self.level)
        self.strength += (STAT_INCREASE_STRENGTH * self.level)
        self.agility += (STAT_INCREASE_AGILITY * self.level)
        self.defense += (STAT_INCREASE_DEFENSE * self.level)
        self.magic += (STAT_INCREASE_MAGIC * self.level)
        self.dexterity += (STAT_INCREASE_DEXTERITY * self.level)
        self.resistance += (STAT_INCREASE_RESISTANCE * self.level)
        # recompute exp cap
        self.max_exp = self.compute_max_exp()
        print(f"LEVEL UP! {self.name} naik ke Level {self.level}")

    def gain_exp(self, amount: int):
        self.exp += amount
        while self.exp >= self.max_exp:
            self.exp -= self.max_exp
            self.level_up()

    def __repr__(self) -> str:
        try:
            exp_cap = self.max_exp
        except Exception:
            exp_cap = "?"
        return f"Karakter(name={self.name!r}, job={self.job!r}, level={self.level}, exp={self.exp}/{exp_cap})"

    def __str__(self) -> str:
        hp_cur = getattr(self, "current_hp", getattr(self, "hp", "?"))
        hp_max = getattr(self, "max_hp", "?")
        energy_cur = getattr(self, "current_energy", getattr(self, "energy", "?"))
        en_max = getattr(self, "max_energy", "?")
        mana_cur = getattr(self, "current_mana", getattr(self, "mana", "?"))
        ma_max = getattr(self, "max_mana", "?")

        def safe_total(name):
            attr = getattr(self, name, None)
            try:
                return attr() if callable(attr) else attr
            except Exception:
                return "?"

        return (
            "======================\n"
            f"<{self.name}>\n"
            "======================\n"
            f"{self.job}\t[{self.tier}]\n\n"
            f"LV.{self.level} [EXP: {self.exp}/{self.max_exp}]\n"
            f"HP: {hp_cur}/{hp_max}\n"
            f"Energy: {energy_cur}/{en_max}\n"
            f"Mana: {mana_cur}/{ma_max}\n\n"
            f"STR: {safe_total('total_strength')} | AGI: {safe_total('total_agility')} | DEF: {safe_total('total_defense')}\n"
            f"MGC: {safe_total('total_magic')} | DEX: {safe_total('total_dexterity')} | RES: {safe_total('total_resistance')}\n"
        )

    def __str_monster__(self) -> str:
        hp_cur = getattr(self, "current_hp", getattr(self, "hp", "?"))
        hp_max = getattr(self, "max_hp", "?")
        energy_cur = getattr(self, "current_energy", getattr(self, "energy", "?"))
        en_max = getattr(self, "max_energy", "?")
        mana_cur = getattr(self, "current_mana", getattr(self, "mana", "?"))
        ma_max = getattr(self, "max_mana", "?")

        def safe_total(name):
            attr = getattr(self, name, None)
            try:
                return attr() if callable(attr) else attr
            except Exception:
                return "?"

        return (
            "======================\n"
            f"<{self.name}>\n"
            "======================\n"
            f"{self.job}\t[{self.tier}]\n\n"
            f"LV.{self.level} [EXP: {self.exp}]\n"
            f"HP: {hp_cur}/{hp_max}\n"
            f"Energy: {energy_cur}/{en_max}\n"
            f"STR: {safe_total('total_strength')} | AGI: {safe_total('total_agility')} | DEF: {safe_total('total_defense')}\n"
        )

    def use_energy(self, amount: int) -> bool:
        """Kurangi energy jika cukup, kembalikan True; jika tidak cukup, jangan ubah energy dan kembalikan False."""
        if amount <= 0:
            return True
        if amount > self.energy:
            print(f"{self.name} tidak memiliki energy yang cukup!")
            return False
        self.energy -= amount
        return True

    def use_mana(self, amount: int) -> bool:
        """Kurangi mana jika cukup, kembalikan True; jika tidak cukup, jangan ubah mana dan kembalikan False."""
        if amount <= 0:
            return True
        if amount > self.mana:
            print(f"{self.name} tidak memiliki mana yang cukup!")
            return False
        self.mana -= amount
        return True

    def heal_hp(self, amount: int) -> bool:
        """Pulihkan HP, jangan melebihi max_hp."""
        if amount <= 0:
            return False
        old = self.hp
        self.hp = min(self.hp + amount, self.max_hp)
        print(f"{self.name} memulihkan HP sebesar {self.hp - old}. HP sekarang: {self.hp}/{self.max_hp}")
        return True

    def heal_energy(self, amount: int) -> bool:
        """Pulihkan Energy, jangan melebihi max_energy."""
        if amount <= 0:
            return False
        old = self.energy
        self.energy = min(self.energy + amount, self.max_energy)
        print(f"{self.name} memulihkan Energy sebesar {self.energy - old}. Energy sekarang: {self.energy}/{self.max_energy}")
        return True

    def heal_mana(self, amount: int) -> bool:
        """Pulihkan Mana, jangan melebihi max_mana."""
        if amount <= 0:
            return False
        old = self.mana
        self.mana = min(self.mana + amount, self.max_mana)
        print(f"{self.name} memulihkan Mana sebesar {self.mana - old}. Mana sekarang: {self.mana}/{self.max_mana}")
        return True

    def take_damage(self, amount: int) -> bool:
        effective = max(0, amount - self.total_defense())
        if effective > 0:
            self.current_hp = max(0, self.current_hp - effective)
            return True
        return False

    def attack(self, target: "Karakter") -> bool:
        dmg = self.total_strength()
        print(f"{self.name} menyerang {target.name} dengan damage {dmg}")
        if target.take_damage(dmg):
            print(f"{target.name} terluka; HP: {target.current_hp}/{target.max_hp}")
            if target.current_hp <= 0:
                print(f"{target.name} mati!")
            return True
        else:
            print(f"Serangan kurang efektif—pertahanan {target.name} sangat tinggi.")
            return False
