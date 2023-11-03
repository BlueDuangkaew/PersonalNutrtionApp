'''
history_manager.py

<<Add description here>>

Functions:
    add_meal_to_database
    retrieve_all_meals
    find_meal_date
'''
import sqlite3
from datetime import date
from sqlite3 import Error

__author__ = "Plam, Pokpong"

_COLUMNS = ("id", "date", "meal_type", "foods")
MEAL_TYPES = ("breakfast", "lunch", "dinner")

def format_row(row: tuple) -> dict:
    # This function formats the a row of data from the database
    meal = dict(zip(_COLUMNS, row))
    meal["foods"] = meal["foods"].split(", ")
    return meal

# Function to create the SQLite database and table
def create_history_database():
    attributes = ["INTEGER PRIMARY KEY AUTOINCREMENT", 
                  "DATE", 
                  "TEXT", 
                  "TEXT"]
    column_info = (", ").join(
        [" ".join(tup) for tup in zip(_COLUMNS, attributes)]
    )

    conn = sqlite3.connect("meal_history.db")
    cursor = conn.cursor()
    print("history init")
    cursor.execute(f"CREATE TABLE IF NOT EXISTS meals ({column_info})")
    conn.commit()
    conn.close()

# Function to add a meal to the database
def add_meal_to_database(date: date, meal_type: str, foods: list):
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
    cursor.execute(f'''INSERT INTO meals ({", ".join(_COLUMNS[1:4])}) 
                   VALUES ("{date.strftime("%Y-%m-%d")}", 
                           "{meal_type}", 
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
    meals = cursor.fetchall()
    conn.close()

    if not meals:
        raise Exception("No matching data.")
    return list(map(format_row, meals))

def find_meal_date(date: date) -> list:
    '''
    Finds a meal by date and returns a meal if found.
    
    Arguments:
        date:
            The date of the meal.

    Returns:
        A dictionary conatining the info on the meal.
    '''
    conn = sqlite3.connect("meal_history.db")
    cursor = conn.cursor()
    cursor.execute(f'''SELECT * FROM meals 
                   WHERE {_COLUMNS[1]} = "{date.strftime("%Y-%m-%d")}"''')
    meals = cursor.fetchall()
    conn.close()
        
    if not meals:
        raise Exception("No matching data.")
    return list(map(format_row, meals))