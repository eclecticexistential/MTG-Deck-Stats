import sqlite3
from collect_stats import open_hands_stats

open_hand_db_conn = sqlite3.connect('Open_hands.db')


def initialize_open_hand():
    open_hand_db_conn.execute("DROP TABLE IF EXISTS Open_hands")
    open_hand_db_conn.commit()
    try:
        open_hand_db_conn.execute(
            "CREATE TABLE Open_hands(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Mana INTEGER NOT NULL, "
            "Game INTEGER NOT NULL, Player TEXT NOT NULL, Hand INTEGER NOT NULL);")
        open_hand_db_conn.commit()

        print("Table Created")

    except sqlite3.OperationalError:
        print("Table couldn't be Created")


def insert_into_open_hand_db():
    for item in open_hands_stats:
        open_hand_db_conn.execute("INSERT INTO Open_hands (Mana, Game, Player, Hand) VALUES ('" + str(item[0]) + "', '"
                                  + str(item[1]) + "', '" + str(item[2]) + "', '" + str(item[3]) + "')")


def get_open_hand_stats():
    initialize_open_hand()
    insert_into_open_hand_db()
    cursor = open_hand_db_conn.cursor()
    try:
        result = cursor.execute("SELECT Mana, Game, Player, Hand FROM Open_hands")
        for item in result:
            print(list(item))

    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")

    except:
        print("Couldn't Retrieve Data From Database")

get_open_hand_stats()