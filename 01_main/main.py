# Import library yang dibutuhkan
import copy
import sqlite3
import time
import random

# Import constanta
from config.config import DATABASE_NAME
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
        print(f"Welcome back {user_name}")
        
        # Load inventori dan wallet
        cursor.execute("SELECT item_name FROM inventory WHERE id_player = ?", (id_player,))
        items = [item[0] for item in cursor.fetchall()]

        cursor.execute("SELECT gold_player FROM wallet WHERE id_player = ?", (id_player,))
        gold_player = cursor.fetchone()[0]
        print(f"Inventory: {items}")
        print(f"Gold: {gold_player}")

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

def validasi_menu():
    print("-" * 40, "\n   Welcome In Game The Advanture Hero   \n", "-" * 40, sep="")
    print("1. Main")
    print("2. Status karakter")
    print("3. Shop")
    print("4. Exit")

init_database()
login()
validasi_menu()
