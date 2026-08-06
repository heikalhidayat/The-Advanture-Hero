from config import DATABASE_NAME
import sqlite3

def init_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS username (
        id_player INTEGER PRIMARY KEY,
        user_name VARCHAR(50))
        ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
        id_item INTEGER PRIMARY KEY AUTOINCREMENT,
        id_player INTEGER,
        item_name VARCHAR(50))
        ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pocket (
        id_player INTEGER PRIMARY KEY,
        gold_player INTEGER)
        ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS karakter (
        id_player INTEGER,
        name VARCHAR,
        job VARCHAR,
        tier INTEGER,
        level INTEGER,
        exp INTEGER,
        base_hp INTEGER,
        base_energy INTEGER,
        base_mana INTEGER,
        strength INTEGER,
        agility INTEGER,
        defense INTEGER,
        vitality INTEGER,
        magic INTEGER,
        dexterity INTEGER,
        resistance INTEGER,
        intelligence INTEGER,
        strength_bonus INTEGER,
        aility_bonus INTEGER, 
        defense_bonus INTEGER,
        magic_bonus INTEGER,
        dexterity_bonus INTEGER,
        resistance_bonus INTEGER
        ''')
    
    conn.commit()
    conn.close()
