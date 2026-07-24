class Skills:
    def __init__(self, name, category, range_type, energy, damage, agility, defense):
        self.name = name
        self.category = category
        self.range_type = range_type
        self.energy = energy
        self.damage = damage
        self.agility = agility
        self.defense = defense
        
    def execute(self, user, target):
        if user.energy >= self.energy:
            user.energy -= self.energy
            print(f"{user.name} menggunakan {self.name}!")
            target.take_damage(self.damage)
        else:
            print(f"Energy {user.name} tidak cukup untuk {self.name}!")

class BasicJab(Skills):
    def __init__(self):
        super().__init__(
            name="Basic Jab",
            category="physical",
            range_type="melee",
            energy=5,
            damage=10,
            agility=10,
            defense=0
        )
