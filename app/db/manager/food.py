"""
find_food_name.py

This module contains functions for the food database.

Funtions: 
    find_food_name
    add_food
"""

import sqlite3
import pandas as pd

__author__ = "Peach"

# constant
DB_FILE = "food_database.db"

# create a database connection to a SQLite database

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print("SQLite Database connection successful")
        return conn
    except sqlite3.Error as e:
        print(f"Error: '{e}'")
        return None

# will execute the query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        # if the query is a SELECT statement then it will fetch the results
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            connection.commit()
            return cursor.lastrowid  
    except sqlite3.Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()

# will fetch all rows
def fetch_all_rows(connection, query):
    rows = execute_query(connection, query)
    for row in rows:
        print(row)

# Check if a table exists in the SQLite database.
def check_table_exists(connection, table_name):
   
    check_query = f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table_name}'"
    cursor = connection.cursor()
    cursor.execute(check_query)
    if cursor.fetchone()[0] == 1:
        return True
    return False

#create db then fill with food
def create_and_populate_food_table(connection):
    create_table_query = """
            CREATE TABLE IF NOT EXISTS food (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                food_name TEXT NOT NULL,
                calories INTEGER NOT NULL,
                sodium REAL
            );
        """
    execute_query(connection, create_table_query)

    create_food_table = """
    INSERT INTO food (id, food_name, calories, sodium) VALUES
    (1, 'oatmeal', 90, 1.5),
    (2, 'tempura', 350, 1.3),
    (3, 'burger', 365, 0.2),
    (4, 'pizza', 256, 0.1),
    (5, 'sushi', 483, 0.9),
    (6, 'garlic', 449, 1.3),
    (7, 'sushi', 96, 0.9),
    (8, 'banana', 489, 1.3),
    (9, 'muffin', 445, 0.2),
    (10, 'blueberry', 368, 1.2),
    (11, 'taco', 457, 1.5),
    (12, 'sandwich', 201, 1.1),
    (13, 'lobster', 125, 0.2),
    (14, 'garlic', 383, 1.5),
    (15, 'burger', 425, 0.8),
    (16, 'onion', 99, 1.4),
    (17, 'avocado', 295, 0.3),
    (18, 'sandwich', 216, 1.1),
    (19, 'cheese', 53, 0.5),
    (20, 'beef stew', 111, 1.0),
    (21, 'honeydew', 198, 1.2),
    (22, 'bacon', 494, 1.4),
    (23, 'beef', 445, 0.5),
    (24, 'onion', 110, 0.8),
    (25, 'rice', 452, 0.2),
    (26, 'pancake', 164, 0.5),
    (27, 'bagel', 398, 0.4),
    (28, 'cucumber', 269, 0.6),
    (29, 'toast', 307, 0.4),
    (30, 'cheese', 108, 0.9),
    (31, 'toast', 289, 0.2),
    (32, 'pepper', 436, 1.3),
    (33, 'peach', 225, 0.9),
    (34, 'kale', 88, 0.5),
    (35, 'nectarine', 82, 0.4),
    (36, 'quinoa', 241, 0.3),
    (37, 'bagel', 277, 0.5),
    (38, 'cheese', 434, 0.5),
    (39, 'sushi', 285, 0.9),
    (40, 'lentils', 331, 0.9),
    (41, 'taco', 111, 1.1),
    (42, 'orange', 241, 0.8),
    (43, 'cucumber', 330, 1.2),
    (44, 'edamame', 118, 1.2),
    (45, 'bacon', 488, 0.7),
    (46, 'cherry', 108, 0.8),
    (47, 'muffin', 323, 1.4),
    (48, 'lemon', 88, 1.5),
    (49, 'zucchini', 434, 0.4),
    (50, 'cantaloupe', 328, 0.3),
    (51, 'blueberry', 375, 1.0),
    (52, 'rice', 369, 1.2),
    (53, 'doughnut', 147, 0.4),
    (54, 'olive', 464, 1.3),
    (55, 'croissant', 470, 0.6),
    (56, 'bread', 246, 1.1),
    (57, 'waffle', 127, 0.9),
    (58, 'zucchini', 441, 0.1),
    (59, 'blueberry', 424, 0.9),
    (60, 'figs', 313, 0.8),
    (61, 'raisins', 404, 0.1),
    (62, 'enchilada', 471, 0.4),
    (63, 'quesadilla', 363, 1.4),
    (64, 'grapes', 420, 1.3),
    (65, 'cheese', 58, 0.4),
    (66, 'waffle', 355, 0.2),
    (67, 'carrot', 285, 0.9),
    (68, 'tofu', 175, 1.4),
    (69, 'chocolate', 324, 0.3),
    (70, 'pork', 479, 1.2),
    (71, 'dates', 65, 0.5),
    (72, 'pineapple', 371, 0.5),
    (73, 'pad thai', 56, 0.8),
    (74, 'croissant', 163, 0.9),
    (75, 'edamame', 354, 1.3),
    (76, 'burrito', 210, 0.2),
    (77, 'brown bread', 443, 0.9),
    (78, 'pear', 211, 0.3),
    (79, 'barley', 496, 0.5),
    (80, 'carrot', 437, 0.5),
    (81, 'zucchini', 433, 0.4),
    (82, 'burrito', 155, 1.4),
    (83, 'ice cream', 266, 1.1),
    (84, 'wheat', 66, 1.2),
    (85, 'watermelon', 56, 1.1),
    (86, 'curry', 317, 1.0),
    (87, 'figs', 90, 1.4),
    (88, 'doughnut', 109, 0.7),
    (89, 'coconut', 167, 1.5);



    """

    execute_query(connection, create_food_table)


def main():
    # Connect to the SQLite database
    connection = create_connection(DB_FILE)

    # Check if the food table exists, if not, create it and insert the data
    if connection:
        if not check_table_exists(connection, 'food'):
            create_and_populate_food_table(connection)

        # Display all contents of the food table
        print("Current contents of the food table:")
        fetch_all_rows(connection, "SELECT * FROM food;")
        
        
    # Close connection
    if connection:
        connection.close()
        print("SQLite connection is closed")

#function to add food into the database
def add_food(connection, food_info):
    food_name = food_info.get('food_name')
    calories = food_info.get('calories')
    sodium = food_info.get('sodium')

    # check if all the necessary information is provided
    if food_name and calories is not None and sodium is not None:
        # check if the food already exists in the database
        check_query = f"SELECT * FROM food WHERE food_name = '{food_name}'"
        existing_food = execute_query(connection, check_query)
        
        if existing_food:
            print(f"The food '{food_name}' already exists in the database.")
        else:
            # food does not exist so insert it
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

# function to find food name in the db
def find_food_name(connection, food_name):
    query = f"SELECT * FROM food WHERE food_name = '{food_name}'"
    rows = execute_query(connection, query)

    if not rows:
        raise Exception("No matching data.")
    return rows

if __name__ == "__main__":
    main()
    conn = create_connection(DB_FILE)
    if conn:
        # find a food named 'pizza' in the database
        find_food_name(conn, "pizza")

        # add a new food item to the database
        new_food_info = {
            'food_name': 'peach',
            'calories': 150,
            'sodium': 0.4
        }
        add_food(conn, new_food_info)

        # Close the connection
        conn.close()
