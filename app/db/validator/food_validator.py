'''
food_validator.py

This module contains functions for validating food entries

Functions:
    food_exists
'''

import db_manager.food as db

__author__ = "Pokpong"

def check_food_exists(food_name: str) -> bool:
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
        db.find_food_name(food_name)
    except Exception:
        return False
    return True