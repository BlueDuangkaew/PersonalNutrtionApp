# find_food_name.py
# This module contains functions for the food database.

import sqlite3
import pandas as pd

__author__ = "Peach"

# Constants
DB_FILE = "food_database.db"

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

def add_food(connection, food_info):
    food_name = food_info.get('food_name')
    calories = food_info.get('calories')
    sodium = food_info.get('sodium')

    if food_name and calories is not None and sodium is not None:
        insert_query = f"""
        INSERT INTO food (food_name, calories, sodium)
        VALUES ('{food_name}', {calories}, {sodium});
        """
        try:
            execute_query(connection, insert_query)
            print(f"Food '{food_name}' added to the database.")
        except sqlite3.Error as e:
            print(f"Error adding food to the database: {e}")
    else:
        print("Invalid food information. Make sure 'food_name', 'calories', and 'sodium' are provided.")

def find_food_name(connection, food_name):
    query = f"SELECT * FROM food WHERE food_name = '{food_name}'"
    rows = execute_query(connection, query)
    if rows:
        print(f"Found {len(rows)} matching records for food name '{food_name}':")
        for row in rows:
            print(row)
    else:
        print(f"No records found for food name '{food_name}'")

# Example usage
if __name__ == "__main__":
    conn = create_connection(DB_FILE)
    if conn:
        # Assuming you've already created a table and inserted data
        find_food_name(conn, "pizza")
        conn.close()
