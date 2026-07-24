class Karakter:
    """Base class untuk semua karakter permainan."""
    def __init__(
        self,
        name: str,
        max_exp: int = 100,
        max_hp: int = 100,
        level: int = 0,
        exp: int = 0,
        hp: int | None = None,
        energy: int = 100,
        damage: int = 10,
        agility: int = 10,
        defense: int = 10,
    ):
        self.name = name
        self.level = level
        self.exp = exp
        self.max_exp = max_exp
        self.max_hp = max_hp
        # Jika hp tidak diberikan, set ke max_hp. Jika diberikan, batasi ke max_hp.
        self.hp = max_hp if hp is None else min(hp, max_hp)
        self.energy = energy
        self.damage = damage
        self.agility = agility
        self.defense = defense
        self.is_armed = False
        self.weapon = None

    def __repr__(self):
        return f"<Karakter {self.name} L{self.level} HP:{self.hp}/{self.max_hp} EXP:{self.exp}/{self.max_exp}>"

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
        self.damage += 5
        self.agility += 5
        self.defense += 5
        # Batas exp untuk level berikutnya
        self.max_exp *= 2
        print(f"LEVEL UP! {self.name} naik ke Level {self.level}")
        print(f"Batas EXP baru untuk level berikutnya: {self.max_exp}")

    def take_damage(self, damage: int) -> bool:
        """Kembalikan True jika ada HP yang berkurang, False jika seluruhnya diblock oleh defense."""
        sisa_damage = max(0, damage - self.defense)
        if sisa_damage > 0:
            self.hp = max(0, self.hp - sisa_damage)
            return True
        return False

    def attack(self, target: "Karakter"):
        """Serang target; sertakan weapon jika ada."""
        base_damage = self.damage
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


class Mage(Karakter):
    def __init__(
        self,
        name: str,
        max_exp: int = 100,
        max_hp: int = 100,
        max_mana: int = 100,
        mana: int | None = None,
        level: int = 0,
        exp: int = 0,
        hp: int | None = None,
        energy: int = 100,
        damage: int = 30,
        agility: int = 10,
        defense: int = 10,
    ):
        super().__init__(name, max_exp, max_hp, level, exp, hp, energy, damage, agility, defense)
        self.max_mana = max_mana
        self.mana = max_mana if mana is None else min(mana, max_mana)

    def level_up(self):
        super().level_up()
        self.max_mana += 10
        self.mana = min(self.mana + 10, self.max_mana)
        print(f"Mana {self.name} bertambah! Mana sekarang: {self.mana}/{self.max_mana}")

    def cast_spell(self, cost: int) -> str:
        if cost <= 0:
            return f"{self.name} tidak melakukan apa-apa."
        if self.mana >= cost:
            self.mana -= cost
            return f"{self.name} melakukan sihir! Mana berkurang {cost}."
        return f"{self.name} tidak memiliki mana yang cukup!"

    def restore_mana(self, amount: int) -> bool:
        if amount <= 0:
            return False
        old = self.mana
        self.mana = min(self.mana + amount, self.max_mana)
        return self.mana > old


class Warrior(Karakter):
    def __init__(
        self,
        name: str,
        max_exp: int = 100,
        max_hp: int = 120,
        aura: int = 50,
        level: int = 0,
        exp: int = 0,
        hp: int | None = None,
        energy: int = 100,
        damage: int = 20,
        agility: int = 15,
        defense: int = 15,
    ):
        super().__init__(name, max_exp, max_hp, level, exp, hp, energy, damage, agility, defense)
        self.aura = aura

    def cast_aura(self, amount: int) -> str:
        if amount <= 0:
            return f"{self.name} tidak melakukan apa-apa."
        if self.aura >= amount:
            self.aura -= amount
            return f"{self.name} mengeluarkan aura! Aura berkurang {amount}."
        return f"{self.name} tidak memiliki aura yang cukup!"

    def level_up(self):
        super().level_up()
        self.aura += 10
        print(f"Aura {self.name} bertambah! Aura sekarang: {self.aura}")


class Guardian(Karakter):
    def __init__(
        self,
        name: str,
        max_exp: int = 100,
        max_hp: int = 140,
        level: int = 0,
        exp: int = 0,
        hp: int | None = None,
        energy: int = 100,
        damage: int = 10,
        agility: int = 10,
        defense: int = 30,
    ):
        super().__init__(name, max_exp, max_hp, level, exp, hp, energy, damage, agility, defense)


class Assassin(Karakter):
    def __init__(
        self,
        name: str,
        max_exp: int = 100,
        max_hp: int = 100,
        level: int = 0,
        exp: int = 0,
        hp: int | None = None,
        energy: int = 100,
        damage: int = 15,
        agility: int = 25,
        defense: int = 15,
    ):
        super().__init__(name, max_exp, max_hp, level, exp, hp, energy, damage, agility, defense)


class Archer(Karakter):
    def __init__(
        self,
        name: str,
        max_exp: int = 100,
        max_hp: int = 100,
        aura: int = 50,
        level: int = 0,
        exp: int = 0,
        hp: int | None = None,
        energy: int = 100,
        damage: int = 20,
        agility: int = 20,
        defense: int = 10,
    ):
        super().__init__(name, max_exp, max_hp, level, exp, hp, energy, damage, agility, defense)
        self.aura = aura
