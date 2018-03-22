import sqlite3
from collect_stats import open_hands_stats, first_blood_stats, who_wins_stats, mana_starved

open_hand_db_conn = sqlite3.connect('Open_hands.db')
first_blood_db_conn = sqlite3.connect('First_blood.db')
mana_starved_db_conn = sqlite3.connect('Mana_starved.db')
who_wins_db_conn = sqlite3.connect('Who_wins.db')

def initialize_open_hand():
    open_hand_db_conn.execute("DROP TABLE IF EXISTS Open_hands")
    open_hand_db_conn.commit()
    try:
        open_hand_db_conn.execute(
            "CREATE TABLE Open_hands(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Mana INTEGER NOT NULL, "
            "Game INTEGER NOT NULL, Player TEXT NOT NULL, Hand INTEGER NOT NULL);")
        open_hand_db_conn.commit()

        # print("Table Created")

    except sqlite3.OperationalError:
        print("Table couldn't be Created")


def insert_into_open_hand_db():
    for item in open_hands_stats:
        open_hand_db_conn.execute("INSERT INTO Open_hands (Mana, Game, Player, Hand) VALUES ('" + str(item[0]) + "', '"
                                  + str(item[1]) + "', '" + str(item[2]) + "', '" + str(item[3]) + "')")


def get_open_hand_stats():
    initialize_open_hand()
    insert_into_open_hand_db()
    open_hand_cursor = open_hand_db_conn.cursor()
    try:
        result = open_hand_cursor.execute("SELECT Mana, Game, Player, Hand FROM Open_hands")
        for item in result:
            yield list(item)

    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")

    except:
        print("Couldn't Retrieve Data From Database")


def initialize_first_blood():
    first_blood_db_conn.execute("DROP TABLE IF EXISTS First_blood")
    first_blood_db_conn.commit()
    try:
        first_blood_db_conn.execute(
            "CREATE TABLE First_blood(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Mana INTEGER NOT NULL, "
            "Game INTEGER NOT NULL, Round INTEGER NOT NULL, Player TEXT NOT NULL, Method TEXT NOT NULL, "
            "GoesFirst INTEGER NOT NULL);")
        first_blood_db_conn.commit()

        # print("Table Created")

    except sqlite3.OperationalError:
        print("Table couldn't be Created")


def insert_into_first_blood_db():
    for item in first_blood_stats:
        first_blood_db_conn.execute("INSERT INTO First_blood (Mana, Game, Round, Player, Method, GoesFirst) VALUES ('"
                                  + str(item[0]) + "', '" + str(item[1]) + "', '" + str(item[2]) + "', '" + str(item[3])
                                  + "', '" + str(item[4]) + "', '" + str(item[5]) + "')")


def get_first_blood_stats():
    initialize_first_blood()
    insert_into_first_blood_db()
    cursor = first_blood_db_conn.cursor()
    try:
        result = cursor.execute("SELECT Mana, Game, Round, Player, Method, GoesFirst FROM First_blood")
        for item in result:
            yield list(item)

    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")

    except:
        print("Couldn't Retrieve Data From Database")


def initialize_who_wins():
    who_wins_db_conn.execute("DROP TABLE IF EXISTS Who_wins")
    who_wins_db_conn.commit()
    try:
        who_wins_db_conn.execute(
            "CREATE TABLE Who_wins(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Mana INTEGER NOT NULL, "
            "Game INTEGER NOT NULL, Round INTEGER NOT NULL, Player TEXT NOT NULL, Method TEXT NOT NULL, "
            "GoesFirst TEXT NOT NULL);")
        who_wins_db_conn.commit()

        # print("Table Created")

    except sqlite3.OperationalError:
        print("Table couldn't be Created")


def insert_into_who_wins_db():
    for item in who_wins_stats:
        who_wins_db_conn.execute("INSERT INTO Who_wins (Mana, Game, Round, Player, Method, GoesFirst) VALUES ('"
                                 + str(item[0]) + "', '" + str(item[1]) + "', '" + str(item[2])
                                 + "', '" + str(item[3]) + "', '" + str(item[4]) + "', '" + str(item[5]) + "')")


def get_who_wins_stats():
    initialize_who_wins()
    insert_into_who_wins_db()
    cursor = who_wins_db_conn.cursor()
    try:
        result = cursor.execute("SELECT Mana, Game, Round, Player, Method, GoesFirst FROM Who_wins")
        for item in result:
            yield list(item)

    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")

    except:
        print("Couldn't Retrieve Data From Database")


def initialize_mana_starved():
    mana_starved_db_conn.execute("DROP TABLE IF EXISTS Mana_starved")
    mana_starved_db_conn.commit()
    try:
        mana_starved_db_conn.execute(
            "CREATE TABLE Mana_starved(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Mana INTEGER NOT NULL, "
            "Game INTEGER NOT NULL, Round INTEGER NOT NULL, Player TEXT NOT NULL, GoesFirst TEXT NOT NULL);")
        mana_starved_db_conn.commit()

        # print("Table Created")

    except sqlite3.OperationalError:
        print("Table couldn't be Created")


def insert_into_mana_starved_db():
    for item in mana_starved:
        mana_starved_db_conn.execute("INSERT INTO Mana_starved (Mana, Game, Round, Player, GoesFirst) VALUES ('"
                                     + str(item[0]) + "', '" + str(item[1]) + "', '" + str(item[2])
                                     + "', '" + str(item[3]) + "', '" + str(item[4]) + "')")


def get_mana_starved_stats():
    initialize_mana_starved()
    insert_into_mana_starved_db()
    cursor = mana_starved_db_conn.cursor()
    try:
        result = cursor.execute("SELECT Mana, Game, Round, Player, GoesFirst FROM Mana_starved")
        for item in result:
            yield list(item)

    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")

    except:
        print("Couldn't Retrieve Data From Database")
