'''
nutrition_report_byDate.py

This module contains functions for reporting nutrition from a date range
'''

import sqlite3
import datetime
import plotly.graph_objects as go

__author__ = "Blue"

def generate_daily_report():
    # Connect to the eating_history database
    conn = sqlite3.connect("personal_nutrition_app.db")
    c = conn.cursor()

    #Error Here
    today = datetime.now().date()

    c.execute('SELECT * FROM meal_history WHERE date=?', (today,))
    data = c.fetchall()

    if data:
        print(f"Date: {today}")
        print("Eaten foods:")
        for row in data:
            print(row[2], row[3])

        c.execute('SELECT SUM(calories), SUM(sodium), SUM(protein), SUM(carbohydrate), SUM(fat) FROM meal_history '
                  'INNER JOIN food_nutrition ON meal_history.food_name = food_nutrition.foods WHERE date=?', (today,))
        totals = c.fetchone()

        print(f"\nTotal Nutrition Intake:")
        print(f"Calories: {totals[0]}")
        print(f"Sodium: {totals[1]}")
        print(f"Fats: {totals[2]}")
        print(f"Carbohydrates: {totals[3]}")
        print(f"Protein: {totals[4]}")

        # Generate chart
        labels = ['Calories', 'Sodium', 'Fats', 'Carbohydrates', 'Protein']
        values = [totals[0], totals[1], totals[2], totals[3], totals[4]]

        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        fig.show()
    else:
        print(f"No data for {today}")