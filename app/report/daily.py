'''
nutrition_report_byDate.py

This module contains functions for reporting nutrition from a date range
'''
from datetime import datetime
from db.manager.eating_history import find_meal_date, MEAL_TYPES
from db.manager.food import find_food_name, FOOD_INFO_KEYS

__author__ = "Blue"

def create_food_details(food_list: list):
    #initialize
    meal_summary = {'foods': food_list}
    meal_summary.update({f"Total {nutrition_type}": 0 for nutrition_type in FOOD_INFO_KEYS[1:]})

    for food_item in food_list:
        food_details = find_food_name(food_item)
        for nutrition_type in FOOD_INFO_KEYS[1:]:
            meal_summary[f"Total {nutrition_type}"] += food_details[nutrition_type]
            
    return meal_summary

def daily_summary(all_meals: dict[str, dict]):
    #Add the sumary to the dict 
    today_summary = {}
    types = list(list(all_meals.values())[0].keys())[1:]
    print(types)
    for nutrition_type in types:
        today_summary.update({nutrition_type: sum([meal[nutrition_type] for meal in all_meals.values()])})
    
    return today_summary

def generate_daily_report(date: datetime):
    #initialize dict
    all_meal = {}

    meal_data = find_meal_date(date)

    for meal_item in meal_data:

        #catagorize
        for meal_type in MEAL_TYPES:
            all_meal.update({meal_type: create_food_details(meal_item["foods"])})

    report_summary = daily_summary(all_meal)

    print(f"\nToday Summary:")
    for key, total in report_summary.items():
        print(f"{key}: {total}")

# def _sum_daily_intake(daily_food_info: list[dict[str, float]]) -> list[float]:
#     sum_elem_wise = (lambda lists : 
#         [map(sum, [ls[i] for ls in lists]) for i in range(len(lists[0]))])
#     nutrition_vals = (list(food_info.values())[1:] for food_info in daily_food_info)
#     return sum_elem_wise(nutrition_vals)

# def generate_daily_report(date: datetime):
#     '''
#     <<function brief description>>

#     Arguments:
#         nutrition_type:
#             <<brief description>> 
#         max_value:
#             <<brief description>> 
    
#     Returns:
#         <<brief description>> 
#     '''
#     sum_elem_wise = (lambda lists : 
#         [map(sum, [ls[i] for ls in lists]) for i in range(len(lists[0]))])

#     # Retrieve today meals from the eating_history.py
#     meals = find_meal_date(date)
#     # Retrieve food details using food names
#     foods = (meal['foods'] for meal in meals)
#     print(type(foods), foods)
#     nutrition_vals = [list(find_food_name(food).values())[1:] for food in foods]
#     sum_food_details = _sum_daily_intake(nutrition_vals)
#     return sum_food_details
