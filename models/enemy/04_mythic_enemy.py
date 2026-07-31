class Enemy:
    '''Base class untuk semua monster'''
    def __init__(
        self, 
        # Indentitas & progresi
        name: str,
        monster_type: str,
        level: int = 0,
        
        # Pools
        hp: int = 100, 
        energy: int = 100,

        # Core Stats 
        strength: int = 10, 
        agility: int = 10, 
        defense=10,

        # Item drop
        drop_exp=10,
        drop_item=None,
    ):
        self.name = name
        self.monster_type = monster_type
        self.level = level
        self.hp = hp
        self.energy = energy
        self.strength = strength
        self.agility = agility
        self.defense = defense
        self.drop_exp = drop_exp
        self.drop_item = drop_item

    def __repr__(self):
        return f"<Karakter {self.name} L{self.level} HP:{self.hp}/{self.max_hp}>"

    def take_damage(self, strength):
      sisa_damage = strength - self.defense

      if sisa_damage > 0:
          self.hp -= sisa_damage
          return True
      else:
          return False

    def attack(self, target):
        print(f"{self.name} menyerang {target.name} dengan damage {self.strength}")
        terluka = target.take_damage(self.strength)
        if terluka:
            print(f"{target.name} terluka dengan damage {self.strength}")
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

class AncientDragon(Enemy):
    def __init__(self):
        super().__init__(
            name="Ancient Dragon",
            monster_type="mythic",
            level=100,
            hp=1000,
            energy=1000,
            strength=1400,
            agility=800,
            defense=2000,
            drop_exp=5000,
            drop_item="Ancient dragon" # Sisik naga legendaris (5.500 gold)
        )

class Kraken(Enemy):
    def __init__(self):
        super().__init__(
            name="Kraken",
            monster_type="mythic",
            level=100,
            hp=1000,
            energy=1000,
            strength=1200,
            agility=1000,
            defense=1200,
            drop_exp=5000,
            drop_item=None,
        )

class Phoenix(Enemy):
    def __init__(self):
        super().__init__(
            name="Phoenix",
            monster_type="mythic",
            level=100,
            hp=1000,
            energy=1000,
            strength=1500,
            agility=1000,
            defense=1000,
            drop_exp=5000,
            drop_item=None,
        )

class Leviathan(Ememy):
    '''Penguasa lautan terdalam dengan sihir banjur bandang'''
    def __init__(self):
        super().__init__(
            name="Leviathan",
            monster_type="mythic",
            level=100,
            hp=1000,
            energy=1000,
            strength=1500,
            agility=1000,
            defense=1000,
            drop_exp=5000,
            drop_item=None,
        )

class Titan(Enemy):
    '''Raksasa seukuran gunung tang mampu memicu gempa bumi'''
    def __init__(self):
        super().__init__(
            name="Titan",
            monster_type="mythic",
            level=100,
            hp=1000,
            energy=1000,
            strength=5000,
            agility=5000,
            defense=5000,
            drop_exp=5000,
            drop_item=None,
        )
