class karakter:
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
        target.take_damage(self.damage)

    def use_energy(self, amount):
        if amount > self.energy:
            self.energy = 0
            return False
        else:
            self.energy -= amount
            return True

    def heal(self, amount):
        self.hp += amount
        if self.hp > 100:
            self.hp = 100
        return True
