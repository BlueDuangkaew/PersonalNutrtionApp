'''
history_manager.py

<<Add description here>>

Functions:
    add_meal_to_database
    retrieve_all_meals
    find_meal_date
'''
import sqlite3
from datetime import datetime
from sqlite3 import Error

__author__ = "Plam, Pokpong"

DB_FILE = "meal_history.db"
_COLUMN_INFOS = {"id": "INTEGER PRIMARY KEY AUTOINCREMENT", 
                 "date": "DATE", 
                 "meal_type": "TEXT", 
                 "foods": "TEXT"}
_MEAL_INFO_TYPES = tuple(_COLUMN_INFOS.keys())[1:]
MEAL_TYPES = ("breakfast", "lunch", "dinner")

def _format_rows(rows: list[tuple]) -> list[dict]:
    # This function formats the a row of data from the database
    def format_row(row):
        row = dict(zip(_MEAL_INFO_TYPES, row[1:]))
        if row["foods"]:
            row["foods"] = row["foods"].split(", ")
        else:
            row["foods"] = []
        return row

    if isinstance(rows, tuple):
        rows = format_row(rows)
    else:
        rows = [format_row(row) for row in rows]
    return rows

# Function to create the SQLite database and table
def create_history_database():
    column_info = (", ").join(
        [" ".join(tup) for tup in _COLUMN_INFOS.items()]
    )
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        f"""CREATE TABLE IF NOT EXISTS meals (
            {column_info},
            UNIQUE ({", ".join(_MEAL_INFO_TYPES[:2])})
        )""")
    conn.commit()
    conn.close()

# Function to add a meal to the database
def upsert_meal(date: datetime, meal_type: str, foods: list):
    '''
    Adds a meal to the history database

    Arguments:
        date:
        meal_type:
        foods:
    
    Returns:
    '''
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(f'''INSERT INTO meals ({", ".join(_MEAL_INFO_TYPES)}) 
                   VALUES ("{date.strftime("%Y-%m-%d")}", 
                           "{meal_type}", 
                           "{", ".join(foods)}") 
                   ON CONFLICT({", ".join(_MEAL_INFO_TYPES[:2])})
                   DO UPDATE SET {"foods"}=excluded.{"foods"}''')
    conn.commit()
    conn.close()

# Function to retrieve all meals from the database
def retrieve_all_meals():
    '''
    Retrieves all meals from the history database
    
    Returns:
    '''
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM meals")
    meals = cursor.fetchall()
    conn.close()

    if not meals:
        raise Exception("No matching data.")
    return _format_rows(meals)

def find_meal_date(date: datetime) -> list[dict]:
    '''
    Finds a meal by date and returns a meal if found.
    
    Arguments:
        date:
            The date of the meal.

    Returns:
        A dictionary conatining the info on the meal.
    '''
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(f'''SELECT * FROM meals 
                   WHERE {_MEAL_INFO_TYPES[0]} 
                   = "{date.strftime("%Y-%m-%d")}"''')
    meals = cursor.fetchall()
    conn.close()
        
    if not meals:
        raise Exception("No matching data.")
    return _format_rows(meals)