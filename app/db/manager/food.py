# find_food_name.py
# This module contains functions for the food database.

import sqlite3
import pandas as pd

__author__ = "Peach"

# Constants
DB_FILE = "food_database.db"
_COLUMN_INFOS = {"id": "INTEGER PRIMARY KEY AUTOINCREMENT", 
                 "food_name": "TEXT NOT NULL", 
                 "calories": "REAL", 
                 "fat": "REAL", 
                 "carbs": "REAL", 
                 "sodium": "REAL"}
FOOD_INFO_KEYS = tuple(_COLUMN_INFOS.keys())[1:]

def _format_rows(rows: list[tuple]) -> list[dict]:
    # This function formats the a row of data from the database
    format_row = lambda row : dict(zip(FOOD_INFO_KEYS, row[1:]))
    
    if isinstance(rows, tuple):
        rows = format_row(rows)
    else:
        rows = [format_row(row) for row in rows]
    return rows

# Database Management Functions

#create db then fill with food
def create_food_table():
    create_table_query = f"""
            CREATE TABLE IF NOT EXISTS food (
            {', '.join([f"{k} {v}" for k, v in _COLUMN_INFOS.items()])}
            );
        """
    print(', '.join([f"{k} {v}" for k, v in _COLUMN_INFOS.items()]))
    execute_query(create_table_query)

def create_connection(db_file):
    """Create a database connection to a SQLite database"""
    try:
        conn = sqlite3.connect(db_file)
        print("SQLite Database connection successful")
        return conn
    except sqlite3.Error as e:
        print(f"Error: '{e}'")
        return None

def execute_query(query):
    connection = create_connection(DB_FILE)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        # If the query is a SELECT statement, fetch the results.
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            connection.commit()
            return cursor.lastrowid  # In case you need the id of the row just inserted
    except sqlite3.Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()

def fetch_all_rows(query):
    rows = execute_query(query)
    print(_format_rows(rows))

def add_food(food_info: dict):
    values = tuple(food_info.values())
    print(values)
    if (tuple(food_info.keys()) != FOOD_INFO_KEYS 
            or None in values 
            or 0 in values):
        print("Invalid food information. Make sure 'food_name', 'calories', and 'sodium' are provided.")
        return

    insert_query = f"""
    INSERT INTO food ({', '.join(FOOD_INFO_KEYS)})
    VALUES ('{values[0]}', {', '.join(map(str, values[1:]))});
    """
    print(insert_query)
    try:
        execute_query(insert_query)
        print(f"Food '{values[0]}' added to the database.")
    except sqlite3.Error as e:
        print(f"Error adding food to the database: {e}")

def find_food_name(food_name):
    query = f"SELECT * FROM food WHERE food_name = '{food_name}'"
    rows = execute_query(query)

    if not rows:
        raise Exception("No matching data.")
    return _format_rows(rows)

# # Example usage
# if __name__ == "__main__":
#     conn = create_connection(DB_FILE)
#     if conn:
#         # Assuming you've already created a table and inserted data
#         find_food_name(conn, "pizza")
#         conn.close()
