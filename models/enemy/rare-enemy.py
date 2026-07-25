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
        drop_item=None
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
            agility=80,
            defense=150,
            drop_exp=200,
            drop_item=None
        )

class Harpy(Enemy):
    '''Mkhluk setengah wanita setengah burung yang menyerang dari udara'''
    def __init__(self):
        super().__init__(
            name="Harpy",
            class_enemy="rare",
            level=1,
            hp=250,
            energy=150,
            damage=200,
            agility=200,
            defense=150,
            drop_exp=200,
            drop_item=None
        )

class CentaurArcher(Enemy):
    '''Manusia setengah kuda yang mahir memanah'''
    def __init__(self):
        super().__init__(
            name="Centaur Archer",
            class_enemy="rare",
            level=1,
            hp=300,
            energy=200,
            damage=250,
            agility=250,
            defense=250,
            drop_exp=300,
            drop_item=None
        )

class ZombiePlaguebringer(Enemy):
    '''Mayat hidup yang menyebarkan racun di area sekitar'''
    def __init__(self):
        super().__init__(
            name="Zombie Plaguebringer",
            class_enemy="rare",
            level=1,
            hp=400,
            energy=300,
            damage=300,
            agility=250,
            defense=150,
            drop_exp=300,
            drop_item=None
        )

class Werewolf(Enemy):
    '''Manusia serigala lincah dengan serangan cakar beruntun'''
    def __init__(self):
        super().__init__(
            name="Werewolf",
            class_enemy="rare",
            level=1,
            hp=350,
            energy=250,
            damage=200,
            agility=300,
            defense=300,
            drop_exp=350,
            drop_item=None
        )

class Basilisk(Enemy):
    '''Kadal besar yang bisa memberikan efek kutukan atau kaku'''
    def __init__(self):
        super().__init__(
            name="Basilisk",
            class_enemy="rare",
            level=1,
            hp=450,
            energy=350,
            damage=350,
            agility=300,
            defense=400,
            drop_exp=400,
            drop_item=None
        )
