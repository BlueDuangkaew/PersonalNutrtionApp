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
                food_name TEXT NOT NULL, 
                calories REAL, 
                fat REAL, 
                carbs REAL, 
                sodium REAL
            );

        """
    execute_query(connection, create_table_query)

    create_food_table = """
    INSERT INTO food (food_name, calories, fat, carbs, sodium) VALUES
    ('apple', 52, 0.2, 14, 1),
    ('banana', 89, 0.3, 23, 1),
    ('pear', 57, 0.1, 15, 1),
    ('mango', 60, 0.4, 15, 2),
    ('pineapple', 50, 0.1, 13, 1),
    ('kiwi', 61, 0.5, 15, 3),
    ('watermelon', 30, 0.2, 7.6, 1),
    ('pomegranate', 83, 1.2, 19, 3),
    ('papaya', 43, 0.3, 11, 1),
    ('plum', 46, 0.3, 11.4, 0),
    ('peach', 39, 0.3, 10, 0),
    ('grapes', 69, 0.2, 18, 2),
    ('cherries', 50, 0.3, 12, 3),
    ('raspberries', 52, 0.7, 12, 1),
    ('blackberries', 43, 0.5, 10, 1),
    ('cranberries', 46, 0.1, 12, 2),
    ('gooseberries', 44, 0.6, 10, 1),
    ('lychee', 66, 0.4, 17, 1),
    ('figs', 74, 0.3, 19.2, 0),
    ('dates', 282, 0.4, 75, 1),
    ('prunes', 240, 0.4, 64, 2),
    ('apricot', 48, 0.4, 11, 1),
    ('nectarine', 44, 0.3, 10.6, 0),
    ('coconut water', 19, 0.2, 4.4, 105),
    ('coconut milk', 230, 24, 6, 25),
    ('almond milk', 15, 1.1, 0.6, 150),
    ('soy milk', 54, 1.8, 6, 44),
    ('rice milk', 47, 1, 9.1, 86),
    ('oat milk', 50, 1.5, 9.4, 92),
    ('hazelnut milk', 29, 2.8, 1.2, 12),
    ('cashew milk', 25, 2, 1.4, 5),
        ('macadamia milk', 95, 50, 1, 5.2),
    ('pea protein milk', 120, 70, 0.1, 4.5),
    ('flax milk', 50, 25, 2.5, 2.5),
    ('hemp milk', 125, 60, 5, 4.5),
    ('potato', 6, 77, 17, 0.1),
    ('yam', 21, 118, 28, 0.2),
    ('bok choy', 65, 13, 2.2, 0.2),
    ('cabbage', 18, 25, 6, 0.1),
    ('brussels sprouts', 25, 43, 9, 0.3),
    ('collard greens', 27, 32, 5.9, 0.6),
    ('mustard greens', 20, 27, 4.7, 0.4),
    ('seaweed', 233, 45, 9.1, 0.6),
    ('turnip', 67, 28, 6.4, 0.1),
    ('radish', 39, 16, 3.4, 0.1),
    ('leek', 20, 61, 14.2, 0.3),
    ('celery', 80, 16, 3, 0.2),
    ('artichoke', 120, 64, 14.3, 0.4),
    ('asparagus', 6, 20, 3.7, 0.2),
    ('green beans', 13, 31, 7, 0.1),
    ('carrot', 88, 41, 10, 0.2),
    ('beet', 35, 43, 10, 0.2),
    ('sweet potato', 76, 86, 20, 0.1),
    ('butternut squash', 67, 45, 12, 0.1),
    ('zucchini', 33, 17, 3.1, 0.3),
    ('pumpkin', 49, 26, 6.5, 0.1),
    ('cucumber', 90, 15, 3.6, 0.2),
    ('bell pepper', 150, 20, 4.6, 0.2),
    ('eggplant', 110, 25, 6, 0.2),
    ('spinach', 91, 23, 3.6, 0.4),
    ('kale', 45, 49, 8.8, 0.9),
    ('broccoli', 92, 34, 6.6, 0.4),
    ('cauliflower', 146, 25, 5, 0.3),
    ('arugula', 108, 25, 3.7, 0.7),
    ('green peas', 89, 81, 14, 0.4),
    ('okra', 73, 33, 7.5, 0.2),
    ('chard', 101, 19, 3.7, 0.2),
    ('fennel', 87, 31, 7, 0.2),
    ('parsnip', 78, 75, 18, 0.3),
    ('turnip greens', 123, 29, 6.3, 0.4),
    ('chicory', 145, 23, 4.7, 0.3),
    ('endive', 95, 17, 3.4, 0.1),
    ('escarole', 85, 19, 3.8, 0.2),
    ('romaine lettuce', 102, 17, 3.3, 0.3),
    ('red leaf lettuce', 120, 16, 3, 0.2),
    ('butterhead lettuce', 105, 13, 2.2, 0.3),
    ('watercress', 79, 11, 1.3, 0.1),
    ('bamboo shoots', 120, 27, 5.2, 0.3),
    ('sprouts', 67, 29, 5.5, 0.2),
    ('mushrooms', 58, 22, 3.3, 0.3),
    ('tomato', 150, 18, 3.9, 0.2),
    ('green onion', 45, 32, 7.3, 0.2),
    ('kohlrabi', 140, 36, 8.4, 0.1),
    ('garlic', 1, 149, 33, 0.5),
    ('shallots', 72, 72, 16.8, 0.1),
    ('onion', 64, 44, 10.1, 0.1),
    ('chives', 3, 30, 6.4, 0.1),
    ('parsley', 34, 36, 6.3, 0.6),
    ('coriander', 2, 23, 5.2, 0.5),
    ('dill', 1, 43, 7, 0.5),
    ('rosemary', 2, 131, 20.7, 5.9),
    ('thyme', 3, 101, 24.5, 1.7),
    ('basil', 1, 22, 4.3, 0.6),
    ('oregano', 1, 265, 68.9, 4.3),
    ('marjoram', 1, 271, 60.6, 7.6);


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
    fat = food_info.get('fat')
    carbs = food_info.get('carbs')
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
            INSERT INTO food (food_name, calories, fat, carbs, sodium)
            VALUES ('{food_name}', {calories}, {fat}, {carbs}, {sodium});
            """
            try:
                execute_query(connection, insert_query)
                print(f"Food '{food_name}' added to the database.")
            except sqlite3.Error as e:
                print(f"Error adding food to the database: {e}")
    else:
        print("Invalid food information. Make sure 'food_name', 'calories', and 'sodium', 'carbs', 'fats'are provided.")

# function to find food name in the db
def find_food_name(connection, food_name):
    query = f"SELECT * FROM food WHERE food_name = '{food_name}'"
    rows = execute_query(connection, query)
    if rows: 
        print(f"Found {len(rows)} matching records for food name '{food_name}':")
        for row in rows:
            print(row)
    else:
        print(f"No records found for food name '{food_name}'")

if __name__ == "__main__":
    main()
    conn = create_connection(DB_FILE)
    if conn:
        # find a food named 'pizza' in the database
        find_food_name(conn, "pizza")

        # add a new food item to the database
        new_food_info = {
            'food_name': 'apple',
            'calories': 150,
            'fat': 0,
            'carbs' : 7,
            'sodium': 0.4
        }
        add_food(conn, new_food_info)

        # Close the connection
        conn.close()

