class Skills:
    def __init__(self, name, category, range_type, debuff, energy, damage, agility, defense):
        self.name = name
        self.category = category
        self.range_type = range_type
        self.debuff = debuff
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
    """Pukulan lurus cepat untuk mencicil damage musuh"""
    def __init__(self):
        super().__init__(
            name="Basic Jab",
            category="physical",
            range_type="melee",
            debuff=None,
            energy=5,
            damage=10,
            agility=10,
            defense=0
        )

class LowKick(Skills):
    """Tendangan ke arah kaki untuk mengganggu keseimbangan lawan"""
    def __init__(self, debuff):
        super().__init__(
            name="Low Kick",
            category="physical",
            range_type="melee",
            debuff="stun",
            energy=10,
            damage=20,
            agility=5,
            defense=0
        )

class HeavyFist(Skills):
    def __init__(self):
        super().__init__(
            name="Heavy Fist",
            category="physical",
            range_type="melee",
            energy=15,
            damage=20,
            agility=0,
            defense=0
        )

class HeavyPunch(Skills):
    def __init__(self):
        super().__init__(
            name="Heavy Punch",
            category="physical",
            range_type="melee",
            energy=25,
            damage=30,
            agility=0,
            defense=0
        )

class SwepingLeg(Skills):
    def __init__(self):
        super().__init__(
            name="Sweping Leg",
            category="physical",
            range_type="mid_range",
            energy=20,
            damage=30,
            agility=0,
            defense=0
        )

class PalmPush(Skills):
    def __init__(self):
        super().__init__(
            name="Palm Push",
            category="physical",
            range_type="mid_range",
            energy=20,
            damage=30,
            agility=10,
            defense=0
        )

class ElbowCharge(Skills):
    def __init__(self):
        super().__init__(
            name="Elbow Charge",
            category="physical",
            range_type="mid_range",
            energy=15,
            damage=15,
            agility=0
        )
