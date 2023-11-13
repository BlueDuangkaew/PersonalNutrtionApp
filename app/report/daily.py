'''
daily.py

This module contains functions for reporting nutrition from a date range

Functions:
    create_food_details
    daily_summary
    generate_daily_report
'''

from datetime import datetime
from db.manager.eating_history import (find_meal_date, 
                                       MEAL_TYPES)
from db.manager.food import (find_food_name, 
                             FOOD_INFO_KEYS, 
                             NUTRITION_UNITS)

__author__ = "Blue, Pokpong"

#function to create food details like nutriation etc
def create_food_details(food_list: list):
    #initialize
    meal_summary = {'foods': food_list}
    nutrition_summary = {f"Total {nutrition}": 0 
                         for nutrition in FOOD_INFO_KEYS[1:]}

    for food_item in food_list:
        food_details = find_food_name(food_item)
        for nutrition in FOOD_INFO_KEYS[1:]:
            nutrition_summary[f"Total {nutrition}"] += food_details[nutrition]
            
    meal_summary.update(nutrition_summary)
    return meal_summary

#summarize the daily nutriation
def daily_summary(all_meals: dict[str, dict]):
    #Add the sumary to the dict 
    today_summary = {}
    nutrition_names = list(list(all_meals.values())[0].keys())[1:]
    for name, unit in zip(nutrition_names, NUTRITION_UNITS):
        today_summary.update(
            {name: f"{sum([meal[name] for meal in all_meals.values()])} {unit}"})
    return today_summary

#function to generate the report
def generate_daily_report(date: datetime):
    #initialize dict
    all_meal = {}

    meal_data = find_meal_date(date)

    #catagorize
    for meal_item, meal_type in zip(meal_data, MEAL_TYPES):
        all_meal.update({meal_type: create_food_details(meal_item["foods"])})
    return date, daily_summary(all_meal)
