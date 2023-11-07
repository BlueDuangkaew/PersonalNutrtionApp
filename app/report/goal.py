'''
nutrition_report_byGoal.py

This module contains functions for reporting nutrition from the user goal set
'''

import sqlite3

__author__ = "Blue"

def generate_target_report():
    #Connect to the database
    conn = sqlite3.connect("personal_nutrition_app.db")
    cursor = conn.cursor()

    #Ask the user for the details
    nutrition_type = input("Enter the nutrition type (Calories, Sodium, Fats, Carbohydrates, Protein): ")
    target_amount = float(input(f"Enter the target amount of {nutrition_type}: "))
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    cursor.execute(f'SELECT SUM({nutrition_type}) FROM meal_history '
              'INNER JOIN food_nutrition ON meal_history.foods = food_nutrition.food_name '
              'WHERE date BETWEEN ? AND ?', (start_date, end_date))
    total_intake = cursor.fetchone()[0]

    if total_intake:
        print(f"Total {nutrition_type} intake between {start_date} and {end_date}: {total_intake}")
        print(f"Target amount: {target_amount}")
        if total_intake >= target_amount:
            print(f"You have exceeded your target by {total_intake - target_amount}")
        else:
            print(f"You need {target_amount - total_intake} more {nutrition_type}")
    else:
        print(f"No data for the selected date range")

if __name__ == "__main__":
    generate_target_report()
