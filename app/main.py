"""
main.py

This module contains functions for the user interface.
"""

import sys
import os
import db.manager.eating_history as hist_db
import db.manager.food as food_db
from db.validator.eating_history import (
    meal_in_db,
    date_in_db,
    date_range_in_db
)
from db.validator.food import food_in_db
from report.daily import generate_daily_report
from report.goal import generate_report_by_goal
import ui

__author__ = "Pokpong"

def main():
    """
    The main function of the module.

    This function initializes the necessary database tables, fills in initial data,
    and enters an infinite loop for the main menu.

    Options:
    0 - Add Meal
    1 - Generate Daily Report
    2 - Generate Target Report
    3 - Exit
    """
    food_db.create_food_table()
    hist_db.create_history_database()
    food_db.fill_in_table("food_information.csv")

    while True:
        opt = ui.main_menu()
        if opt == 0:
            add_meal()
        elif opt == 1:
            make_daily_report()
        elif opt == 2:
            make_target_report()
        elif opt == 3:
            break

def add_meal():
    """
    Function to allow users to add a meal.

    Users can input the date, meal type, and food items for a meal.
    """
    meal_input = ui.MealInput(
        hist_db.MEAL_TYPES,
        food_db.FOOD_INFO_KEYS[0],
        food_db.FOOD_INFO_KEYS[1:],
        food_db.NUTRITION_UNITS
    )
    date, meal_type = meal_input.enter_time()

    if meal_in_db(date, meal_type) and not meal_input.overwrite():
        return
    try:
        for food in meal_input.enter_food():
            if not food_in_db(food):
                food_db.add_food(meal_input.new_food_type())
    except Exception as ex:
        if str(ex) != "cancelled":
            print(str(ex))
    else:
        hist_db.upsert_meal(date, meal_type, meal_input.foods)

def make_daily_report():
    """
    Function to allow users to generate a daily report.

    Users can input the date for which they want to generate the report.
    """
    date = ui.DateInput.enter_one()
    if not date_in_db(date):
        ui.DateInput.no_info()
        return
    ui.print_daily_report(generate_daily_report(date))

def make_target_report():
    """
    Function to allow users to generate a target report.

    Users can input a date range and choose a nutrition type and maximum value for the report.
    """
    date_range = ui.DateInput().enter_range()
    valid_dates = date_range_in_db(date_range)
    if not valid_dates:
        ui.DateInput.range_no_info()
        return
    nutrition_type, max_val = ui.ask_nutrition_type(food_db.FOOD_INFO_KEYS[1:])
    report_info = generate_report_by_goal(valid_dates, nutrition_type, max_val)
    ui.print_target_report(report_info)

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram interrupted. Exiting...")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
