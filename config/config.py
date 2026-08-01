# ============================================
# 1. PENGATURAN DATABASE & SISTEM
# ============================================
DATABASE_NAME = "game.db"
GAME_TITLE = "The Adventure Hero"
GAME_VERSION = "0.0.1"

# ============================================
# 2. BALANCING BASE STATS PLAYER
# ============================================
PLAYER_DEFAULT_HP = 100
PLAYER_DEFAULT_ENERGY = 100
PLAYER_DEFAULT_MANA = 50
PLAYER_DEFAULT_DAMAGE = 10
PLAYER_DEFAULT_AGILITY = 10
PLAYER_DEFAULT_DEFENSE = 10
PLAYER_BASE_MAX_EXP = 100

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
    1: "lobby",
    2: "status karakter",
    3: "shop",
    4: "exit"
}

LOBBY_ROOM = {
    1: "tower gate",
    2: "hero_room",
    3: "training_area",
    4: "armory",
    5: "dining_area"
}

CLASS_KARAKTER_CARD = {
    1: "Warrior",
    2: "Mage",
    3: "Archer",
    4: "Assassin",
    5: "Guardian"
}
