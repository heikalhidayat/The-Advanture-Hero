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
BASE_MANA = 50
BASE_STRENGTH = 10
BASE_AGILITY = 10
BASE_DEFENSE = 10

# ============================================
# 3. BALANCING EXP & LEVEL UP
# ============================================
EXP_MULTIPLIER = 2          # Batas EXP berlipat ganda saat level up
STAT_INCREASE_HP = 10       # Penambahan HP saat level up
STAT_INCREASE_DAMAGE = 5    # Penambahan Damage saat level up
STAT_INCREASE_AGILITY = 5   # Penambahan Agility saat level up
STAT_INCREASE_DEFENSE = 5   # Penambahan Defense saat level up

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
}

CLASS_KARAKTER_CARD = {
    1: "Mage",
    2: "Warrior",
    3: "Guardian",
    4: "Assassin",
    5: "Archer"
}
