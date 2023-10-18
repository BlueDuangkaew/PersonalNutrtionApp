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

# Function to create the SQLite database and table
def create_history_database():
<<<<<<< HEAD
    conn = sqlite3.connect('meal_history.db')
=======
    attributes = ["INTEGER PRIMARY KEY AUTOINCREMENT", 
                  "DATE", 
                  "INTEGER", 
                  "TEXT"]
    column_info = (", ").join(
        [" ".join(tup) for tup in zip(COLUMNS, attributes)]
    )

    conn = sqlite3.connect("meal_history.db")
>>>>>>> e2aefcc (more code beautifying)
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
def add_meal_to_database(date, meal_type, foods):
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
    cursor.execute('INSERT INTO meals (date, meal_type, foods) VALUES (?, ?, ?)',
                   (date.strftime('%Y-%m-%d'), meal_type, ', '.join(foods)))
    print("meal added.")
    conn.commit()
    conn.close()

# Function to retrieve all meals from the database
def retrieve_all_meals():
    '''
    Adds a meal to the history database
    
    Returns:
    '''
    conn = sqlite3.connect('meal_history.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM meals')
    meals = cursor.fetchall()
    conn.close()
    return meals