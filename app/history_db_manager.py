'''
history_manager.py

<<Add description here>>

Functions:
    add_meal_to_database
    retrieve_all_meals
'''
import sqlite3
from datetime import datetime
from sqlite3 import Error

COLUMNS = ("id", "date", "meal_type", "foods")

def row_to_dict(row: tuple) -> dict:
    meal = dict(zip(COLUMNS, row))
    meal["foods"] = meal["foods"].split(", ")
    return meal

# Function to create the SQLite database and table
def create_history_database():
    attributes = ["INTEGER PRIMARY KEY AUTOINCREMENT", "DATE", "TEXT", "TEXT"]
    column_info = (", ").join([" ".join(tup) for tup in zip(COLUMNS, attributes)])

    conn = sqlite3.connect('meal_history.db')
    cursor = conn.cursor()
    print("history init")
    cursor.execute(f"CREATE TABLE IF NOT EXISTS meals ({column_info})")
    conn.commit()
    conn.close()

# Function to add a meal to the database
def add_meal_to_database(date: datetime, meal_type, foods: list):
    '''
    Adds a meal to the history database

    Arguments:
        date:
        meal_type:
        foods:
    
    Returns:
    '''
    conn = sqlite3.connect('meal_history.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO meals ({', '.join(COLUMNS[1:4])}) VALUES (?, ?, ?)",
                   (date.strftime('%Y-%m-%d'), meal_type, ', '.join(foods)))
    print("meal added.")
    conn.commit()
    conn.close()

# Function to retrieve all meals from the database
def retrieve_all_meals():
    '''
    Retrieves all meals from the history database
    
    Returns:
    '''
    conn = sqlite3.connect('meal_history.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM meals')
    meals = cursor.fetchall()
    conn.close()
    return meals

def find_meal_date(date: datetime, meal_time: str) -> list:
    '''
    Finds and returns a meal if found.
    
    Returns:
    '''
    conn = sqlite3.connect('meal_history.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM meals WHERE {COLUMNS[1]}='{date.strftime('%Y-%m-%d')}' AND {COLUMNS[2]}='{meal_time}'")
    meals = cursor.fetchall()
    conn.close()
    meals = list(map(row_to_dict, meals))
    return meals