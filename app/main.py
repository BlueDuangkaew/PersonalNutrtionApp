'''
main.py

This module contains functions for the user interface.
'''

import db.manager.eating_history as hist_db
import db.manager.food as food_db
from db.validator.eating_history import (meal_in_db, 
                                             date_in_db, 
                                             date_range_in_db)
from db.validator.food import food_in_db
from report.daily import generate_daily_report
from report.goal import generate_report_by_goal
import ui

__author__ = "Pokpong"

# Define the main function
def main():
    food_db.create_food_table()
    hist_db.create_history_database()
    food_db.fill_food_table()

    # Create an infinite loop for the main menu
    while True:
        opt = ui.main_menu()
        match opt:
            case 0:
                add_meal()
            case 1:
                make_daily_report()
            case 2:
                make_target_report()
            case 3:
                break

#function to allow users to add meal
def add_meal():
    meal_input = ui.MealtimeInput(hist_db.MEAL_TYPES)
    date, meal_type = meal_input.enter()
    if meal_in_db(date, meal_type) and not meal_input.overwrite():
        return
    foodinput = ui.FoodInput(food_db.FOOD_INFO_KEYS)
    for food in foodinput.getter():
        if not food_in_db(food):
            food_db.add_food(foodinput.new_type())
    if not foodinput.foods:
        return
    hist_db.add_meal_to_database(date, meal_type, foodinput.foods)

#function to allow users to enter date for daily report    
def make_daily_report():
    date = ui.DateInput.enter_one()
    if not date_in_db(date):
        ui.DateInput.no_info()
        return
    ui.print_daily_report(generate_daily_report(date))

#function to allow user to enter date range for target report   
def make_target_report():
    date_range = ui.DateInput().enter_range()
    valid_dates = date_range_in_db(date_range)
    if not valid_dates:
        ui.DateInput.range_no_info()
        return
    nutrition_type, max_val = ui.ask_nutrition_type(food_db.FOOD_INFO_KEYS[1:])
    report_info = generate_report_by_goal(valid_dates, nutrition_type, max_val)
    ui.print_target_report(report_info)

if __name__ == '__main__':
    main()