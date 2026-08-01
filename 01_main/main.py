# Import library yang dibutuhkan
import copy
import sqlite3
import time
import random

# Import constanta
from config import DATABASE_NAME, MENU_OPTIONS, CLASS_KARAKTER_CARD, LOBBY_ROOM
from database import init_database
from karakter import Karakter, Mage, Warrior, Guardian, Assassin, Archer

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

        print(f"\n[LOADING] WELCOME, {user_name} (ID: {id_player})")
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
    print("1. Lobby")
    print("2. karakter")
    print("3. Shop")
    print("4. Exit")

def lobby():
    print("\n============== LOBBY ==============\n")
    print("1. Tower Gate")
    print("2. Barracks")
    print("3. Training Area")
    print("4. Armory")
    print("5. Dining Hall")

def karakter_card():
    print("\n--------------- KARAKTER ---------------")
    print("\nHERO CARD :")
    print("1. Mage")
    print("2. Warrior")
    print("3. Guardian")
    print("4. Assassin")
    print("5. Archer")

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
            exit_bottom("enter", "continue")

        elif menu_choice == 2:
            karakter_card()
            card_choice = get_choice("your hero", CLASS_KARAKTER_CARD)

            if card_choice == 1:
                print(Mage("Mage"))
                exit_bottom("enter", "continue")

            elif card_choice == 2:
                print(Warrior("Warrior"))
                exit_bottom("enter", "continue")

            elif card_choice == 3:
                print(Guardian("Guardian"))
                exit_bottom("enter", "continue")

            elif card_choice == 4:
                print(Assassin("Assassin"))
                exit_bottom("enter", "continue")

            elif card_choice == 5:
                print(Archer("Archer"))
                exit_bottom("enter", "continue")

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
