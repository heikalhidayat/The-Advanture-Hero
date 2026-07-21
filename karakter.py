class Karakter:
    def __init__(self, name, max_exp, level=0, exp=0, hp=100, energy=100, damage=10, agility=10, defense=10):
        self.name = name
        self.exp = exp
        self.level = level
        self.max_exp = 100
        self.hp = hp
        self.energy = energy
        self.damage = damage
        self.agility = agility
        self.defense = defense

    def exp_up(self, amount):
        self.exp += amount
        print(f"{self.name} mendapatkan {amount} EXP! ({self.exp}/{self.max_exp})")
        while self.exp >= self.max_exp:
            self.exp -= self.max_exp
            self.level_up()

    def level_up(self):
        self.level += 1
        self.hp += 10
        self.energy += 10
        self.damage += 5
        self.agility += 5
        self.defense += 5

        self.max_exp *= 2
        print(f"LEVEL UP! {self.name} naik ke Level {self.level}")
        print(f"Batas EXP baru untuk Level berikutnya: {self.max_exp}")

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

    def use_energy(self, amount):
        if amount > self.energy:
            print(f"{self.name} tidak memiliki energy yang cukup!")
            self.energy = 0
            return False
        else:
            self.energy -= amount
            return True

    def heal(self, amount):
        self.hp += amount
        if self.hp > 100:
            print(f"{self.name} memulihkan HP sebesar {amount}. HP sekarang: {self.hp}")
            self.hp = 100
        return True

class Mage(Karakter):
    def __init__(self, name, max_exp, mana=50, level=0, exp=0, hp=100, energy=100, damage=20, agility=5, defense=5):
        super().__init__(name, max_exp, level, exp, hp, energy, damage, agility, defense)
        self.mana = mana

    def level_up(self):
        super().level_up()
        self.mana += 10
        print(f"Mana {self.name} bertambah! Mana sekarang: {self.mana}")

    def cast_spell(self, amount):
        if self.mana >= amount:
            self.mana -= amount
            return f"{self.name} melakukan sihir! mana berkurang {amount}"
        else:
            return f"{self.name} tidak memiliki mana yang cukup!"
            
class Warrior(Karakter):
	  def __init__(self, name, max_exp, aura=50, level=0, exp=0, hp=100, energy=100, damage=15, agility=15, defense=15):
	      super().__init__(name, max_exp, level, exp, hp, energy, damage, agility, defense)
	      self.aura = aura
