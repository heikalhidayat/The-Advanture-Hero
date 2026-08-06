# Import library yang dibutuhkan
import copy
import sqlite3
import time
import random

# Import constanta
from config import DATABASE_NAME, MENU_OPTIONS, CLASS_KARAKTER_CARD, LOBBY_ROOM, SUMMONING_TYPE, TOWER_FLOOR

# Import database
from database import init_database

# Import karakter
from karakter import Mage, Tank, Assassin, Support, Marksman, Fighter, Wizard, Necromancer

# Import monster
from normal_enemy import Slime

def jeda_loading(second):
     '''jeda loading'''
     for i in range(5):
         print(".", end="")
         time.sleep(second)


def login():
    user_name = input("Masukkan username: ")

    conn = sqlite3.connect(DATABASE_NAME)
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
        cursor.execute("SELECT gold_player FROM wallet WHERE id_player = ?", (id_player,))
        gold_player = cursor.fetchone()[0]

        print(f"\nGold: {gold_player}")

    else:
        cursor.execute("INSERT INTO username (user_name) VALUES (?)", (user_name,))
        conn.commit()
        id_player = cursor.lastrowid
        cursor.execute("INSERT INTO inventory (id_player) VALUES (?)", (id_player,))
        cursor.execute("INSERT INTO wallet (id_player) VALUES (?)", (id_player,))
        conn.commit()
        items = []
        gold_player = 0

        print(f"\n[LOADING] WELCOME... {user_name} (ID: {id_player})")
        time.sleep(1)

    conn.close()

    return id_player, user_name, items, gold_player

class InvalidMenuChoiceError(Exception):
    pass

def get_choice(x, y):
    while True:
        try:
            choice = int(input(f"\nchoice {x}: "))

            if choice not in y:
                raise InvalidMenuChoiceError

            return choice

        except ValueError:
            print("Invalid input. Please enter a number.")

        except InvalidMenuChoiceError as e:
            print(f"Invalid input {e}")

def exit_bottom(x, y):
    input(f"\nPress {x} to {y}...") 

def menu():
    print("\n============== MENU UTAMA ==============\n")
    for i,(number, option) in enumerate(MENU_OPTIONS.items()):
        print(f"{i+1}. {option}")

def lobby():
    print("-" * 40)
    print("================= LOBBY ================")
    print("-" * 40, "\n")
    for i,(number, option) in enumerate(LOBBY_ROOM.items()):
        print(f"{i+1}. {option}")

def tower_floor():
    print("\n======== Go Beyond Your Limits =========")
    print("-" * 40)
    for i,(number, option) in enumerate(TOWER_FLOOR.items()):
        print(f"{i+1}. {option}")

def monster():
    print("\nDefeat the enemies in front of you!\n")
    tier_monster = random.randint(1, 3)
    level_monster = random.randint(1, 5)                
    total_exp = random.randint(100, 200) * (tier_monster * level_monster)
    print(Slime(tier=tier_monster, level=level_monster, exp=total_exp).__str_monster__())

def barracks():
    print("\n=============== BARRACKS ===============")
    print("-" * 40)

def training_area():
    print("\n============= TRAINING AREA ============")
    print("-" * 40)

def armory():
    print("\n================ ARMORY ================")
    print("-" * 40)

def dining_hall():
    print("\n============== DINING HALL =============")
    print("-" * 40)

def summoning_room():
    print("\n=========== Summoning ROOM ============\n")
    for i,(number, option) in enumerate(SUMMONING_TYPE.items()):
        print(f"{i+1}. {option}")

def karakter_summon():
    list_karakter = [Mage(), Tank(), Assassin(), Support(), Marksman(), Fighter(), Wizard(), Necromancer()]
    summoning_free = random.choice(list_karakter)
    print(f"Selamat Master! Anda mendapatkan Hero:\n\n {summoning_free.__str_physic__()}")

def main():
    init_database()
    id_player, user_name, items, gold_player = login()

    print("\n", "-" * 40, "\n   Welcome In Game The Advanture Hero   \n", "-" * 40, sep="")

    while True:
        menu()
        menu_choice = get_choice("menu", MENU_OPTIONS)

        if menu_choice == 1:
            lobby()
            lobby_choice = get_choice("Lobby", LOBBY_ROOM)

            if lobby_choice == 1:
                tower_floor()
                tower_floor_choice = get_choice("Tower Floor", TOWER_FLOOR)

                if tower_floor_choice == 1:
                    monster()

                exit_bottom("enter", "continue")

            elif lobby_choice == 2:
                barracks()
                exit_bottom("enter", "continue")

            elif lobby_choice == 3:
                training_area()
                exit_bottom("enter", "continue")

            elif lobby_choice == 4:
                armory()
                exit_bottom("enter", "continue")

            elif lobby_choice == 5:
                dining_hall()
                exit_bottom("enter", "continue")

            elif lobby_choice == 6:
                summoning_room()
                summoning_choice = get_choice("Your card summoning", SUMMONING_TYPE)
                if summoning_choice == 1:
                    karakter_summon()
                    exit_bottom("enter", "continue")

                elif summoning_choice == 2:
                    exit_bottom("enter", "continue")

        elif menu_choice == 2:
            pass

        elif menu_choice == 3:
            pass

        elif menu_choice == 4:
            print("\nThank you for playing!")
            break

# =================================================
# MAIN PROGRAM
# =================================================
if __name__ == "__main__":
    main()
