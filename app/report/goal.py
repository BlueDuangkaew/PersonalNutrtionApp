'''
goal.py

This module contains functions for reporting nutrition from the user goal set

Functions:
    generate_report_by_goal

'''

from datetime import datetime
from db.manager.eating_history import find_meal_date
from db.manager.food import find_food_name

__author__ = "Blue, Pokpong"

#generate the goal report
def generate_report_by_goal(
        dates: list[datetime], nutrition_type: str, max_value: float):
    '''
    Arguments:
        dates:
            a date range of start and end
        nutrition_type:
            calories, sodium, fats, carbohydrates
        max_value:
            the maximum amount of the nutrition type
    
    Returns:
        report_info
            A dictionary conatining "Nutrition Type, Max Value, and Difference"
    '''
    
    diff = {}
    for date in dates:
        daily_meals = find_meal_date(date)
        food_names = [food for meal in daily_meals for food in meal["foods"]]
        nutrition_sum = sum([find_food_name(food_name)[nutrition_type] 
                             for food_name in food_names])
        diff.update({date: (nutrition_sum/max_value * 100) - 100})
        
    report_info = {
        "header": {"Nutrition type": nutrition_type, "Max value": max_value}, 
        "diff": diff
    }

    return report_info
