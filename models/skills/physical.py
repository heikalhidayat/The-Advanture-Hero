class Skills:
    def __init__(self, name, category, armed, range_type, debuff, energy, damage, agility, defense):
        self.name = name
        self.category = category
        self.armed = armed
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
    '''Pukulan lurus cepat untuk mencicil damage musuh'''
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
    '''Tendangan ke arah kaki untuk mengganggu keseimbangan lawan'''
    def __init__(self):
        super().__init__(
            name="Low Kick",
            category="physical",
            armed=False,
            range_type="melee",
            debuff="stun",
            energy=10,
            damage=20,
            agility=5,
            defense=0
        )

class HeavyFist(Skills):
    '''Pukulan berat penghancur pertahanan'''
    def __init__(self):
        super().__init__(
            name="Heavy Fist",
            category="physical",
            armed=False,
            range_type="melee",
            debuff=None,
            energy=15,
            damage=20,
            agility=0,
            defense=0
        )

class HeavyPunch(Skills):
    '''Pukulan berat untuk menghancurkan musuh'''
    def __init__(self):
        super().__init__(
            name="Heavy Punch",
            category="physical",
            armed=False,
            range_type="melee",
            debuff=None,
            energy=25,
            damage=30,
            agility=0,
            defense=0
        )

class SwepingLeg(Skills):
    '''Tendangan memutar menyapu area depan'''
    def __init__(self):
        super().__init__(
            name="Sweping Leg",
            category="physical",
            armed=False,
            range_type="mid_range",
            debuff=None,
            energy=20,
            damage=30,
            agility=0,
            defense=0
        )

class PalmPush(Skills):
    '''Dorongan telapak tangan bertekanan udara'''
    def __init__(self):
        super().__init__(
            name="Palm Push",
            category="physical",
            armed=False,
            range_type="mid_range",
            debuff=None,
            energy=20,
            damage=30,
            agility=10,
            defense=0
        )

class ElbowCharge(Skills):
    '''Terjangan siku ke depan sambil menahan serangan'''
    def __init__(self):
        super().__init__(
            name="Elbow Charge",
            category="physical",
            armed=False,
            range_type="mid_range",
            debuff=None,
            energy=15,
            damage=15,
            agility=0
        )

class AirSlap(Skills):
    '''Tebasan angin tipis dari kecepatan tangan'''
    def __init__(self):
        super().__init__(
            name="Air Slap",
            category="physical",
            armed=False,
            range_type="long_range",
            debuff=None,
            energy=15,
            damage=15,
            agility=0
        )

class StraightSlash(Skills):
    '''Ayunan senjata standar ke depan'''
    def __init__(self):
        super().__init__(
            name="Straight Slash",
            category="physical",
            armed=True,
            range_type="melee",
            debuff=None,
            energy=15,
            damage=15,
            agility=0
        )

class QuickTrust(Skills):
    '''Tusukan instan yang sangat cepat'''
    def __init__(self):
        super().__init__(
            name="Quick Trust",
            category="physical",
            armed=True,
            range_type="melee",
            debuff=None,
            energy=15,
            damage=15,
            agility=20
        )

class PommelStrike(Skills):
    '''Hantaman gagang senjata untuk mengejutkan musuh'''
    def __init__(self):
        super().__init__(
            name="Pommel Strike",
            category="physical",
            armed=True,
            range_type="melee",
            debuff=None,
            energy=20,
            damage=20,
            agility=0
        )

class WideSwing(Skills):
    '''Tebasan melebar area depan'''
    def __init__(self):
        super().__init__(
            name="Wide Swing",
            category="physical",
            armed=True,
            range_type="mid_range",
            debuff=None,
            energy=15,
            damage=15,
            agility=12
        )

class GuardBreak(Skills):
    '''Serangan vertikal berat dari atas ke bawah'''
    def __init__(self):
        super().__init__(
            name="Guard Break",
            category="physical",
            armed=True,
            range_type="mid_range",
            debuff=None,
            energy=20,
            damage=25,
            agility=0
        )

class CircularSlash(Skills):
    '''Menebas melingkar 360 derajat di sekeliling musuh'''
    def __init__(self):
        super().__init__(
            name="Circular Slash",
            category="physical",
            armed=True,
            range_type="mid_range",
            debuff=None,
            energy=25,
            damage=18,
            agility=18
        )

class EnergyEdge(Skills):
    '''Ayunan senjata yang melepaskan gelombang energi'''
    def __init__(self):
        super().__init__(
            name="Energy Edge",
            category="physical",
            armed=True,
            range_type="long_range",
            debuff=None,
            energy=25,
            damage=25,
            agility=0
        )
