from math import e
# Import library yang dibutuhkan
import copy
import sqlite3
import time
import random

# ==============================================================================
# IMPORT REQUIRED FILES
# ==============================================================================

# Import constanta
from config import (
    DATABASE_NAME, MENU_OPTIONS, LOBBY_ROOM, SUMMONING_TYPE, TOWER_FLOOR,
    CARD_SUMMONING, SKILL,
)

# Import database
from database import init_database

# Import karakter
from karakter import Mage, Tank, Assassin, Support, Marksman, Fighter, Wizard, Necromancer

# Import monster
from normal_enemy import Slime

# Import Skills
from melee_magical import (
    ShockTounch,
)
from mid_range_magical import (
    HealingGrace, HolySantuary, FrostNova, RaiseUndead,
)
from long_range_magical import (
    ManaBurst, ShockWave, RepelWave, ArcaneRing, MagicShield, MagicArrow, SparkProjectile,
    Fireball, LightningStrike, MeteorStrike, GuardianLink, DivineIntervention, ChronoShift,
    GravityWell, BlackHole, Decay, SoulFeast, ArmyDarkness,
)
from melee_physical import (
    BasicJab, LowKick, HeavyFist, HeavySmash, BattleCry, CycloneSlash, BerserkCharge,
    ShieldBash, IronFortress, GroundTremor, BastionHope, SwepingLeg, PalmPush, ElbowCharge,
    AirSlap, StrikeSlash, QuickTrust, WideSwing, GuardBreak, CircularSlash, PoisonBlade,
    FlurryBlows, Assassinate,
)
from mid_range_physical import (
    ShadowStep, TumbleEscape,
)
from long_range_physical import (
    EnergyEdge, HallArrows, PiercingArrow, QuickShot,
)

# ==============================================================================
#
# ==============================================================================

CLASS_KARAKTER_CARD = {
    "Mage": Mage,
    "Tank": Tank,
    "Assassin": Assassin,
    "Support": Support,
    "Marksman": Marksman,
    "Fighter": Fighter,
    "Wizard": Wizard,
    "Necromancer": Necromancer
}

CLASS_SKILLS_CARD = {
    "Shock Tounch": ShockTounch,
    "Healing Grace": HealingGrace,
    "Holy Santuary": HolySantuary,
    "Frost Nova": FrostNova,
    "Raise Undead": RaiseUndead,
    "Mana Burst": ManaBurst,
    "Shock Wave": ShockWave,
    "Repel Wave": RepelWave,
    "Arcane Ring": ArcaneRing,
    "Magic Shield": MagicShield,
    "Magic Arrow": MagicArrow,
    "Spark Projectile": SparkProjectile,
    "Fireball": Fireball,
    "Lightning Strike": LightningStrike,
    "Meteor Strike": MeteorStrike,
    "Guardian Link": GuardianLink,
    "Divine Intervention": DivineIntervention,
    "Chrono Shift": ChronoShift,
    "Gravity Well": GravityWell,
    "Black Hole": BlackHole,
    "Decay": Decay,
    "Soul Feast": SoulFeast,
    "Army Darkness": ArmyDarkness,
    "Basic Jab": BasicJab,
    "Low Kick": LowKick,
    "Heavy Fist": HeavyFist,
    "Heavy Smash": HeavySmash,
    "Battle Cry": BattleCry,
    "Cyclone Slash": CycloneSlash,
    "Berserk Charge": BerserkCharge,
    "Shield Bash": ShieldBash,
    "Iron Fortress": IronFortress,
    "Ground Tremor": GroundTremor,
    "Bastion Hope": BastionHope,
    "Sweping Leg": SwepingLeg,
    "Palm Push": PalmPush,
    "Elbow Charge": ElbowCharge,
    "Air Slap": AirSlap,
    "Strike Slash": StrikeSlash,
    "Quick Trust": QuickTrust,
    "Wide Swing": WideSwing,
    "Guard Break": GuardBreak,
    "Circular Slash": CircularSlash,
    "Poison Blade": PoisonBlade,
    "Flurry Blows": FlurryBlows,
    "Assassinate": Assassinate,
    "Shadow Step": ShadowStep,
    "Tumble Escape": TumbleEscape,
    "Energy Edge": EnergyEdge,
    "Hall Arrows": HallArrows,
    "Piercing Arrow": PiercingArrow,
    "Quick Shot": QuickShot,
}

class InvalidMenuChoiceError(Exception):
    pass

def get_choice(x, y):
    while True:
        try:
            choice = int(input(f"\n{x}: "))

            if choice not in y:
                raise InvalidMenuChoiceError

            return choice

        except ValueError:
            print("Invalid input. Please enter a number.")

        except InvalidMenuChoiceError as e:
            print(f"Invalid input {e}")

def exit_bottom(x, y):
    input(f"\nPress {x} to {y}...")

def jeda_loading(second):
     '''jeda loading'''
     for i in range(5):
         print(".", end="")
         time.sleep(second)

