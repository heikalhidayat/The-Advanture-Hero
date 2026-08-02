# Import config base atribut
from config import BASE_HP, BASE_ENERGY, BASE_MANA, BASE_STRENGTH, BASE_AGILITY, BASE_DEFENSE, BASE_MAGIC, BASE_DEXTERITY, BASE_RESISTANCE

# Import config multiplier atribut
from config import BASE_HP_MULTIPLIER, BASE_ENERGY_MULTIPLIER, BASE_MANA_MULTIPLIER, BASE_STRENGTH_MULTIPLIER, BASE_AGILITY_MULTIPLIER, BASE_DEFENSE_MULTIPLIER, BASE_MAGIC_MULTIPLIER, BASE_DEXTERITY_MULTIPLIER, BASE_RESISTANCE_MULTIPLIER

# Import stat increase
from config import STAT_INCREASE_HP, STAT_INCREASE_ENERGY, STAT_INCREASE_MANA, STAT_INCREASE_STRENGTH, STAT_INCREASE_AGILITY, STAT_INCREASE_DEFENSE, STAT_INCREASE_MAGIC, STAT_INCREASE_DEXTERITY, STAT_INCREASE_RESISTANCE

class Karakter:
    def __init__(
        self,
        
        # Data Identitas & progresi
        name: str,
        job: str,
        level: int = 1,
        exp: int = 1,

        # Sumber daya utama
        hp: int = BASE_HP,
        energy: int = BASE_ENERGY,
        mana: int = BASE_MANA,

        # Core Stats class physical
        strength: int = BASE_STRENGTH,
        agility: int = BASE_AGILITY,
        defense: int = BASE_DEFENSE,
        vitality: int = 1,

        # Core stats class magical
        magic: int = BASE_MAGIC,
        dexterity: int = BASE_DEXTERITY,
        resistance: int = BASE_RESISTANCE,
        intelligence: int = 1,

        # Equipment
        strength_bonus: int = 0,
        agility_bonus: int = 0,
        defense_bonus: int = 0,
        magic_bonus: int = 0,
        dexterity_bonus: int = 0,
        resistance_bonus: int = 0,
    ):
        self.name = name
        self.job = job
        self.level = level
        self.exp = exp
        self.hp = hp
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
        self.strength_bonus = strength_bonus
        self.agility_bonus = agility_bonus
        self.defense_bonus = defense_bonus
        self.magic_bonus = magic_bonus
        self.dexterity_bonus = dexterity_bonus
        self.resistance_bonus = resistance_bonus
        self.max_hp = self.max_hp()
        self.max_energy = self.max_energy()
        self.max_mana = self.max_mana()
        self.max_exp = self.max_exp()

    def max_exp(self):
        return self.level ** 2 * 100

    def max_hp(self):
        return self.hp + (self.vitality * BASE_HP_MULTIPLIER)

    def max_energy(self):
        return self.energy + (self.vitality * BASE_ENERGY_MULTIPLIER)

    def max_mana(self):
        return self.mana + (self.intelligence * BASE_MANA_MULTIPLIER)

    def total_strength(self):
        return self.strength + (self.vitality * BASE_STRENGTH_MULTIPLIER) + self.strength_bonus

    def total_agility(self):
        return self.agility + (self.vitality * BASE_AGILITY_MULTIPLIER) + self.agility_bonus

    def total_defense(self):
        return self.defense + (self.vitality * BASE_DEFENSE_MULTIPLIER) + self.defense_bonus

    def total_magic(self):
        return self.magic + (self.intelligence * BASE_MAGIC_MULTIPLIER) + self.magic_bonus

    def total_dexterity(self):
        return self.dexterity + (self.intelligence * BASE_DEXTERITY_MULTIPLIER) + self.dexterity_bonus

    def total_resistance(self):
        return self.resistance + (self.intelligence * BASE_RESISTANCE_MULTIPLIER) + self.resistance_bonus

    def __repr__(self):
        return f'''======================\n<{self.name}>\n======================\n{self.job}\n \nLV.{self.level}[EXP:{self.exp}/{self.max_exp}]\nHP:{self.hp}/{self.max_hp}\nEnergy:{self.energy}/{self.max_energy}'''

    def exp_up(self, amount: int):
        self.exp += amount
        print(f"{self.name} mendapatkan {amount} EXP! ({self.exp}/{self.max_exp})")
        while self.exp >= self.max_exp:
            self.exp -= self.max_exp
            self.level_up()

    def level_up(self):
        self.level += 1
        
        # pulihkan sedikit HP ketika naik level
        self.hp = min(self.hp + 10, self.max_hp)

        # Tingkatkan atribut dasar
        self.max_hp += (STAT_INCREASE_HP * self.level)
        self.max.energy += (STAT_INCREASE_ENERGY * self.level)
        self.max.mana += (STAT_INCREASE_MANA * self.level)

        # Tingkatkan artibut tambahan
        self.strength += (STAT_INCREASE_STRENGTH * self.level)
        self.agility += (STAT_INCREASE_AGILITY * self.level)
        self.defense += (STAT_INCREASE_DEFENSE * self.level)
        self.magic += (STAT_INCREASE_MAGIC * self.level)
        self.dexterity += (STAT_INCREASE_DEXTERITY * self.level)
        self.resistance += (STAT_INCREASE_RESISTANCE * self.level)

        # Batas exp untuk level berikutnya
        self.max_exp *= 2

        print(f"LEVEL UP! {self.name} naik ke Level {self.level}")
        print(f"Batas EXP baru untuk level berikutnya: {self.max_exp}")

    def take_damage(self, strength: int) -> bool:
        """Kembalikan True jika ada HP yang berkurang, False jika seluruhnya diblock oleh defense."""
        sisa_damage = max(0, strength - self.defense)
        if sisa_damage > 0:
            self.hp = max(0, self.hp - sisa_damage)
            return True
        return False

    def attack(self, target: "Karakter") -> bool:
        total_damage = self.total_strength()
        print(f"{self.name} menyerang {target.name} dengan damage {total_damage}")
        terluka = target.take_damage(total_damage)
        if terluka:
            print(f"{target.name} terluka dengan damage {total_damage}")
            if target.hp <= 0:
                print(f"{target.name} mati!")
            return True
        else:
            print(f"Serangan kurang efektif!! Defense {target.name} sangat tinggi!!")
            return False

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
