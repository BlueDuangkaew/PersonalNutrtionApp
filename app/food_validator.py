import food_db_manager

def food_exists(food_name: str) -> bool:
    try:
        food_db_manager.find_food_name(food_name)
    except:
        return False
    return True

print(food_exists("apple"), food_exists("hi"))