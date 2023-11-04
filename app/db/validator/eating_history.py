"""
eating_history.py
"""

from datetime import date
from datetime import timedelta
from db.manager.eating_history import find_meal_date, MEAL_TYPES

__author__ = "Pokpong"

def _date_range(date_bounds: tuple[date, date], step: int):
    # Creates a generator for interating dates intervals by a specified number 
    # of days a time.
    for i in range(0, (date_bounds[1] - date_bounds[0]).days, step):
        yield date_bounds[0] + timedelta(days=i)

def date_in_db(date: date):
    """
    Checks if the date has complete info or not. No data counts as incompelete.

    Arguments:
        date: 
            date to check
    
    Returns:
        True:   date exists
        False:  date doesn't exist
    """
    meals = []
    try:
        meals = find_meal_date(date)
    except Exception as ex:
        if str(ex) == "No matching data.":
            return False
        else:
            print(str(ex))
    
    if len(meals) == len(MEAL_TYPES):
        return True
    return False

def date_range_in_db(date_bounds: tuple[date, date]):
    """
    Finds the dates within the bounds that have complete info.

    The lower bound is included and upper bound is excluded. 
    Like the range class.

    Arguments:
        date_bounds: 
            date range to check
    
    Returns:
        list of dates with compelete info
    """
    return [date for date in _date_range(date_bounds, 1) if date_in_db(date)]

def meal_in_db(date: date, meal_type: str):
    """
    Checks if a meal exist or not.

    Arguments:
        date:
            date of the meal
        meal_type: 
            type/time of the meal
    
    Returns:
        True:   meal exists
        False:  meal doesn't exist
    """
    meals = []
    try:
        meals = find_meal_date(date)
    except Exception as ex:
        if str(ex) == "No matching data.":
            return False
        else:
            print(str(ex))
    
    if meal_type in [meal["meal_type"] for meal in meals]:
        return True
    return False