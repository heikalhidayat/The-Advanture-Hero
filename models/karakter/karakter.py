from config import BASE_HP, BASE_ENERGY, BASE_MANA
from base_karakter import Karakter

from melee_physical import (
    HeavySmash, BattleCry, CycloneSlash, BerserkCharge, BasicJab,
    ShieldBash, IronFortress, GroundTremor, BastionHope,
    PoisonBlade, FlurryBlows, Assassinate
)

from mid_range_physical import (
    ShadowStep, TumbleEscape,
)

from long_range_physical import (
    QuickShot, PiercingArrow, HallArrows,
)

from mid_range_magical import (
    HealingGrace, HolySantuary, RaiseUndead, FrostNova,
)
from long_range_magical import (
    Fireball, MagicShield, LightningStrike, MeteorStrike, DivineIntervention,
    ArmyDarkness, SoulFeast, Decay, BlackHole, GravityWell, ChronoShift,
    GuardianLink
)

class Fighter(Karakter):
    def __init__(
        self,
        name = "Ragnar",
        job = "Fighter",
        tier = 1,
        level = 1, 
        exp = 0,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 10,
        agility = 6,
        defense = 8, 
        vitality = 20,
        magic = 0,
        dexterity = 2,
        resistance = 4,
        intelligence = 10,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04, 
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, intelligence, strength_bonus,
            agility_bonus, defense_bonus
        )

        self.skill_01 = HeavySmash()
        self.skill_02 = BattleCry()
        self.skill_03 = CycloneSlash()
        self.skill_04 = BerserkCharge()

class Tank(Karakter):
    def __init__(
        self,
        name = "Aegis",
        job = "Tanker",
        tier = 1,
        level = 1, 
        exp = 0, 
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA, 
        strength = 10,
        agility = 5,
        defense = 13, 
        vitality = 25,
        magic = 0,
        dexterity = 0,
        resistance = 2,
        intelligence = 5,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04, 
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, intelligence, strength_bonus,
            agility_bonus, defense_bonus
        )

        self.skill_01 = ShieldBash()
        self.skill_02 = IronFortress()
        self.skill_03 = GroundTremor()
        self.skill_04 = BastionHope()

class Mage(Karakter):
    def __init__(
        self,
        name = "Ignis",
        job = "Mage",
        tier = 1,
        level = 1, 
        exp = 0,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 2,
        agility = 2,
        defense = 1, 
        vitality = 5,
        magic = 15,
        dexterity = 6,
        resistance = 4,
        intelligence = 25,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04, 
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, intelligence, strength_bonus,
            agility_bonus, defense_bonus
        )

        self.skill_01 = Fireball()
        self.skill_02 = MagicShield()
        self.skill_03 = LightningStrike()
        self.skill_04 = MeteorStrike()

class Assassin(Karakter):
    def __init__(
        self,
        name = "Grim",
        job = "Assassin",
        tier = 1,
        level = 1, 
        exp = 0,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 8,
        agility = 15,
        defense = 1,
        vitality = 18,
        magic = 0,
        dexterity = 6,
        resistance = 0,
        intelligence = 12,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04, 
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, intelligence, strength_bonus,
            agility_bonus, defense_bonus
        )

        self.skill_01 = ShadowStep()
        self.skill_02 = PoisonBlade()
        self.skill_03 = FlurryBlows()
        self.skill_04 = Assassinate()

class Marksman(Karakter):
    def __init__(
        self,
        name = "Hawkeye",
        job = "Marksman",
        tier = 1,
        level = 1, 
        exp = 0,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 6,
        agility = 6,
        defense = 1, 
        vitality = 12,
        magic = 0,
        dexterity = 15,
        resistance = 2,
        intelligence = 18,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04, 
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, intelligence, strength_bonus,
            agility_bonus, defense_bonus
        )

        self.skill_01 = QuickShot()
        self.skill_02 = PiercingArrow()
        self.skill_03 = TumbleEscape()
        self.skill_04 = HallArrows()

class Support(Karakter):
    def __init__(
        self,
        name = "Lyra",
        job = "Support",
        tier = 1,
        level = 1, 
        exp = 0,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 2,
        agility = 2,
        defense = 4, 
        vitality = 8,
        magic = 10,
        dexterity = 2,
        resistance = 10,
        intelligence = 22,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04, 
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, intelligence, strength_bonus,
            agility_bonus, defense_bonus
        )

        self.skill_01 = HealingGrace()
        self.skill_02 = Holysanctuary()
        self.skill_03 = GuardianLink()
        self.skill_04 = DivineIntervention()

class Wizard(Karakter):
    def __init__(
        self,
        name = "Zphyr",
        job = "Wizard",
        tier = 1,
        level = 1, 
        exp = 0,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 0,
        agility = 2,
        defense = 0, 
        vitality = 5,
        magic = 18,
        dexterity = 6,
        resistance = 4,
        intelligence = 25,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04, 
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, intelligence, strength_bonus,
            agility_bonus, defense_bonus
        )

        self.skill_01 = FrostNova()
        self.skill_02 = ChronoShift()
        self.skill_03 = GravityWell()
        self.skill_04 = BlackHole()

class Necromancer(Karakter):
    def __init__(
        self,
        name = "Mortis",
        job = "Necromancer",
        tier = 1,
        level = 1, 
        exp = 0,
        skill_01 = None,
        skill_02 = None,
        skill_03 = None,
        skill_04 = None,
        base_hp = BASE_HP,
        base_energy = BASE_ENERGY,
        base_mana = BASE_MANA,
        strength = 0,
        agility = 0,
        defense = 0,
        vitality = 5,
        magic = 20,
        dexterity = 2,
        resistance = 8,
        intelligence = 25,
        strength_bonus = 0,
        agility_bonus = 0,
        defense_bonus = 0,
        magic_bonus = 0,
        dexterity_bonus = 0,
        resistance_bonus = 0
    ):
        super().__init__(
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04, 
            base_hp, base_energy, base_mana, strength, agility, defense, 
            vitality, magic, dexterity, resistance, intelligence, strength_bonus,
            agility_bonus, defense_bonus
        )

        self.skill_01 = RaiseUndead()
        self.skill_02 = Decay()
        self.skill_03 = SoulFeast()
        self.skill_04 = ArmyDarkness()

# EXAMPLE
karu = Fighter()
jab = BasicJab()

print(jab.dict_skill)
print(karu.skill_01)
print(karu.strength)
print(karu.change_skill(jab))