# ==============================================================================
#
# ==============================================================================
def login():
    user_name = input("Masukkan username: ")

    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Cek apakah sudah terdaftar
    cursor.execute("SELECT id_player, user_name FROM username WHERE user_name = ?", (user_name,))
    data_player = cursor.fetchone()

    if data_player is not None:
        id_player = data_player[0]
        print(f"\n[LOADING] Welcome back {user_name} (ID: {id_player})")

        # Load inventori
        cursor.execute("SELECT item_name FROM inventory WHERE id_player = ?", (id_player,))
        items = [item[0] for item in cursor.fetchall()]

        # Load gold player
        cursor.execute("SELECT gold_player FROM pocket WHERE id_player = ?", (id_player,))
        gold_player = cursor.fetchone()[0]

        # Load karakter tersimpan
        cursor.execute("SELECT id_karakter FROM karakter WHERE id_player = ?", (id_player,))
        id_karakter = cursor.fetchall()

    else:
        cursor.execute("INSERT INTO username (user_name) VALUES (?)", (user_name,))
        id_player = cursor.lastrowid
        conn.commit()
        cursor.execute("INSERT INTO inventory (id_player) VALUES (?)", (id_player,))
        conn.commit()
        cursor.execute("INSERT INTO pocket (id_player) VALUES (?)", (id_player,))
        conn.commit()
        items = []
        gold_player = 0

        print(f"\n[LOADING] WELCOME... {user_name} (ID: {id_player})")
        time.sleep(1)

    conn.close()

    return id_player, user_name, items, gold_player

def menu():
    print("\n============== MENU UTAMA ==============\n")
    for i, (number, option) in enumerate(MENU_OPTIONS.items()):
        print(f"{i+1}. {option}")

def lobby():
    print("-" * 40)
    print("================= LOBBY ================")
    print("-" * 40, "\n")
    for i, (number, option) in enumerate(LOBBY_ROOM.items()):
        print(f"{i+1}. {option}")

def tower_floor():
    print("\n======== Go Beyond Your Limits =========")
    print("-" * 40)
    for i, (number, option) in enumerate(TOWER_FLOOR.items()):
        print(f"{i+1}. {option}")

def monster():
    print("\nDefeat the enemies in front of you!\n")
    tier_monster = random.randint(1, 3)
    level_monster = random.randint(1, 5)
    total_exp = random.randint(100, 200) * (tier_monster * level_monster)
    monster = copy.deepcopy(Slime(tier=tier_monster, level=level_monster, exp=total_exp))
    monster.level_up()
    print(f"{monster.__str__()}")

def barracks(id_player, x):
    print("\n=============== BARRACKS ===============")
    print("-" * 40)

    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        '''
        SELECT
            name, job, tier, level, exp, skill_01, skill_02, skill_03, skill_04,
            base_hp, base_energy, base_mana, strength, agility, defense, vitality,
            magic, dexterity, resistance, intelligence, strength_bonus, agility_bonus,
            defense_bonus, magic_bonus, dexterity_bonus, resistance_bonus
        FROM
            karakter
        WHERE
            id_player = ?
        ''',
            (id_player,)
    )

    all_character = cursor.fetchall()

    # Cek apakah sudah ada karakter
    if len(all_character) == 0:
        print("\nMaster! Anda belum memiliki hero!\n")
        return None, None
    else:
        for i, character in enumerate(all_character):
            print(f"{i+1}. Name: {character["name"]} | Job: {character["job"]}")

        choice = get_choice(x, range(1, len(all_character) + 1))
        selected_character = all_character[choice - 1]
        character = CLASS_KARAKTER_CARD[selected_character["job"]]()
        print(f"{character.__str__()}")

        card_skills = [
            character.skill_01.name,
            character.skill_02.name,
            character.skill_03.name,
            character.skill_04.name
        ]

        for i, skill in enumerate(card_skills):
            print(f"{i+1}. Skill{i+1}: {skill}")

    return card_skills, character

    conn.commit()
    conn.close()

def attack_logic(card_skills, character):
        while True:
            for i, skill in enumerate(card_skills):
                print(f"{i+1}. Skill{i+1}: {skill}")

            choice_attack = get_choice("Select a skill", SKILL)
            if choice_attack == 1:
                character.total_damage(CLASS_SKILLS_CARD[card_skills[0]]())
                break
            elif choice_attack == 2:
                character.total_damage(CLASS_SKILLS_CARD[card_skills[1]]())
                break
            elif choice_attack == 3:
                character.total_damage(CLASS_SKILLS_CARD[card_skills[2]]())
                break
            elif choice_attack == 4:
                character.total_damage(CLASS_SKILLS_CARD[card_skills[3]]())
                break

