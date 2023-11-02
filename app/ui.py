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
                return date.strftime('%Y-%m-%d'), date < datetime.now()
    return date_str
    
def enter_meal_type():
    while True:
        meal_type = input("Enter meal type (breakfast/lunch/dinner/snack): ").lower()  # Convert to lowercase for case-insensitivity
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
    return start_date, end_date

def ask_nutrition_type():
    while True:
    # Ask the user to input a nutrition type (calories, sodium, or sugar)
        nutrition_type = input("Enter a nutrition type (calories, sodium, sugar): ").lower()

    # Check if the input is valid
        if nutrition_type not in ["calories", "sodium", "sugar"]:
            print("Invalid nutrition type. Please enter calories, sodium, or sugar.")
            return

    # Ask the user to input the limit for the chosen nutrition type
        max_value = input(f"Enter the limit for {nutrition_type}: ")
    return nutrition_type, max_value

def report_menu():

    while True:
        print("\nReport Menu")
        print("1. Daily report")
        print("2. Goal report")
        print("3. Back to main menu")

        # Prompt the user to select an option
        choice = input("Select an option (1/2/3): ")

        # Check the user's choice and take appropriate actions
        if choice == '1':
            ask_date_range()
            generate_report_by_date(start_date, end_date) 
            print("Generating reports from a date range.")
            #create function to asl for date range and check if the database is empty
            #ask for date range
            #is the database empty?
            # Call the function to generate a daily report
        elif choice == '2':
            #create function to ask for nutrition type and check if the database is empty?
            #is the database empty?
            #ask for nutrition type
            ask_nutrition_type()
            generate_report_by_goal()
            print("Generating reports from the user's goal.")
              # Call the function to generate a goal report
        elif choice == '3':
            break  # Return to the main menu
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    while True:
        print("\nFood and Nutrition Tracker")
        print("1. Enter a meal")
        print("2. Generate a nutrition report")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ")

        # Check the user's choice and take appropriate actions
        if choice == '1':

            enter_date()
            #create input meal type function and check for validity
            enter_meal_type()
            #create function to ask for food input
            enter_food_items()
        elif choice == '2':
            report_menu()  # Call the function to display the report menu
        elif choice == '3':
            print("Exit. Have a great day!")
            break  # Exit the program
        else:
            print("Invalid choice. Please select 1, 2, or 3.")