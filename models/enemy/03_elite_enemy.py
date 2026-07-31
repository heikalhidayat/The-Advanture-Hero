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

class Minotaur(Enemy):
    '''Monster berkepala banteng yang menjaga labirin dan koridor sempit'''
    def __init__(self):
        super().__init__(
            name="Minotaur",
            monster_type="elite",
            level=1,
            hp=400,
            energy=350,
            strength=600,
            agility=345,
            defense=450,
            drop_exp=500,
            drop_item="Polished minotaur horn" # Tanduk raksasa kokoh yang melambangkan kekuatatan. sangat bernilai untuk pembuatan item (500 gold)
        )

class Golem(Enemy):
    '''Raksasa batu atau besi dengan pertahanan fisik absolut'''
    def __init__(self):
        super().__init__(
            name="Golem",
            monster_type="elite",
            level=1,
            hp=400,
            energy=350,
            strength=600,
            agility=345,
            defense=450,
            drop_exp=500,
            drop_item="Pure iron ore core" # Bagian terdalam golem yang merupakan bongkahan besi tanpa cacat (650 gold)
        )

class Wyvern(Enemy):
    '''Kerabat naga yang lebih kecil namun sangat agresif di udara'''
    def __init__(self):
        super().__init__(
            name="Wyvern",
            monster_type="elite",
            level=1,
            hp=400,
            energy=350,
            strength=600,
            agility=345,
            defense=450,
            drop_exp=500,
            drop_item=None
        )

class Necromancer(Enemy):
    '''Penyihir hitam yang terus menerus membangkitkan monster mati'''
    def __init__(self):
        super().__init__(
            name="Necromancer",
            monster_type="elite",
            level=1,
            hp=400,
            energy=350,
            strength=600,
            agility=345,
            defense=450,
            drop_exp=500,
            drop_item="Forbidden spellbook page" # Lembaran kertas kuno berisi catatan mantra pembangkit mayat (750 gold)
        )

class Cyclops(Enemy):
    '''Raksasa bermata satu yang mampu melempar batu besar'''
    def __init__(self):
        super().__init__(
            name="Cyclops",
            monster_type="elite",
            level=1,
            hp=400,
            energy=350,
            strength=600,
            agility=345,
            defense=450,
            drop_exp=500,
            drop_item="Cyclops giant tear" # Cairan kristal langka yang keluar saat cyclop mati (800 gold)
        )

class Succubus(Enemy):
    '''Monster penggoda yang mencuri nyawa (HP) menggunkan sihir'''
    def __init__(self):
        super().__init__(
            name="Succubus",
            monster_type="elite",
            level=1,
            hp=400,
            energy=350,
            strength=600,
            agility=345,
            defense=450,
            drop_exp=500,
            drop_item=None
        )

class Chimera(Enemy):
    '''Makhluk hibrida berkepala singa, kambing, dan berekor ular'''
    def __init__(self):
        super().__init__(
            name="Chimera",
            monster_type="elite",
            level=1,
            hp=400,
            energy=350,
            strength=600,
            agility=345,
            defense=450,
            drop_exp=500,
            drop_item="Chimera triple-blood" # campuran darah singa, kambing, dan ular yang menghasilkan energi alkia murni (950 gold)
        )

class Lich(Enemy):
    '''Penyihir mayat hidup yang menguasai sihir es tingkat tinggi'''
    def __init__(self):
        super().__init__(
            name="Lich",
            monster_type="elite",
            level=1,
            hp=400,
            energy=350,
            strength=600,
            agility=345,
            defense=450,
            drop_exp=500,
            drop_item="Frozen lich phylactery" # Wadah jiwa kristal es abadi tempat lich menyimpan keabadiannya (1.200 gold)
        )
