'''
nutrition_report_byDate.py

This module contains functions for reporting nutrition from a date range
'''

from eating_history import find_meal_date
from food import find_food_name
import datetime
import plotly.graph_objects as go

__author__ = "Blue"

def generate_daily_report():

    try:
        # Get today's date
        today = datetime.date.today()

        # Retrieve today's meals from the eating_history.py
        today_meal = find_meal_date(today)

        # Initialize dictionaries to store food details for each meal type
        breakfast_details = {}
        lunch_details = {}
        dinner_details = {}

        # Calculate total calories for each meal
        total_calories = 0

        # Iterate through the foods in today's meals and retrieve their details
        for food_name in today_meal[0]['foods']:
            food_info = find_food_name(food_name)
            total_calories += food_info[0]['calories']

            if today_meal[0]['meal_type'] == "Breakfast":
                if food_name not in breakfast_details:
                    breakfast_details[food_name] = food_info[0]['calories']
                else:
                    breakfast_details[food_name] += food_info[0]['calories']
            elif today_meal[0]['meal_type'] == "Lunch":
                if food_name not in lunch_details:
                    lunch_details[food_name] = food_info[0]['calories']
                else:
                    lunch_details[food_name] += food_info[0]['calories']
            elif today_meal[0]['meal_type'] == "Dinner":
                if food_name not in dinner_details:
                    dinner_details[food_name] = food_info[0]['calories']
                else:
                    dinner_details[food_name] += food_info[0]['calories']

        # Print the report
        print(f"Daily Report for {today.strftime('%Y-%m-%d')}")
        print("Breakfast:")
        for food, calories in breakfast_details.items():
            print(f"- {food}: {calories} calories")

        print("Lunch:")
        for food, calories in lunch_details.items():
            print(f"- {food}: {calories} calories")

        print("Dinner:")
        for food, calories in dinner_details.items():
            print(f"- {food}: {calories} calories")

        print(f"Today's Total Calories: {total_calories} calories")

        # Create a pie chart to visualize meal type distribution
        labels = ['Breakfast', 'Lunch', 'Dinner']
        values = [sum(breakfast_details.values()), sum(lunch_details.values()), sum(dinner_details.values())]

        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        fig.update_layout(title='Calorie Distribution by Meal Type')
        fig.show()

    except Exception as e:
        print(f"Error: {e}")

# Call the generate_daily_report function
generate_daily_report()
