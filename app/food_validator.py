'''
food_validator.py

This module contains functions for validating food entries

Functions:
    food_in_dbs
'''

from db.manager.food import find_food_name

__author__ = "Pokpong"

<<<<<<< Updated upstream:app/food_validator.py
def check_food_exists(food_name: str) -> bool:
=======
def food_in_db(food_name: str, connection) -> bool:
>>>>>>> Stashed changes:app/db/validator/food.py
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
<<<<<<< Updated upstream:app/food_validator.py
        db.find_food_name(food_name)
    except:
        return False
=======
        find_food_name(connection, food_name)
    except Exception as ex:
        if str(ex) == "No matching data.":
            return False
        else:
            print(str(ex))
>>>>>>> Stashed changes:app/db/validator/food.py
    return True