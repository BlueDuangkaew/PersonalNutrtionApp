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
        row["foods"] = row["foods"].split(", ")
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
    cursor.execute(f'''INSERT INTO meals ({", ".join(_MEAL_INFO_TYPES)}) 
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
    meals = cursor.fetchall()
    conn.close()

    if not meals:
        raise Exception("No matching data.")
    return _format_rows(meals)

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
                   WHERE {_MEAL_INFO_TYPES[0]} 
                   = "{date.strftime("%Y-%m-%d")}"''')
    meals = cursor.fetchall()
    conn.close()
        
    if meal is None:
        raise Exception("No matching data.")
    return format_row(meal)



# def report_daily_intake(date: datetime) -> dict:
#     '''
#     Reports the daily intake of meals.

#     Arguments:
#         date: A datetime object representing the date to report the meals for.

#     Returns:
#         A dictionary containing:
#         - the date
#         - the total number of meals consumed
#         - a list of all the foods consumed on that date
#     '''
#     conn = sqlite3.connect("meal_history.db")
#     cursor = conn.cursor()
#     query = f'''SELECT * FROM meals 
#                 WHERE date(date) = date("{date.strftime("%Y-%m-%d")}")'''
#     cursor.execute(query)
#     meals = cursor.fetchall()
#     conn.close()

#     if not meals:
#         return {
#             "date": date.strftime("%Y-%m-%d"),
#             "total_meals": 0,
#             "foods": []
#         }
    
#     total_meals = len(meals)
#     foods_consumed = []
#     for meal in meals:
#         meal_data = format_row(meal)
#         foods_consumed.extend(meal_data['foods'])
    
#     return {
#         "date": date.strftime("%Y-%m-%d"),
#         "total_meals": total_meals,
#         "foods": foods_consumed
#     }

# if __name__ == "__main__":
#     # Ensure the database and table are created first
#     create_history_database()

#     # Example of how to run the report_daily_intake function
#     try:
#         today = datetime.now()
#         daily_report = report_daily_intake(today)
#         print(daily_report)
#     except Exception as e:
#         print(f"An error occurred: {e}")

