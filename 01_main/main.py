# Import library yang dibutuhkan
import copy
import sqlite3
import time
import random

# Import constanta
from config.config import DATABASE_NAME, MENU_OPTIONS
from utils.database import init_database

def login():
    user_name = input("Masukkan username: ")

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Cek apakah sudah terdaftar
    cursor.execute("SELECT id_player, user_name FROM username WHERE user_name = ?", (user_name,))
    data_player = cursor.fetchone()

    if data_player is not None:
        id_player = data_player[0]
        print(f"Welcome back {user_name} (ID: {id_player})")

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

def menu():
    print("\n------- MENU UTAMA -------")
    print("1. Main")
    print("2. Status karakter")
    print("3. Shop")
    print("4. Exit")

class InvalidMenuChoiceError(Exception):
    pass

def get_menu_choice():
    while True:
        try:
            choice = int(input("choice menu: "))

            if choice not in MENU_OPTIONS:
                raise InvalidMenuChoiceError

            return choice

        except ValueError:
            print("Invalid input. Please enter a number.")

        except InvalidMenuChoiceError as e:
            print(f"Invalid Input! {e}")

def main():
    init_database()
    id_player, user_name, items, gold_player = login()

    print("-" * 40, "\n   Welcome In Game The Advanture Hero   \n", "-" * 40, sep="")

    while True:
        menu()
        choice = get_menu_choice()

        if choice == 1:
            pass

        if choice == 2:
            print("\n--------------- KARAKTER ---------------")
            print("HERO CARD")

# =================================================
# MAIN PROGRAM
# =================================================
if __name__ == "__main__":
    main()
