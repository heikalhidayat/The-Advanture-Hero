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
STAT_INCREASE_HP = 10         # Penambahan HP saat level up
STAT_INCREASE_ENERGY = 10     # Penambahan energy saat level up
STAT_INCREASE_MANA = 10       # Penambahan mana saat level up
STAT_INCREASE_STRENGTH = 10   # Penambahan Strength saat level up
STAT_INCREASE_AGILITY = 10    # Penambahan Agility saat level up
STAT_INCREASE_DEFENSE = 10    # Penambahan Defense saat level up
STAT_INCREASE_MAGIC = 10      # Penambahan Magic saat level up
STAT_INCREASE_DEXTERITY = 10  # Penambahan Dexterity saat level up
STAT_INCREASE_RESISTANCE = 10 # Penambahan Resistance saat level up

# ============================================
# 
# ============================================
MENU_OPTIONS = {
    1: "Lobby",
    2: "Karakter",
    3: "Shop",
    4: "Exit"
}

LOBBY_ROOM = {
    1: "Tower Gate",
    2: "Barracks",
    3: "Training Area",
    4: "Armory",
    5: "Dining Hall"
    6: "Summoning Room"
}

CLASS_KARAKTER_CARD = {
    1: "Mage",
    2: "Warrior",
    3: "Guardian",
    4: "Assassin",
    5: "Archer"
}

SUMMONING_TYPE = {
    1: "Use Card Free",
    2: "Use Card Crystal",
}
