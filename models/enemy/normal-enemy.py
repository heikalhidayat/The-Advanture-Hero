class Enemy:
    '''Base class untuk semua monster'''
    def __init__(
        self, 
        name, 
        level=0, 
        hp=100, 
        energy=100, 
        damage=10, 
        agility=10, 
        defense=10,
        drop_exp=10,
        drop_item=None,
    ):
        self.name = name
        self.level = level
        self.hp = hp
        self.energy = energy
        self.damage = damage
        self.agility = agility
        self.defense = defense
        self.drop_exp = drop_exp
        self.drop_item = drop_item

    def __repr__(self):
        return f"<Karakter {self.name} L{self.level} HP:{self.hp}/{self.max_hp}>"

    def take_damage(self, damage):
      sisa_damage = damage - self.defense

      if sisa_damage > 0:
          self.hp -= sisa_damage
          return True
      else:
          return False

    def attack(self, target):
        print(f"{self.name} menyerang {target.name} dengan damage {self.damage}")
        terluka = target.take_damage(self.damage)
        if terluka:
            print(f"{target.name} terluka dengan damage {self.damage}")
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
            level=1,
            hp=20,
            energy=20,
            damage=5,
            agility=5,
            defense=5,
            drop_exp=10,
            drop_item=None
        )

class GoblinScout(Enemy):
    '''Makhluk hijau kecil bersenjata pisau belati'''
    def __init__(self):
        super().__init__(
            name="Goblin Scout",
            level=1,
            hp=30,
            energy=30,
            damage=10,
            agility=10,
            defense=10,
            drop_exp=20,
            drop_item=None
        )

class GiantRat(Enemy):
    '''Tikus selokan seukuran anjing yang menyerang berpasangan'''
    def __init__(self):
        super().__init__(
            name="Giant Rat",
            level=1,
            hp=40,
            energy=40,
            damage=15,
            agility=15,
            defense=15,
            drop_exp=20
            drop_item=None
        )

class SkeletonWarrior(Enemy):
    '''Mayat hidup rapuh yang membawa pedang tua'''
    def __init__(self):
        super().__init__(
            name="Skeleton Warrior",
            level=1,
            hp=50,
            energy=50,
            damage=20,
            agility=15,
            defense=15,
            drop_exp=30,
            drop_item=None
        )

class Kobold(Enemy):
    '''Makhluk mirip anjing humanoid yang suka mencuri barang'''
    def __init__(self):
        super().__init__(
            name="Kobold",
            level=1,
            hp=60,
            energy=60,
            damage=25,
            agility=20,
            defense=20,
            drop_exp=40
            drop_item=None
        )

class GiantSpider(Enemy):
    '''Laba-laba hutan yang bisa memperlambat anda'''
    def __init__(self):
        super().__init__(
            name="Giant Spider",
            level=1,
            hp=70,
            energy=70,
            damage=30,
            agility=25,
            defense=25,
            drop_exp=50,
            drop_item=None
        )

class FeralWolf(Enemy):
    '''Serigala lapar yang mengincar pemain yang sendirian'''
    def __init__(self):
        super().__init__(
            name="Feral Wolf",
            level=1,
            hp=80,
            energy=80,
            damage=35,
            agility=25,
            defense=30,
            drop_exp=60,
            drop_item=None
        )

class Imps(Enemy):
    '''Setan kecil yang hobi melemparkan bola api kecil'''
    def __init__(self):
        super().__init__(
            name="Imps",
            level=1,
            hp=90,
            energy=90,
            damage=40,
            agility=30,
            defense=35,
            drop_exp=70,
        )

