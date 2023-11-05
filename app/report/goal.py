'''
nutrition_report_byGoal.py

This module contains functions for reporting nutrition from the user goal set
'''
from db.manager.eating_history import find_eating_history_by_date
from db.manager.food import retrieve_food_by_name

__author__ = "Blue"

def generate_target_report():
    '''
    Generates a target report for a specific nutrition type and date range.

    Arguments:
        nutrition_type:
            The type of nutrition to report on.
        target_amount:
            The target amount of the specified nutrition type.
        start_date:
            The start date for the report period.
        end_date:
            The end date for the report period.
    
    Returns:
        None
    '''
    try:
        # Ask the user which nutrition type they want to see
        nutrition_type = input("Which nutrition type would you like to see?\n"
                               "1. Calories\n"
                               "2. Sodium (mg)\n"
                               "3. Carbohydrates (g)\n"
                               "4. Fats (g)\n")

        # Ask the user for the amount of nutrition target
        target_amount = float(input("Please enter the target amount: "))

        # Ask the user for the date range
        start_date = input("Enter the start date (YYYY-MM-DD): ")
        end_date = input("Enter the end date (YYYY-MM-DD): ")

        # Retrieve meals from the eating history database
        meals = find_eating_history_by_date(start_date, end_date)

        # Retrieve food details using food names and calculate total nutrition intake
        total_nutrition = 0
        for meal in meals:
            food_list = [retrieve_food_by_name(food_name) for food_name in meal['foods']]
            if nutrition_type == '1':
                total_nutrition += sum(food['calories'] for food in food_list)
            elif nutrition_type == '2':
                total_nutrition += sum(food['sodium'] for food in food_list)
            elif nutrition_type == '3':
                total_nutrition += sum(food['carbohydrates'] for food in food_list)
            elif nutrition_type == '4':
                total_nutrition += sum(food['fats'] for food in food_list)

        # Print the report
        print(f"Target Report for {start_date} to {end_date}")
        if nutrition_type == '1':
            print(f"Total Calories: {total_nutrition} calories")
        elif nutrition_type == '2':
            print(f"Total Sodium: {total_nutrition} mg")
        elif nutrition_type == '3':
            print(f"Total Carbohydrates: {total_nutrition} grams")
        elif nutrition_type == '4':
            print(f"Total Fats: {total_nutrition} grams")

    except Exception as e:
        print(f"Error: {e}")

# Call the generate_target_report function
generate_target_report()