class Enemy:
    '''Base class untuk semua monster'''
    def __init__(
        self, 
        name,
        class_enemy, 
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
        self.class_enemy = class_enemy
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

class OrcBerseker(Enemy):
    '''Makhluk berbadan besar dengan kapak ganda'''
    def __init__(self):
        super().__init__(
            name="Orc Berseker",
            class_enemy="rare",
            level=1,
            hp=100,
            energy=80,
            damage=90, 
            agility=10, 
            defense=80,
            drop_exp=100,
            drop_item=None
        )

class Gargoyle(Enemy):
    '''Patung batu hidup yang menyergap dari langit-langit'''
    def __init__(self):
        super().__init__(
            name="Gargoyle",
            class_enemy="rare",
            level=1,
            hp=200,
            energy=100,
            damage=150,
            agility=50,
            defense=100,
            drop_exp=200,
            drop_item=None
        )

class Lizardman(Enemy):
    '''Manusia reptil bersenjata tombak dengan pertahanan tinggi'''
    def __init__(self):
        super().__init__(
            name="Lizardman",
            class_enemy="rare",
            level=1,
            hp=150,
            energy=120,
            damage=100,
            agiliti=80,
            defense=150,
            drop_exp=200,
            drop_item=None
        )
