def find_food_name(food_name: str) -> dict:
    if(food_name == "hi"):
        raise Exception("Food not found")
    return {"food": food_name}