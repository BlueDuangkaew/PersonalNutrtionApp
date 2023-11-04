'''
food_validator.py

This module contains functions for validating food entries

Functions:
    food_exists
'''

import db_manager.food as db

__author__ = "Pokpong"

def food_in_db(food_name: str) -> bool:
    """
    Checks if a given food name exists in the food database.

    Arguments:
        food_name: str
            food name to search
    
    Returns:
        True:
            if found
        False:
            if not found
    """
    try:
        find_food_name(food_name)
    except Exception as ex:
        if str(ex) == "No matching data.":
            return False
        else:
            print(str(ex))
    return True