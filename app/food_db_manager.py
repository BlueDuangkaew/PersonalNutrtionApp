'''
food_db_manager.py

This is merely a mock-up of the food database manager.

Functions:
    find_food_name
'''

def find_food_name(food_name: str) -> dict:
    '''
    Mock-up of finding foods by name functionality

    Arguments:
        food_name:
            String of the food name

    Returns:
        A dictionary with the food name its nutrition values.

    Expections:
        Food not found:
    '''
    if(food_name == "hi"):
        raise Exception("Food not found")
    return {"food": food_name, "calories": 0, "sodium": 0}