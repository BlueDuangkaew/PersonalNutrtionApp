"""
find_food_name.py

This module contains functions for the food database.

Funtions: 
    find_food_name
    add_food
"""

import csv
import sqlite3

__author__ = "Peach, Pokpong"

# Constants
DB_FILE = "food_database.db"
_COLUMN_INFOS = {
    "id": {"attr": "INTEGER PRIMARY KEY AUTOINCREMENT"}, 
    "food_name": {"attr": "TEXT NOT NULL UNIQUE"}, 
    "calories": {"attr": "REAL", "unit": "cal"}, 
    "fat": {"attr": "REAL", "unit": "g"}, 
    "carbs": {"attr": "REAL", "unit": "g"}, 
    "sodium": {"attr": "REAL", "unit": "mg"}
}
FOOD_INFO_KEYS = tuple(_COLUMN_INFOS.keys())[1:]
NUTRITION_UNITS = tuple(v["unit"] for v in _COLUMN_INFOS.values() 
                        if "unit" in v)

# This function formats the a row of data from the database
def _format_rows(rows: list) -> list:
    format_row = lambda row : dict(zip(FOOD_INFO_KEYS, row[1:]))
    
    if isinstance(rows, tuple):
        rows = format_row(rows)
    else:
        rows = [format_row(row) for row in rows]
    return rows

#create db then fill with food
def create_food_table():
    """Create the food table in the SQLite database."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Define the SQL command to create the table
    create_table_command = """
    CREATE TABLE IF NOT EXISTS food (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        food_name TEXT NOT NULL UNIQUE,
        calories REAL,
        fat REAL,
        carbs REAL,
        sodium REAL
    );
    """
    cursor.execute(create_table_command)
    conn.commit()
    conn.close()

#fill in the table with info from csv file
def fill_in_table(csv_file_path: str):
    """
    Fill the food table with data from a CSV file.

    :param csv_file_path: Path to the CSV file containing food data.
    """
    db_file = DB_FILE  
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                row = [f"'{row[0]}'" for elem in row if isinstance(elem, str)]
                try:
                    cursor.execute(f"""INSERT OR IGNORE INTO food 
                                ({', '.join(FOOD_INFO_KEYS)}) 
                                VALUES ({', '.join(row)})""")
                except sqlite3.Error as e:
                    print(f"{str(e)}")
    except IOError:
        print(f"{csv_file_path} not found. No intial data loaded.")
    conn.commit()
    conn.close()



# Connection management
def create_connection(db_file: str):
    """Create a database connection to a SQLite database"""
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
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
        pass
    finally:
        cursor.close()

#fetches all rows
def fetch_all_rows(query: str):
    rows = execute_query(query)
    return _format_rows(rows)

#add new food to db
def add_food(food_info: dict):
    values = tuple(food_info.values())
    if (tuple(food_info.keys()) != FOOD_INFO_KEYS 
            or None in values):
        return

    insert_query = f"""
    INSERT INTO food ({', '.join(FOOD_INFO_KEYS)})
    VALUES ('{values[0]}', {', '.join(map(str, values[1:]))});
    """
    execute_query(insert_query)

#find food name in db
def find_food_name(food_name: str) -> dict:
    query = f"SELECT * FROM food WHERE food_name = '{food_name}'"
    rows = execute_query(query)

    if not rows:
        raise Exception("No matching data.")
    return _format_rows(rows[0])

def print_all_data():
    query = "SELECT * FROM food"
    rows = execute_query(query)
    formatted_rows = _format_rows(rows)
    for row in formatted_rows:
        print(row)

# # run this file to test
# if __name__ == "__main__":
#     # Import data from CSV to the database
#     db_file = DB_FILE
#     create_food_table(db_file)
#     csv_file = 'food_information.csv'
#     import_data_from_csv(csv_file, db_file)

#     # # Print all data in the database
#     # print_all_data()

#     # Example of finding a food name
#     try:
#         food_data = find_food_name("apple")
#         print(food_data)
#     except Exception as e:
#         print(str(e))
