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
    
    conn.commit()
    conn.close()
