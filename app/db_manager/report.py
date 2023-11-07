# report.py
from datetime import datetime
from eating_history import format_row, create_history_database
import sqlite3

# Suppose you also need the 'retrieve_all_meals' function from 'eating_history.py'
from eating_history import retrieve_all_meals

def report_daily_intake(date: datetime) -> dict:
    '''
    Reports the daily intake of meals.

    Arguments:
        date: A datetime object representing the date to report the meals for.

    Returns:
        A dictionary containing:
        - the date
        - the total number of meals consumed
        - a list of all the foods consumed on that date
    '''
    conn = sqlite3.connect("meal_history.db")
    cursor = conn.cursor()
    query = f'''SELECT * FROM meals 
                WHERE date(date) = date("{date.strftime("%Y-%m-%d")}")'''
    cursor.execute(query)
    meals = cursor.fetchall()
    conn.close()

    if not meals:
        return {
            "date": date.strftime("%Y-%m-%d"),
            "total_meals": 0,
            "foods": []
        }
    
    total_meals = len(meals)
    foods_consumed = []
    for meal in meals:
        meal_data = format_row(meal)
        foods_consumed.extend(meal_data['foods'])
    
    return {
        "date": date.strftime("%Y-%m-%d"),
        "total_meals": total_meals,
        "foods": foods_consumed
    }

if __name__ == "__main__":
    # Ensure the database and table are created first
    create_history_database()

    # Example of how to run the report_daily_intake function
    try:
        today = datetime.now()
        daily_report = report_daily_intake(today)
        print(daily_report)
    except Exception as e:
        print(f"An error occurred: {e}")
