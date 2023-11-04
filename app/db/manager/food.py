# find_food_name.py
# This module contains functions for the food database.

import sqlite3
import pandas as pd

__author__ = "Peach"

# Constants
DB_FILE = "food_database.db"
FOOD_INFO_KEYS = ("food_name", "calories", "fat", "carbs", "sodium")

# Database Management Functions

def create_connection(db_file):
    """Create a database connection to a SQLite database"""
    try:
        conn = sqlite3.connect(db_file)
        print("SQLite Database connection successful")
        return conn
    except sqlite3.Error as e:
        print(f"Error: '{e}'")
        return None

def execute_query(connection, query):
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

def fetch_all_rows(connection, query):
    rows = execute_query(connection, query)
    for row in rows:
        print(row)

def add_food(connection, food_info: dict):
    values = tuple(food_info.values())
    print(values)
    if (tuple(food_info.keys()) != FOOD_INFO_KEYS 
            or None in values 
            or 0 in values):
        print("Invalid food information. Make sure 'food_name', 'calories', and 'sodium' are provided.")
        return

    insert_query = f"""
    INSERT INTO food (food_name, calories, sodium)
    VALUES ('{values[0]}', {', '.join(map(str, values[1:]))});
    """
    try:
        execute_query(connection, insert_query)
        print(f"Food '{values[0]}' added to the database.")
    except sqlite3.Error as e:
        print(f"Error adding food to the database: {e}")

def find_food_name(connection, food_name):
    query = f"SELECT * FROM food WHERE food_name = '{food_name}'"
    rows = execute_query(connection, query)

    if not rows:
        raise Exception("No matching data.")
    return rows

# Example usage
if __name__ == "__main__":
    conn = create_connection(DB_FILE)
    if conn:
        # Assuming you've already created a table and inserted data
        find_food_name(conn, "pizza")
        conn.close()
