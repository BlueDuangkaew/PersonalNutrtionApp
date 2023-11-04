'''
nutrition_report_byDate.py

This module contains functions for reporting nutrition from a date range
'''
import sqlite3

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

        # Retrieve today meals from the eating_history.py
        today_meal = find_meal_date(today)
        today_breakfast = find_meal_date(today)

        # Retrieve food details using food names
        food_details = [find_food_name(food_name) for food_name in today_meal['foods']]

        # Calculate total calories for each meal
        total_calories = sum(food['calories'] for food in food_details)

        # Print the report
        print(f"Daily Report for {date.strftime('%Y-%m-%d')}")
        print(f"Breakfast: {food_details['foods']}")

        print(f"Breakfast:")
        for food in food_details:
            if food['meal_type'] == "Breakfast"
            print(f"- {food['name']}: {food['calories']} calories")
        
        print(f"Today Total Calories: {total_calories} calories")

    except Exception as e:
        print(f"Error: {e}")
