'''
nutrition_report_byDate.py

This module contains functions for reporting nutrition from a date range
'''

from db_manager.eating_history import *
from db_manager import food
import datetime
import plotly.graph_objects as go

__author__ = "Blue"

def generate_daily_report():
    '''
    <<function brief description>>

    Arguments:
        nutrition_type:
            <<brief description>> 
        max_value:
            <<brief description>> 
    
    Returns:
        <<brief description>> 
    '''

    try:

        # Get today's date
        today = datetime.today().strftime('%Y-%m-%d')

        # Retrieve meals from the eating history database
        breakfast_meal = find_meal_date(today, meal_type=0)  # Assuming 0 represents breakfast
        lunch_meal = find_meal_date(today, meal_type=1)  # Assuming 1 represents lunch
        dinner_meal = find_meal_date(today, meal_type=2)  # Assuming 2 represents dinner

        # Retrieve food details using food names
        breakfast_food = [retrieve_food_by_name(food_name) for food_name in breakfast_meal['foods']]
        lunch_food = [retrieve_food_by_name(food_name) for food_name in lunch_meal['foods']]
        dinner_food = [retrieve_food_by_name(food_name) for food_name in dinner_meal['foods']]

        # Print the report
        print(f"Daily Report for {date.strftime('%Y-%m-%d')}")
        print(f"Breakfast: {breakfast['foods']}")
        print(f"Lunch: {lunch['foods']}")
        print(f"Dinner: {dinner['foods']}")

    except Exception as e:
        print(f"Error: {e}")


""""
def generate_dialy_report(today_date):
    '''
    <<function brief description>>

    Arguments:
        nutrition_type:
            <<brief description>> 
        max_value:
            <<brief description>> 
    
    Returns:
        <<brief description>> 
    '''
    eating_history_conn = sqlite3.connect('eating_history.db')
    eating_history_cursor = eating_history_conn.cursor()
    eating_history_cursor.execute('''
        SELECT date, food.name, servings
        FROM eating_history
        INNER JOIN food ON eating_history.food_id = food.food_id
        WHERE date ?
    ''', (today_date))
    report = eating_history_cursor.fetchall()
    eating_history_conn.close()
    return report
"""