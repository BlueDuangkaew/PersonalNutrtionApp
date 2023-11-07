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
import ui as ui

__author__ = "Pokpong"

# Define the main function
def main():
    food_db.create_food_table()
    hist_db.create_history_database()
    food_db.fill_food_table()
    
    # food_db.fetch_all_rows("SELECT * FROM food")
    # print(hist_db.retrieve_all_meals())

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

def add_meal():
    date, meal_type = ui.MealtimeInput(hist_db.MEAL_TYPES).get()
    if meal_in_db(date, meal_type) and not ui.MealtimeInput.overwrite():
        return
    foodinput = ui.FoodInput(food_db.FOOD_INFO_KEYS)
    for food in foodinput.getter():
        if not food_in_db(food):
            food_db.add_food(foodinput.new_type())
    if not foodinput.foods:
        return
    hist_db.add_meal_to_database(date, meal_type, foodinput.foods)
    
def make_daily_report():
    date_range = ui.DateRangeInput.get()
    if date_range_in_db(date_range):
        # generate_daily_report(date_range[0], date_range[1])
        print("\n\nDummy report!!!\n")
    
def make_target_report():
    date_range = ui.DateRangeInput.get()
    if not date_range_in_db(date_range):
        return
    nutrition_type, max_val = ui.ask_nutrition_type(food_db.FOOD_INFO_KEYS)
    # generate_report_by_goal(nutrition_type, max_val)
    print("\n\nDummy report!!!\n")


if __name__ == '__main__':
    main()