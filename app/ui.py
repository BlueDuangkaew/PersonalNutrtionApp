from datetime import datetime, timedelta

'''
ui.py

This module contains functions for the user interface.
'''

__author__ = "Palm"

def enter_date():
    while True:
        date_str = input("Enter the date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError as msg:
            print("Invalid date format. Please use YYYY-MM-DD format.")
        else:
            if date > datetime.now():
                print("The date you entered is in the future. Please enter a valid date.")
            elif date < datetime.now() - timedelta(days=14):
                print("The date you entered is more than two weeks old.")
            else:
                return date.strftime('%Y-%m-%d')

def enter_meal_type():
    while True:
        meal_type = input("Enter meal type (breakfast/lunch/dinner/snack): ").lower()
        if meal_type in ["breakfast", "lunch", "dinner", "snack"]:
            return meal_type
        else:
            print("Invalid meal type. Please enter one of the specified meal types.")

def enter_food_items():
    foods = []
    while True:
        user_food = input("Enter a food item (or 'done' to finish): ")
        if user_food.lower() == 'done':
            break
        else:
            foods.append(user_food)
            print(f"{user_food} added.")
    return foods

def ask_date_range():
    while True:
        start_date_str = input("Enter the start date (YYYY-MM-DD): ")
        end_date_str = input("Enter the end date (YYYY-MM-DD): ")

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")
            continue

        if start_date > end_date:
            print("The start date should be before the end date.")
            continue
        return start_date, end_date

def ask_nutrition_type():
    while True:
        nutrition_type = input("Enter a nutrition type (calories, sodium, sugar): ").lower()
        if nutrition_type not in ["calories", "sodium", "sugar"]:
            print("Invalid nutrition type. Please enter calories, sodium, or sugar.")
        else:
            max_value = input(f"Enter the limit for {nutrition_type}: ")
            return nutrition_type, max_value

def report_menu():
    while True:
        print("\nReport Menu")
        print("1. Daily report")
        print("2. Goal report")
        print("3. Back to main menu")
        
        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            start_date, end_date = ask_date_range()
            print("Generating reports from a date range.")
            # Call the function to generate a daily report using start_date and end_date
        elif choice == '2':
            nutrition_type, max_value = ask_nutrition_type()
            print("Generating reports from the user's goal.")
            # Call the function to generate a goal report using nutrition_type and max_value
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    while True:
        print("\nFood and Nutrition Tracker")
        print("1. Enter a meal")
        print("2. Generate a nutrition report")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            date = enter_date()
            meal_type = enter_meal_type()
            foods = enter_food_items()
            # Process the entered meal data
        elif choice == '2':
            report_menu()
        elif choice == '3':
            print("Exit. Have a great day!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
