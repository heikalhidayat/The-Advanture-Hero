from config import BASE_HP, BASE_ENERGY, BASE_STRENGTH, BASE_AGILITY, BASE_DEFENSE

class Karakter:
    def __init__(
        self,
        
        # Data Identitas & progresi
        name: str,
        job: str,
        level: int = 0,
        exp: int = 0,

        # Sumber daya utama
        hp: int = BASE_HP,
        energy: int = BASE_ENERGY,

        # Core Stats
        strength: int = BASE_STRENGTH,
        agility: int = BASE_AGILITY,
        defense: int = BASE_DEFENSE,

        # Equipment
        strength_bonus: int = 0,
        agility_bonus: int = 0,
        defense_bonus: int = 0,
    ):
        self.name = name
        self.job = job
        self.level = level
        self.exp = exp
        self.hp = hp
        self.energy = energy
        self.strength = strength
        self.agility = agility
        self.defense = defense
        self.strength_bonus = strength_bonus
        self.agility_bonus = agility_bonus
        self.defense_bonus = defense_bonus

    def __repr__(self):
        return f"<{self.name}>\t\tL.{self.level}\nHP:{self.hp}/{self.max_hp}\t\tEXP:{self.exp}/{self.max_exp}>"

    def exp_up(self, amount: int):
        self.exp += amount
        print(f"{self.name} mendapatkan {amount} EXP! ({self.exp}/{self.max_exp})")
        while self.exp >= self.max_exp:
            self.exp -= self.max_exp
            self.level_up()

    def level_up(self):
        self.level += 1
        # Naikkan max_hp, dan pulihkan sedikit HP ketika naik level
        self.max_hp += 10
        self.hp = min(self.hp + 10, self.max_hp)
        # Energy dan atribut lain
        self.energy += 10
        self.strength += 5
        self.agility += 5
        self.defense += 5
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

    def attack(self, target: "Karakter"):
        """Serang target; sertakan weapon jika ada."""
        base_damage = self.strength
        weapon_damage = 0
        if self.is_armed and getattr(self.weapon, "damage", None) is not None:
            weapon_damage = self.weapon.damage
        total_damage = base_damage + weapon_damage
        print(f"{self.name} menyerang {target.name} dengan damage {total_damage}")
        terluka = target.take_damage(total_damage)
        if terluka:
            print(f"{target.name} terluka dengan damage {total_damage}")
        else:
            print(f"Serangan kurang efektif!! Defense {target.name} sangat tinggi!!")

    def use_energy(self, amount: int) -> bool:
        """Kurangi energy jika cukup, kembalikan True; jika tidak cukup, jangan ubah energy dan kembalikan False."""
        if amount <= 0:
            return True
        if amount > self.energy:
            print(f"{self.name} tidak memiliki energy yang cukup!")
            return False
        self.energy -= amount
        return True

    def heal(self, amount: int) -> bool:
        """Pulihkan HP, jangan melebihi max_hp."""
        if amount <= 0:
            return False
        old = self.hp
        self.hp = min(self.hp + amount, self.max_hp)
        print(f"{self.name} memulihkan HP sebesar {self.hp - old}. HP sekarang: {self.hp}/{self.max_hp}")
        return True
