class Enemy:
    def __init__(self, name, level=0, hp=100, energy=100, damage=10, agility=10, defense=10):
        self.name = name
        self.level = level
        self.hp = hp
        self.energy = energy
        self.damage = damage
        self.agility = agility
        self.defense = defense

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
