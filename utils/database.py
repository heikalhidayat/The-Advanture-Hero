from config.config import DATABASE_NAME
import sqlite3

def get_by_id(name, value, id):
    get_name = f"get_{name}_by_id"
    def get_name(id):
        conn = sqlite3.connect(DATABASE_NAME)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {name} WHERE {value} = ?", (id))
        result = cursor.fetchone()

        conn.close()
        return dict(result)

    return get_name(id)

def init_database():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS username (
            id_player INTEGER PRIMARY KEY,
            user_name VARCHAR(50)
        )
    '''
    )
    
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS inventory (
            id_item INTEGER PRIMARY KEY AUTOINCREMENT,
            id_player INTEGER,
            item_name VARCHAR(50)
        )
    '''
    )
    
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS pocket (
            id_pocket INTEGER PRIMARY KEY AUTOINCREMENT,
            id_player INTEGER PRIMARY KEY,
            gold_player INTEGER
        )
    '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS karakter (
            id_karakter INTEGER PRIMARY KEY AUTOINCREMENT,
            id_player INTEGER,
            name VARCHAR,
            job VARCHAR,
            tier INTEGER,
            level INTEGER,
            exp INTEGER,
            skill_01 VARCHAR,
            skill_02 VARCHAR,
            skill_03 VARCHAR,
            skill_04 VARCHAR,
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
            agility_bonus INTEGER, 
            defense_bonus INTEGER,
            magic_bonus INTEGER,
            dexterity_bonus INTEGER,
            resistance_bonus INTEGER
        )
    '''
    )
    
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS skills (
            id_skills INTEGER PRIMARY KEY AUTOINCREMENT,
            id_player INTEGER,
            name VARCHAR,
            category VARCHAR,
            armed INTEGER,
            range_type VARCHAR,
            debuff VARCHAR,
            level INTEGER,
            competence INTEGER,
            energy INTEGER, 
            mana INTEGER,
            strength INTEGER,
            agility INTEGER,
            defense INTEGER,
            vitality INTEGER,
            magic INTEGER,
            dexterity INTEGER,
            resistance INTEGER,
            intelligence INTEGER
        )
    '''
    )

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS equipment (
            id_equipment INTEGER PRIMARY KEY AUTOINCREMENT,
            id_player INTEGER,
            name VARCHAR,
            category VARCHAR,
            kind VARCHAR,
            price INTEGER,
            capacity INTEGER,
            base_durability INTEGER,
            current_durability INTEGER,
            strength INTEGER,
            agility INTEGER,
            defense INTEGER,
            magic INTEGER,
            dexterity INTEGER,
            resistance INTEGER
        )
    '''
    )
    
    conn.commit()
    conn.close()