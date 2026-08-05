class Enemy:
    '''Base class untuk semua monster'''
    def __init__(
        self, 
        # Indentitas & progresi
        name: str,
        monster_type: str,
        level: int = 0,
        # base values
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

        # base values and current values
        self.hp = hp
        self.max_hp = hp
        self.energy = energy
        self.max_energy = energy

        # stats
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

class Slime(Enemy):
    '''Gumpalan jeli penggangu dengan serangan ringan'''
    def __init__(self):
        super().__init__(
            name="Slime",
            monster_type="normal",
            level=1,
            hp=20,
            energy=20,
            strength=5,
            agility=5,
            defense=5,
            drop_exp=10,
            drop_item="sticky slime gel" # Cairan kenyal serbaguna untuk bahan ramuan (5 gold)
        )

class GoblinScout(Enemy):
    '''Makhluk hijau kecil bersenjata pisau belati'''
    def __init__(self):
        super().__init__(
            name="Goblin Scout",
            monster_type="normal",
            level=1,
            hp=30,
            energy=30,
            strength=10,
            agility=10,
            defense=10,
            drop_exp=20,
            drop_item="Tattered goblin pouch" # Kanton kulit kecil berisi koin-koin berkarat hasil curian goblin (12 gold)
        )

class GiantRat(Enemy):
    '''Tikus selokan seukuran anjing yang menyerang berpasangan'''
    def __init__(self):
        super().__init__(
            name="Giant Rat",
            monster_type="normal",
            level=1,
            hp=40,
            energy=40,
            strength=15,
            agility=15,
            defense=15,
            drop_exp=20,
            drop_item="Coarse rat pelt" # kulit berbulu kasar yang biasanya di beli pengrajun untuk latihan menyamak kulit (8 gold)
        )

class SkeletonWarrior(Enemy):
    '''Mayat hidup rapuh yang membawa pedang tua'''
    def __init__(self):
        super().__init__(
            name="Skeleton Warrior",
            monster_type="normal",
            level=1,
            hp=50,
            energy=50,
            strength=20,
            agility=15,
            defense=15,
            drop_exp=30,
            drop_item="Brittle bone fragment" # Tulang tua yang diselimuti energi kegelapan, dicari oleh ahli nujum amatir (15 gold)
        )

class Kobold(Enemy):
    '''Makhluk mirip anjing humanoid yang suka mencuri barang'''
    def __init__(self):
        super().__init__(
            name="Kobold",
            monster_type="normal",
            level=1,
            hp=60,
            energy=60,
            strength=25,
            agility=20,
            defense=20,
            drop_exp=40,
            drop_item="Kobold shiny pebble" # Batu tiruan yan gidkira emas oleh para kobold karena permukaannya yang mengkilap (20 gold)
        )

class GiantSpider(Enemy):
    '''Laba-laba hutan yang bisa memperlambat anda'''
    def __init__(self):
        super().__init__(
            name="Giant Spider",
            monster_type="normal",
            level=1,
            hp=70,
            energy=70,
            damage=30,
            agility=25,
            defense=25,
            drop_exp=50,
            drop_item="Sticky spider silk" # Benang sutra tebal yang sangat kuat (18 gold)
        )

class FeralWolf(Enemy):
    '''Serigala lapar yang mengincar pemain yang sendirian'''
    def __init__(self):
        super().__init__(
            name="Feral Wolf",
            monster_type="normal",
            level=1,
            hp=80,
            energy=80,
            strength=35,
            agility=25,
            defense=30,
            drop_exp=60,
            drop_item="Sharp wolf fang" # Taring tajam yang bisa dijadikan bahan dasar senjata (25 gold)
        )

class Imps(Enemy):
    '''Setan kecil yang hobi melemparkan bola api kecil'''
    def __init__(self):
        super().__init__(
            name="Imps",
            monster_type="normal",
            level=1,
            hp=90,
            energy=90,
            strength=40,
            agility=30,
            defense=35,
            drop_exp=70,
            drop_item=None
        )
