"""
find_food_name.py

This module contains functions for the food database.

Funtions: 
    find_food_name
    add_food
"""

import sqlite3

__author__ = "Peach, Pokpong"


# Constants
DB_FILE = "food_database.db"
_COLUMN_INFOS = {"id": "INTEGER PRIMARY KEY AUTOINCREMENT", 
                 "food_name": "TEXT NOT NULL UNIQUE", 
                 "calories": "REAL", 
                 "fat": "REAL", 
                 "carbs": "REAL", 
                 "sodium": "REAL"}
FOOD_INFO_KEYS = tuple(_COLUMN_INFOS.keys())[1:]

# This function formats the a row of data from the database
def _format_rows(rows: list[tuple]) -> list[dict]:
    format_row = lambda row : dict(zip(FOOD_INFO_KEYS, row[1:]))
    
    if isinstance(rows, tuple):
        rows = format_row(rows)
    else:
        rows = [format_row(row) for row in rows]
    return rows


#create db then fill with food
def create_food_table():
    create_table_query = f"""
            CREATE TABLE IF NOT EXISTS food (
            {', '.join([f"{k} {v}" for k, v in _COLUMN_INFOS.items()])}
            );
        """
    execute_query(create_table_query)

#fill the table with info of db
def fill_food_table():
    create_food_table = f"""
    INSERT INTO food ({', '.join(FOOD_INFO_KEYS)}) VALUES
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
    execute_query(create_food_table)

# to create the connection to db
def create_connection(db_file: str):
    """Create a database connection to a SQLite database"""
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(f"Error: '{e}'")
        return None
    return conn

#to exectue query
def execute_query(query: str):
    connection = create_connection(DB_FILE)
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        # if the query is a SELECT statement, fetch the results.
        if query.strip().upper().startswith("SELECT"):
            return cursor.fetchall()
        else:
            connection.commit()
            return cursor.lastrowid 
    except sqlite3.Error as e:
        print(f"Error: '{e}'")
    finally:
        cursor.close()

#prints rows
def fetch_all_rows(query: str):
    rows = execute_query(query)
    print(_format_rows(rows))

#add new food to db
def add_food(food_info: dict):
    values = tuple(food_info.values())
    print(values)
    if (tuple(food_info.keys()) != FOOD_INFO_KEYS 
            or None in values):
        print("Cannot add empty data.")
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

#find food name in db
def find_food_name(food_name: str) -> dict:
    query = f"SELECT * FROM food WHERE food_name = '{food_name}'"
    rows = execute_query(query)

    if not rows:
        raise Exception("No matching data.")
    return _format_rows(rows[0])

# # Example usage
# if __name__ == "__main__":
#     conn = create_connection(DB_FILE)
#     if conn:
#         # Assuming you've already created a table and inserted data
#         find_food_name(conn, "pizza")
#         conn.close()