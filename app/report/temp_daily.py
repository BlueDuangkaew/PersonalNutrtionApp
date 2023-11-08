'''
nutrition_report_byDate.py

This module contains functions for reporting nutrition from a date range
'''

from eating_history import find_meal_date
from food import find_food_name
from datetime import date
import plotly.graph_objects as go

__author__ = "Blue"

def create_food_details(meal_type: str, food_list: list):
    #initialize
    total_cal = 0
    total_sodium = 0
    total_carb = 0
    total_fat = 0

    for food_item in food_list:

        food_details = find_food_name(food_item)
        
        total_cal += food_details['calories']
        total_sodium += food_details['sodium']
        total_carb += food_details['carbohydrate']
        total_fat += food_details['fat']

    meal_summary = {
        'meal_type': meal_type, 
        'foods': food_list, 
        'total_cal': total_cal,
        'total_sodium': total_sodium,
        'total_carb': total_carb,
        'total_fat': total_fat,
    }
    return meal_summary


"""def create_food_details(meal_type: str, food_list: list):
    for food_item in food_list:

        #Get details from find_food_name function
        food_details = find_food_name(food_item)

        #Sum
        total_cal =+ food_details('calories')
        total_sodium =+ food_details('sodium')
        total_protein =+ food_details('protein')
        total_carb =+ food_details('carbohydrate')
        total_fat =+ food_details('fat')

    #Add the sumary to the dict
    meal_summary = {
        'meal_type': meal_type, 
        'foods': food_list, 
        'total_cal': total_cal,
        'total_sodium': total_sodium,
        'total_protein': total_protein,
        'total_carb': total_carb,
        'total_fat': total_fat,
    }
    return meal_summary"""

def daily_summary():
    pass

def generate_daily_report(date: date):

    #Get the data from find meal date function
    #Collecting to meals_history
    
    '''
    meals = {
        date
        meal_type
        food_list
    }

    nutrition_details = {
        food_name, 
        calories, 
        sodium, 
        protien, 
        carbohydrate, 
        fat
    }
    '''

    meal_data = find_meal_date(date)

    # print(meal_data["foods"])
    '''
    _COLUMNS = ("id", "date", "meal_type", "foods")
    MEAL_TYPES = ("Breakfast", "Lunch", "Dinner")
    '''

    for meal_item in meal_data:
        #Summary all the nutrition intakes for that day
        #Display: Selected Date, Total Nutrition Intakes

        #food_tmp ==> list
        food_tmp = meal_item["foods"]

        for food_item in food_tmp:

            #nutrition_details ==> Dict
            nutrition_details = find_food_name(food_item)
            '''
            "food_name"
            "calories"
            "fat"
            "carbs"
            "sodium"
            '''


            #sum all the nutrition details
            today_cal =+ nutrition_details["calories"]
            today_sodium =+ nutrition_details["sodium"]
            today_carb =+ nutrition_details["carbs"]
            today_fat =+ nutrition_details["fat"]

        #Categorize and collect data by meal_type
        if meal_item["meal_type"] == "Breakfast":
            breakfast_meal = create_food_details(meal_item["meal_type"], meal_item["foods"])
            print(breakfast_meal)

    #Add the sumary to the dict 
    today_summary = {
        'total_cal': today_cal,
        'total_sodium': today_sodium,
        'total_carb': today_carb,
        'total_fat': today_fat
    }

    #Generate 
    

    print(today_summary)


'''    print(f"\nTotal Nutrition Intake:")
    print(f"Calories: {totals[0]}")
    print(f"Sodium: {totals[1]}")
    print(f"Fats: {totals[2]}")
    print(f"Carbohydrates: {totals[3]}")
    print(f"Protein: {totals[4]}")

    # Generate chart
    labels = ['Calories', 'Sodium', 'Fats', 'Carbohydrates', 'Protein']
    values = [totals[0], totals[1], totals[2], totals[3], totals[4]]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.show()'''

if __name__ == '__main__':
    from datetime import date
    # Import other necessary modules and functions here
    
    # You can call your functions or perform other actions here
    # For example, call your generate_daily_report function with a sample date:
    sample_date = date(2023, 11, 7)  # Replace with your desired date
    generate_daily_report(sample_date)