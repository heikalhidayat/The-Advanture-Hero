from base_karakter import Karakter

class Enemy(Karakter):
    def __init__(
        self,
        name,
        job = None,
        tier = 1,
        level = 1,
        exp = 0,
        base_hp = 0,
        base_energy = 0,
        base_mana = 0,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 0,
        magic = 0,
        dexterity = 0,
        resistance = 0,
        intelligence = 0,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(
            name, job, tier, level, exp, base_hp, base_energy,
            base_mana, strength, agility, defense, vitality, magic,
            dexterity, resistance, intelligence, strength_bonus, 
            agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, 
            resistance_bonus
        )
        self.drop_item = None

    @property
    def total_drop_exp(self) -> int:
        return self.exp * (self.tier * self.level)
