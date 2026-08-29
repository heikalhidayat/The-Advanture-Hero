from models.karakter.base_karakter import Karakter

class Enemy(Karakter):
    def __init__(
        self,
        name,
        job: str,
        tier: int,
        level: int,
        exp: int,
        skill_01: str,
        skill_02: int,
        skill_03: int,
        skill_04: int,
        # base values
        base_hp: int,
        base_energy: int,
        base_mana: int,
        # core stats
        strength: int,
        agility: int,
        defense: int,
        vitality: int,
        magic: int,
        dexterity: int,
        resistance: int,
        intelligence: int,
        # equipment bonus
        strength_bonus: int,
        agility_bonus: int,
        defense_bonus: int,
        magic_bonus: int,
        dexterity_bonus: int,
        resistance_bonus: int,
        # drop
        drop_item: str,
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04,
            base_hp, base_energy, base_mana, strength, agility, defense, vitality, 
            magic, dexterity, resistance, intelligence, strength_bonus, 
            agility_bonus, defense_bonus, magic_bonus, dexterity_bonus, 
            resistance_bonus
        )
        self.drop_item = drop_item

    @property
    def total_drop_exp(self) -> int:
        return self.exp * (self.tier * self.level)