def activate_ability(id_player):
    # belum lengkap
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO skill (
            id_player, name, category, armed, range_type, debuff, level,
            competence, energy, mana, strength, agility, defense, vitality,
            magic, dexterity, resistance, intelligence
        )
        VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
            (id_player,)
    )

    conn.commit()
    conn.close()

    skill_available = SLOT_SKILL # ganti jadi ke database
    if len(skill_available) == 0:
        print("Do not yet possess those skills")
    else:
        for i, skill in enumerate(skill_available):
            print(f"{i+1}. {skill}")

def summoning_room():
    print("\n=========== SUMMONING ROOM ============\n")
    for i, (number, option) in enumerate(SUMMONING_TYPE.items()):
        print(f"{i+1}. {option}")

def card_summoning_hero():
    for i, (number, option) in enumerate(CARD_SUMMONING.items()):
        print(f"{i+1}. {option}")

def card_summoning_equipment():
    pass

def summoning_heroes(id_player):
    list_karakter = [Mage(), Tank(), Assassin(), Support(), Marksman(), Fighter(), Wizard(), Necromancer()]
    summoning_free = random.choice(list_karakter)
    print(f"Congratulations, Master! You have gained a hero:\n\n{summoning_free.__str__()}", sep="")

    # Masukkan ke database
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO karakter (
            id_player, name, job, tier, level, exp, skill_01, skill_02, skill_03,
            skill_04, base_hp, base_energy, base_mana, strength, agility,
            defense, vitality, magic, dexterity, resistance, intelligence,
            strength_bonus, agility_bonus, defense_bonus, magic_bonus,
            dexterity_bonus, resistance_bonus
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
            (
                (id_player),
                (summoning_free.name),
                (summoning_free.job),
                (summoning_free.tier),
                (summoning_free.level),
                (summoning_free.exp),
                (summoning_free.skill_01.name),
                (summoning_free.skill_02.name),
                (summoning_free.skill_03.name),
                (summoning_free.skill_04.name),
                (summoning_free.base_hp),
                (summoning_free.base_energy),
                (summoning_free.base_mana),
                (summoning_free.strength),
                (summoning_free.agility),
                (summoning_free.defense),
                (summoning_free.vitality),
                (summoning_free.magic),
                (summoning_free.dexterity),
                (summoning_free.resistance),
                (summoning_free.intelligence),
                (summoning_free.strength_bonus),
                (summoning_free.agility_bonus),
                (summoning_free.defense_bonus),
                (summoning_free.magic_bonus),
                (summoning_free.dexterity_bonus),
                (summoning_free.resistance_bonus)
           )
    )

    conn.commit()
    conn.close()

def main():
    init_database()
    id_player, user_name, items, gold_player = login()

    print("\n", "-" * 40, "\n   Welcome In Game The Advanture Hero   \n", "-" * 40, sep="")

    while True:
        menu()
        menu_choice = get_choice("menu", MENU_OPTIONS)

        # LOBBY
        if menu_choice == 1:

          while True:
                lobby()
                lobby_choice = get_choice("Lobby", LOBBY_ROOM)

                # Tower Floor
                if lobby_choice == 1:
                    card_skills, character = barracks(id_player, "Choose your hero, Master!")
                    while card_skills is None:
                        break
                    else:
                        jeda_loading(0.51)
                        tower_floor()
                        tower_floor_choice = get_choice("Select the desired Tower Floor", TOWER_FLOOR)
                        if tower_floor_choice == 1:
                            monster()
                            attack_logic(card_skills, character)
                        elif tower_floor_choice == 2:
                            pass

                # Barracks
                elif lobby_choice == 2:
                    barracks(id_player, "Select a character to view more information")
                    exit_bottom("enter", "continue")
                    break

                # Summoning Room
                elif lobby_choice == 3:
                    while True:
                        summoning_room()
                        summoning_choice = get_choice("Choose the summon you want, Master!", SUMMONING_TYPE)

                        if summoning_choice == 1:
                            while True:
                                card_summoning_hero()
                                card_summoning_hero_choice = get_choice("Select a summoning card, Master!", CARD_SUMMONING)
                                if card_summoning_hero_choice == 1:
                                    summoning_heroes(id_player)
                                    exit_bottom("enter", "continue")
                                elif card_summoning_hero_choice == 2:
                                    exit_bottom("enter", "continue")
                                elif card_summoning_hero_choice == 3:
                                    break

                        elif summoning_choice == 2:
                            while True:
                                card_summoning_equipment()
                                card_summoning_equipment_choice = get_choice("Select a summoning card, Master!", CARD_SUMMONING)
                                if card_summoning_equipment_choice == 1:
                                    exit_bottom("enter", "continue")
                                elif card_summoning_equipment_choice == 2:
                                    exit_bottom("enter", "continue")
                                elif card_summoning_equipment_choice == 3:
                                    break

                        elif summoning_choice == 3:
                            break

                # Back
                elif lobby_choice == 4:
                    break

        # SHOP
        elif menu_choice == 2:
            pass

        # EXIT
        elif menu_choice == 3:
            print("\nThank you for playing!")
            break

# ==============================================================================
# MAIN PROGRAM
# ==============================================================================
if __name__ == "__main__":
    main()
