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

_COLUMNS = ("id", "date", "meal_type", "foods")
MEAL_TYPES = ("breakfast", "lunch", "dinner")

def format_row(row: tuple) -> dict:
    # This function formats the a row of data from the database
    meal = dict(zip(COLUMNS, row))
    meal["foods"] = meal["foods"].split(", ")
    return meal

# Function to create the SQLite database and table
def create_history_database():
    attributes = ["INTEGER PRIMARY KEY AUTOINCREMENT", 
                  "DATE", 
                  "INTEGER", 
                  "TEXT"]
    column_info = (", ").join(
        [" ".join(tup) for tup in zip(COLUMNS, attributes)]
    )

    conn = sqlite3.connect("meal_history.db")
    cursor = conn.cursor()
    print("history init")
    cursor.execute(f"CREATE TABLE IF NOT EXISTS meals ({column_info})")
    conn.commit()
    conn.close()

# Function to add a meal to the database
def add_meal_to_database(date: datetime, meal_type: int, foods: list):
    '''
    Adds a meal to the history database

    Arguments:
        date:
        meal_type:
        foods:
    
    Returns:
    '''
    conn = sqlite3.connect("meal_history.db")
    cursor = conn.cursor()
    cursor.execute(f'''INSERT INTO meals ({", ".join(COLUMNS[1:4])}) 
                   VALUES ("{date.strftime("%Y-%m-%d")}", 
                           {meal_type}, 
                           "{", ".join(foods)}")''')
    print("meal added.")
    conn.commit()
    conn.close()

# Function to retrieve all meals from the database
def retrieve_all_meals():
    '''
    Retrieves all meals from the history database
    
    Returns:
    '''
    conn = sqlite3.connect("meal_history.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM meals")
    meals = list(map(format_row, cursor.fetchall()))
    conn.close()
    return meals

def find_meal_date(date: datetime, meal_type: int) -> dict:
    '''
    Finds a meal by date and meal time and returns a meal if found.
    
    Arguments:
        date:
            The date of the meal.
        meal_type:
            The meal time/type.

    Returns:
        A dictionary conatining the info on the meal.
    '''
    conn = sqlite3.connect("meal_history.db")
    cursor = conn.cursor()
    cursor.execute(f'''SELECT * FROM meals 
                   WHERE {COLUMNS[1]} = "{date.strftime("%Y-%m-%d")}" 
                   AND {COLUMNS[2]} = {meal_type}''')
    meal = cursor.fetchone()
    conn.close()
    if meal is None:
        raise Exception("No matching data.")
    return format_row(meal)