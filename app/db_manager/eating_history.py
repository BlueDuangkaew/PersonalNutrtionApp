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

__author__ = "Plam"

# Function to create the SQLite database and table
def create_history_database():
    conn = sqlite3.connect("meal_history.db")
    cursor = conn.cursor()
    print("history init")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS meals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date DATE,
            meal_type TEXT,
            foods TEXT
        )
    ''')
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
    conn = sqlite3.connect('meal_history.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO meals (date, meal_type, foods) \
                   VALUES (?, ?, ?)',
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
