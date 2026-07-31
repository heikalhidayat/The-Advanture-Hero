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

class OrcBerseker(Enemy):
    '''Makhluk berbadan besar dengan kapak ganda'''
    def __init__(self):
        super().__init__(
            name="Orc Berseker",
            monster_type="rare",
            level=1,
            hp=100,
            energy=80,
            strength=90, 
            agility=10, 
            defense=80,
            drop_exp=100,
            drop_item="Broken orc cleaver" # Potongan besi berat dari senjata orc yang bisa dilebur kembali oleh pandai besi (90 gold)
        )

class Gargoyle(Enemy):
    '''Patung batu hidup yang menyergap dari langit-langit'''
    def __init__(self):
        super().__init__(
            name="Gargoyle",
            monster_type="rare",
            level=1,
            hp=200,
            energy=100,
            strength=150,
            agility=50,
            defense=100,
            drop_exp=200,
            drop_item="Gargoyle heartstone" # Batu berbentuk jantung yang menyimpan energi magis penyokong hidup sang patung (110 gold)
        )

class Lizardman(Enemy):
    '''Manusia reptil bersenjata tombak dengan pertahanan tinggi'''
    def __init__(self):
        super().__init__(
            name="Lizardman",
            monster_type="rare",
            level=1,
            hp=150,
            energy=120,
            strength=100,
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
            monster_type="rare",
            level=1,
            hp=250,
            energy=150,
            strength=200,
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
            monster_type="rare",
            level=1,
            hp=300,
            energy=200,
            strength=250,
            agility=250,
            defense=250,
            drop_exp=300,
            drop_item="Centaur tail hair" # Rambut ekor yang sangat elastis, sangat bagus untuk dijadikan tali busur panah berkualitas (130 gold)
        )

class ZombiePlaguebringer(Enemy):
    '''Mayat hidup yang menyebarkan racun di area sekitar'''
    def __init__(self):
        super().__init__(
            name="Zombie Plaguebringer",
            monster_type="rare",
            level=1,
            hp=400,
            energy=300,
            strength=300,
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
            monster_type="rare",
            level=1,
            hp=350,
            energy=250,
            strength=200,
            agility=300,
            defense=300,
            drop_exp=350,
            drop_item="Tuft of cursed fur" # Bulu tebal manusia serigala yang tetap hangat meski berada di cuaca ekstrim (150 gold)
        )

class Basilisk(Enemy):
    '''Kadal besar yang bisa memberikan efek kutukan atau kaku'''
    def __init__(self):
        super().__init__(
            name="Basilisk",
            monster_type="rare",
            level=1,
            hp=450,
            energy=350,
            strength=350,
            agility=300,
            defense=400,
            drop_exp=400,
            drop_item="Basilisk petrifying eye" # Bola mata reptil yang telah mati namun tatapannya masih menyisakan aura (220 gold)
        )
