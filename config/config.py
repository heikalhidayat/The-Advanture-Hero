# ============================================
# 1. PENGATURAN DATABASE & SISTEM
# ============================================
DATABASE_NAME = "game.db"
GAME_TITLE = "The Adventure Hero"
GAME_VERSION = "0.0.1"

# ============================================
# 2. BALANCING BASE STATS PLAYER
# ============================================
BASE_HP = 100
BASE_ENERGY = 100
BASE_MANA = 100
# PHYSICAL
BASE_STRENGTH = 10
BASE_AGILITY = 10
BASE_DEFENSE = 10
# MAGICAL
BASE_MAGIC = 10
BASE_DEXTERITY = 10
BASE_RESISTANCE = 10
# BASE ATRIBUT
BASE_VITALITY = 10
BASE_INTELLIGENCE = 10
# BASE CAPASITY SKILL
BASE_CAPASITY_SKILL = 4

# ============================================
# 3. BALANCING EXP & LEVEL UP
# ============================================
BASE_HP_MULTIPLIER = 15
BASE_ENERGY_MULTIPLIER = 15
BASE_MANA_MULTIPLIER = 15
BASE_STRENGTH_MULTIPLIER = 15
BASE_AGILITY_MULTIPLIER = 15
BASE_DEFENSE_MULTIPLIER = 15
BASE_MAGIC_MULTIPLIER = 15
BASE_DEXTERITY_MULTIPLIER = 15
BASE_RESISTANCE_MULTIPLIER = 15

# ============================================
# 4. LEVEL UP
# ============================================
STAT_INCREASE_HP = 10           # Penambahan HP saat level up
STAT_INCREASE_ENERGY = 10       # Penambahan energy saat level up
STAT_INCREASE_MANA = 10         # Penambahan mana saat level up
STAT_INCREASE_STRENGTH = 10     # Penambahan Strength saat level up
STAT_INCREASE_AGILITY = 10      # Penambahan Agility saat level up
STAT_INCREASE_DEFENSE = 10      # Penambahan Defense saat level up
STAT_INCREASE_MAGIC = 10        # Penambahan Magic saat level up
STAT_INCREASE_DEXTERITY = 10    # Penambahan Dexterity saat level up
STAT_INCREASE_RESISTANCE = 10   # Penambahan Resistance saat level up

STAT_INCREASE_VITALITY = 10     # Penambahan Vitality saat level up
STAT_INCREASE_INTELLIGENCE = 10 # Penambahan Intelligence saat level up

# ============================================
# 5. TIER POINT
# ============================================
TIER_F = 1
TIER_D = 2
TIER_C = 3
TIER_B = 4
TIER_A = 5
TIER_S = 6

# ============================================
# 6. BASE ATRIBUT EQUIPMENT
# ============================================
BASE_DURABILITY = 10

# ============================================
# 7. DICT
# ============================================
DEBUFF = {
    "Crowd Control": {
        "Stun": 2,
        "Slow": 2,
        "Knockback": 2,
        "pull": 2,
        "freeze": 2
    },
    "Utility": {
        "Blind": 2,
        "Taunt": 2, 
        "Charm": 2,
        "Fear": 2,
        "Sleep": 2,
        "Silence": 2
    },
    "Damage over Time": {
        "Born": 2,
        "Poison": 2,
        "Bleed": 2,
        "Corrosion": 2
    }
}

# ============================================
# 8. SLOT SKILL
# ============================================
SKILL = {
    1: "Skill 1",
    2: "Skill 2",
    3: "Skill 3",
    4: "Skill 4"
}

# ============================================
# 9. MAIN OPTION
# ============================================
MENU_OPTIONS = {
    1: "Lobby",
    2: "Shop",
    3: "Exit"
}

LOBBY_ROOM = {
    1: "Tower Gate",
    2: "Barracks",
    3: "Summoning Room",
    4: "Armory",
    5: "Back"
}

TOWER_FLOOR = {
    1: "The Threshold",
    2: "Back"
}

SUMMONING_TYPE = {
    1: "Summon a Hero",
    2: "Summon a Equipment",
    3: "Back"
}

CARD_SUMMONING = {
    1: "Use Card Free",
    2: "Use Card Crystal",
    3: "Back"
}
