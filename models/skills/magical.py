class Skills:
    def __init__(self, name, category, target_area, range_type, debuff, mana, damage):
        self.name = name
        self.category = "magical_attack"
        self.target_area = target_area
        self.range_type = range_type
        self.debuff = debuff
        self.mana = mana
        self.damage = damage
        
    def execute(self, user, target):
        if user.mana >= self.mana:
            user.mana -= self.mana
            print(f"{user.name} menggunakan {self.name}!")
            target.take_damage(self.damage)
        else:
            print(f"Mana {user.name} tidak cukup untuk {self.name}!")

class ManaBurst(Skills):
    '''Ledakan energi instan di telapak tangan'''
    def __init__(self, category):
        super().__init__(
              name="Mana Burst",
              target_area="single_target",
              range_type="melee",
              debuff="knockback",
              mana=15,
              damage=35
        )

class ShockTounch(Skills):
    '''sentuhan listrik bertegangan tinggi'''
    def __init__(self, category):
        super().__init__(
              name="Shock Tounch",
              target_area="Single Target",
              range_type="melee",
              debuff="stun",
              mana=20,
              damage=25
        )

class RepelWave(Skills):
    '''gelombang dorongan sihir berbentuk kipas'''
    def __init__(self, category):
        super().__init__(
              name="Repel Wave",
              target_area="Area of Effect",
              range_type="mid_range",
              debuff="slow",
              mana=25,
              damage=40
        )

class ArcaneRing(Skills):
    '''Lingkaran energy yang meledak di sekeliling tubuh'''
    def __init__(self, category):
        super().__init__(
              name="Arcane Ring",
              target_area="Area of Effect",
              range_type="mid_range",
              debuff=None,
              mana=30,
              damage=50
        )

class MagicArrow(Skills):
    '''Proyektil sihir standar berbentuk panah cahaya'''
    def __init__(self, category):
        super().__init__(
              name="Magic Arrow",
              target_area="Single Target",
              range_type="long_range",
              debuff=None,
              mana=10,
              damage=30
        )

class SparkProjectile(Skills):
    '''Bola listrik kecil yang dilempar dari jauh'''
    def __init__(self, category):
        super().__init__(
              name="Spark Projectile",
              target_area="Single Target",
              range_type="long_range",
              debuff="paralyze",
              mana=15,
              damage=25
        )
